import time
from typing import Union

from django.core.exceptions import ValidationError
from django.utils.timezone import now

from domain.entity.invoice import Invoice
from domain.entity.payment import Payment
from landing_app.models import SubscriptionModel
from landing_app.models.payment import PaymentModel
from landing_app.service.email_notification_service import send_payment_failure_email


class PaymentService:
    MAX_RETRY_ATTEMPTS = 3
    RETRY_BACKOFF_TIME = 10

    @staticmethod
    def process_payment(invoice: Invoice, payment_method: str, amount: int) -> Union[Payment, bool]:
        try:
            existing_payment = PaymentModel.objects.filter(invoice=invoice,
                                                           status='success').first()
            if existing_payment:
                raise ValidationError("Duplicate payment attempt detected.")

            retry_count = 0
            while retry_count < PaymentService.MAX_RETRY_ATTEMPTS:
                try:
                    payment_status = PaymentService._process_with_gateway(payment_method, amount)

                    if payment_status == 'success':
                        payment = PaymentModel.objects.create(
                            invoice=invoice,
                            amount=amount,
                            payment_method=payment_method,
                            status='success',
                            payment_date=now()
                        )
                        if invoice.product.is_recurring:
                            SubscriptionModel.objects.filter(
                                user=invoice.user, product=invoice.product
                            ).update(until_date=now())
                        return True
                    elif payment_status == 'failed':
                        retry_count += 1
                        PaymentModel.objects.create(
                            invoice=invoice,
                            amount=amount,
                            payment_method=payment_method,
                            status='failed',
                            retry_count=retry_count,
                            payment_date=now()
                        )
                        if retry_count < PaymentService.MAX_RETRY_ATTEMPTS:
                            time.sleep(PaymentService.RETRY_BACKOFF_TIME * (
                                    2 ** (retry_count - 1)))  # Exponential backoff
                        else:
                            send_payment_failure_email(invoice.user,
                                                       "Payment failed after several attempts.")
                        return False
                    elif payment_status == 'timeout':
                        retry_count += 1
                        PaymentModel.objects.create(
                            invoice=invoice,
                            amount=amount,
                            payment_method=payment_method,
                            status='pending',
                            retry_count=retry_count,
                            payment_date=now()
                        )
                        if retry_count < PaymentService.MAX_RETRY_ATTEMPTS:
                            time.sleep(PaymentService.RETRY_BACKOFF_TIME * (
                                    2 ** (retry_count - 1)))  # Exponential backoff
                        else:
                            send_payment_failure_email(invoice.user,
                                                       "Payment gateway timeout after several attempts.")
                        return False

                except TimeoutError as e:
                    print(f"Payment timeout error: {str(e)}")
                    return False

                except ValidationError as e:
                    print(f"Payment validation error: {str(e)}")
                    return False

                except Exception as e:
                    send_payment_failure_email(
                        invoice.user, f"Unexpected error during payment: {str(e)}"
                    )
                    return False
        except Exception:
            return False

    @staticmethod
    def _process_with_gateway(payment_method: str, amount: int) -> str:
        from random import choice
        return choice(['success', 'failed', 'timeout'])
