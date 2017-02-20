from rest_framework import generics, mixins

from .serializers import ProblemSerializer
from .models import Problem


class ProblemCreateAPI(generics.CreateAPIView):
    serializer_class = ProblemSerializer


class ProblemDetailAPI(generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin):
    queryset = Problem.objects.all()
    lookup_field = 'id'
    serializer_class = ProblemSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)
