"""Storage configuration for media storage.

At this point this module is configured to support cloud storage
easily you can change between cloud providers by changing the config variables
read more https://django-storages.readthedocs.io/en/latest/index.html
or you can back to the default file system storage by removing
the STORAGE variable.
"""

import os

import environ

from core.settings.components.common import BASE_DIR

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
env = environ.Env(
    AWS_ACCESS_KEY_ID=(str, ""),
    AWS_SECRET_ACCESS_KEY=(str, ""),
    AWS_PRIVATE_BUCKET_NAME=(str, ""),
    AWS_S3_REGION_NAME=(str, ""),
    AWS_S3_ENDPOINT=(str, ""),
    AWS_S3_ENDPOINT_URL=(str, ""),
    MEDIA_STORAGE=(str, "django.core.files.storage.FileSystemStorage"),
)

STORAGES = {
    "default": {
        "BACKEND": env("MEDIA_STORAGE"),
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT = env("AWS_S3_ENDPOINT")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
