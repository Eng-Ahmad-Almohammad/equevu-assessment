"""Candidate views that is responsible to handel candidate views endpoints."""

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from candidate.models import Candidate
from candidate.permissions import IsAdminUserOrPostOnly
from candidate.serializers import CandidateResumeSerializer, CandidateSerializer

# Create your views here.


class CandidateListCreateView(ListCreateAPIView):
    """Responsible to create and list candidates data.

    THis view is responsible to accept post and get requests to create a
    new candidates or to list candidates data based on
    the serializer configuration.
    """

    queryset = Candidate.objects.order_by("-id").all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAdminUserOrPostOnly]


class ResumeRetrieveView(RetrieveAPIView):
    """Responsible to get specific candidates data.

    THis view is responsible to accept get request show
    a candidate data based on the serializer configuration.
    """

    queryset = Candidate.objects.all()
    serializer_class = CandidateResumeSerializer
    permission_classes = [IsAdminUserOrPostOnly]
