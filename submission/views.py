from rest_framework.views import APIView
from rest_framework import mixins, generics

from .models import Submission
from .serializer import (
    SubmissionDetailSerializer,
    SubmissionAbstractSerializer,
    SubmissionCreateSerializer,
)


class SubmissionCreateAPI(generics.CreateAPIView):
    serializer_class = SubmissionCreateSerializer


class SubmissionDetailAPI(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Submission.objects.all()
    serializer_class = SubmissionDetailSerializer


class SubmissionAbstractAPI(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Submission.objects.all()
    serializer_class = SubmissionAbstractSerializer
