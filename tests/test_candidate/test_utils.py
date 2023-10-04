import pytest

from candidate.utils import resume_upload_path


@pytest.mark.django_db()
def test_creating_upload_path(candidate):
    file_name = "Equevu_-__Software_Engineer_task.pdf"
    actual_upload_path = resume_upload_path(candidate, file_name)

    expected_path = "candidates/John_Doe-{0}/{1}".format(
        candidate.created_at.strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3], file_name
    )

    assert actual_upload_path == expected_path
