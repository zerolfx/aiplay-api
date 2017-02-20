from django.conf.urls import url
from .views import (
    ProblemCreateAPI,
    ProblemDetailAPI,
    TagAIP,
)

urlpatterns = [
    url(r'^create/', ProblemCreateAPI.as_view(), name='problem create'),
    url(r'^detail/(?P<id>[\d]+)', ProblemDetailAPI.as_view(), name='problem detail'),
    url(r'^tag/(?P<name>[\w]+)', TagAIP.as_view()),
]
