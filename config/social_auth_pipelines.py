import logging

logger = logging.getLogger(__name__)


def log_associated_user(backend, uid, user=None, social=None, *args, **kwargs):
    """
    Logs the user already associated with the social account.
    """
    if social:
        logger.info(
            f"Social account already associated with user:"
            f" {social.user} (username: {social.user.username})"
        )
    else:
        # Query the social account manually if it isn't passed
        social_model = backend.strategy.storage.user.get_social_auth_model()
        try:
            social = social_model.objects.get(provider=backend.name, uid=uid)
            logger.info(
                f"Found social account linked to user:"
                f" {social.user} (username: {social.user.username})"
            )
        except social_model.DoesNotExist:
            logger.info(f"No social account found for provider {backend.name} and uid {uid}.")
    return None
