"""URL module that provides candidate endpoints."""

from django.urls import path

from candidate.views import CandidateListCreateView, ResumeRetrieveView

urlpatterns = [
    path("", CandidateListCreateView.as_view(), name="candidate_list_create"),
    path("<int:pk>/", ResumeRetrieveView.as_view(), name="resume_details"),
]
