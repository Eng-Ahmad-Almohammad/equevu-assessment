"""
This module is used to provide configuration, fixtures, and plugins for pytest.

It may be also used for extending doctest's context:
1. https://docs.python.org/3/library/doctest.html
2. https://docs.pytest.org/en/latest/doctest.html
"""

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from candidate.models import BaseModel, Candidate


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture(name="candidate")
def create_candidate():
    resume_file = SimpleUploadedFile(
        "resume.pdf",
        b"This is a sample resume content.",
        content_type="application/pdf",
    )
    return Candidate.objects.create(
        full_name="John Doe",
        date_of_birth="2000-01-01",
        years_of_experience=2,
        department="hr",
        resume=resume_file,
    )
