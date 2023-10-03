"""Django internal configuration for configuring the candidate app."""
from django.apps import AppConfig


class CandidateConfig(AppConfig):
    """Class representing a candidate application and its configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "candidate"
