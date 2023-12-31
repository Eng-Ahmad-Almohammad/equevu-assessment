"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `development`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ

from split_settings.tools import include

ENV = environ.get("DJANGO_ENV") or "development"

base_settings = [
    "components/common.py",  # standard django settings
    "components/db.py",  # postgres
    "components/rest_framework.py",  # django rest framework settings
    "components/storage.py",
    # You can even use glob:
    # 'components/*.py'
    # Select the right env:
    "environments/{0}.py".format(ENV),
]

# Include settings:
include(*base_settings)
