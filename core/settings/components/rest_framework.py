"""Django Rest Framework configurations.

At this module you will add the DRF config to septate them
from other configurations.
"""
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    # this is not a best practice but since I will not apply any auth
    # so it is fine or the better solution was to disable the
    # auth on the view level
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}
