from rest_framework import generics, mixins

from .serializers import ProblemSerializer, TagSerializer
from .models import Problem

from tagging.models import Tag


class ProblemCreateAPI(generics.CreateAPIView):
    serializer_class = ProblemSerializer


class ProblemListAPI(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class ProblemDetailAPI(generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       ):
    queryset = Problem.objects.all()
    lookup_field = 'id'
    serializer_class = ProblemSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TagAIP(generics.GenericAPIView,
             mixins.RetrieveModelMixin,
             mixins.DestroyModelMixin,
             ):
    queryset = Tag.objects.all()
    lookup_field = 'name'
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
