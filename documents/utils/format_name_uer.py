from django.core.handlers.wsgi import WSGIRequest


def format_name(request: WSGIRequest) -> str:
    """
    Rename Anonymizer to Guest
    """
    name = str(request.user)

    return name if name != "AnonymousUser" else "Гость"
