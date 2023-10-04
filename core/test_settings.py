"""Testing database configurations.

At this module you will add the test database config to septate them
from other configurations.
"""

from core.settings.components.common import *  # noqa: F403 F401 WPS347

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # Use an in-memory database for testing
    },
}
