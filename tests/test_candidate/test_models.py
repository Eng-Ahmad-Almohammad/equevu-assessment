import pytest


@pytest.mark.django_db()
def test_candidate_models_string_representation(candidate):
    assert candidate.full_name == str(candidate)
