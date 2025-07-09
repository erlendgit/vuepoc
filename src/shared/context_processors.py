from django.conf import settings


def shared_context(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "DEBUG": settings.DEBUG,
        "LANGUAGE_CODE": settings.LANGUAGE_CODE,
    }
