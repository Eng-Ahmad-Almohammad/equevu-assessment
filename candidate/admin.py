"""Admin configuration modula for candidate's app models."""

from django.contrib import admin

from candidate.models import Candidate

# Register your models here.
admin.site.register(Candidate)
