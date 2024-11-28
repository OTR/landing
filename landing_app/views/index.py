from django.conf import settings
from django.http import HttpResponse

def serve_html_file(request):
    path = str(settings.BASE_DIR / "static" / "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HttpResponse(html_content, content_type="text/html")
