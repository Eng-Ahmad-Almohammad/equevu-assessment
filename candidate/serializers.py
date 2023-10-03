"""Provide serializers that will be used in the views."""

from pathlib import Path

from django.utils.translation import gettext as _
from rest_framework import serializers

from candidate.models import Candidate, Departments


class CandidateSerializer(serializers.ModelSerializer):
    """Serializer for the Candidate model.

    This serializer is used to serialize and deserialize Candidate instances.
    """

    department = serializers.ChoiceField(choices=Departments.choices, write_only=True)
    department_display = serializers.CharField(
        source="get_department_display",
        read_only=True,
    )
    resume = serializers.FileField(write_only=True)

    class Meta:
        """Serializer options."""

        model = Candidate
        fields = [
            "id",
            "full_name",
            "date_of_birth",
            "years_of_experience",
            "department",
            "department_display",
            "resume",
        ]

    def validate_resume(self, resume):
        """
        Validate the 'resume' field to check for allowed file extensions.

        Args:
            resume (file): The uploaded file to be validated.

        Returns:
            file: The validated file if it meets the extension requirements.

        Raises:
            ValidationError: If the file extension is not allowed.

        """
        allowed_extensions = ["pdf", "docx"]
        extension = Path(resume.name).suffix[1:].lower()

        if extension not in allowed_extensions:
            message = _(
                "File extension '{extension}' is not allowed. Allowed extensions are: {allowed_extensions}.",
            ).format(
                extension=extension,
                allowed_extensions=", ".join(allowed_extensions),
            )

            raise serializers.ValidationError(message)
        return resume


class CandidateResumeSerializer(serializers.ModelSerializer):
    """Serializer for the Candidate model.

    This serializer is used to serialize and deserialize Candidate instance and show only id and resume.
    """

    class Meta:
        """Serializer options."""

        model = Candidate
        fields = ["id", "resume"]
