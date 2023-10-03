"""Module that contain all candidates app models."""

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext as _

from candidate.utils import resume_upload_path


class BaseModel(models.Model):
    """Inheriting this model will create timestamps fields.

    Since most of the models have timestamp fields so we created a
    base model that can be inherited to follow the DRY principle
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Model options."""

        abstract: bool = True

    def __str__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object,
            which is the created_at attribute.
        """
        return self.created_at


class Departments(models.TextChoices):
    """Enum that has the departments information."""

    it: tuple = "it", _("IT")
    hr: tuple = "hr", _("HR")
    finance: tuple = "finance", _("Finance")


class Candidate(BaseModel):
    """DB model that will be used to access the candidate_candidate table."""

    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"))
    years_of_experience = models.FloatField(verbose_name=_("Years of Experience"))
    department = models.CharField(
        max_length=10,
        choices=Departments.choices,
        verbose_name=_("Department"),
    )
    resume = models.FileField(
        upload_to=resume_upload_path,
        verbose_name=_("Resume"),
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "docx"])],
    )

    class Meta:
        """Model options."""

        verbose_name = _("Candidate")
        verbose_name_plural = _("Candidate")

    def __str__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object,
            which is the full_name attribute.
        """
        return self.full_name
