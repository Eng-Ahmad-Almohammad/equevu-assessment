import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from candidate.utils import resume_upload_path


@pytest.mark.django_db()
def test_missing_required(api_client):
    response = api_client.post(reverse("candidate_list_create"), data={})

    assert response.status_code == 400
    assert response.json().get("full_name") == ["This field is required."]
    assert response.json().get("date_of_birth") == ["This field is required."]
    assert response.json().get("years_of_experience") == ["This field is required."]
    assert response.json().get("department") == ["This field is required."]
    assert response.json().get("resume") == ["No file was submitted."]


@pytest.mark.django_db()
def test_wrong_date_formate(api_client):
    candidate = {
        "full_name": "John Doe",
        "date_of_birth": "2000/01/01",
        "years_of_experience": 2,
        "department": "hr",
    }
    response = api_client.post(reverse("candidate_list_create"), data=candidate)
    assert response.status_code == 400
    assert response.json().get("date_of_birth") == [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ]


@pytest.mark.django_db()
def test_unsupported_department_choice(api_client):
    candidate = {
        "full_name": "John Doe",
        "date_of_birth": "2000-01-01",
        "years_of_experience": 2,
        "department": "test",
    }
    response = api_client.post(reverse("candidate_list_create"), data=candidate)
    assert response.status_code == 400
    assert response.json().get("department") == ['"test" is not a valid choice.']


@pytest.mark.django_db()
def test_upload_unsupported_file_format(api_client):
    file_content = b"This is a sample text content."
    resume_file = SimpleUploadedFile(
        "sample.txt", file_content, content_type="text/plane"
    )
    candidate = {
        "full_name": "John Doe",
        "date_of_birth": "2000-01-01",
        "years_of_experience": 2,
        "department": "hr",
        "resume": resume_file,
    }
    response = api_client.post(reverse("candidate_list_create"), data=candidate)
    assert response.status_code == 400
    assert response.json().get("resume") == [
        "File extension 'txt' is not allowed. Allowed extensions are: pdf, docx."
    ]


@pytest.mark.django_db()
def test_successfully_create_a_candidate(api_client):
    file_content = b"This is a sample PDF content."
    resume_file = SimpleUploadedFile(
        "sample.pdf", file_content, content_type="application/pdf"
    )
    candidate = {
        "full_name": "John Doe",
        "date_of_birth": "2000-01-01",
        "years_of_experience": 2,
        "department": "hr",
        "resume": resume_file,
    }
    response = api_client.post(reverse("candidate_list_create"), data=candidate)
    assert response.status_code == 201
    assert response.json().get("id") == 1
    assert response.json().get("full_name") == "John Doe"
    assert response.json().get("date_of_birth") == "2000-01-01"
    assert response.json().get("years_of_experience") == 2.0
    assert response.json().get("department_display") == "HR"


@pytest.mark.django_db()
def test_unauthorized_list_request(api_client):
    response = api_client.get(reverse("candidate_list_create"))
    assert response.status_code == 403


@pytest.mark.django_db()
def test_authorized_list_request(api_client, candidate):
    response = api_client.get(reverse("candidate_list_create"), HTTP_X_ADMIN="1")
    assert response.status_code == 200
    response = response.json()
    assert len(response) == 1
    assert response[0]["full_name"] == "John Doe"


@pytest.mark.django_db()
def test_unauthorized_download_request(api_client, candidate):
    response = api_client.get(reverse("candidate_list_create"))
    assert response.status_code == 403


@pytest.mark.django_db()
def test_authorized_download_request(api_client, candidate):
    response = api_client.get(reverse("resume_details", args=["1"]), HTTP_X_ADMIN="1")
    assert response.status_code == 200
    assert response.json()["resume"] == "http://testserver/media/{0}".format(
        resume_upload_path(candidate, "resume.pdf"),
    )
