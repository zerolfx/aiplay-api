from django.conf.urls import url
from .views import (
    SubmissionCreateAPI,
    SubmissionDetailAPI,
    SubmissionAbstractAPI,
)

urlpatterns = [
    url(r'^create/', SubmissionCreateAPI.as_view(), name='submission create'),
    url(r'^detail/(?P<id>[\d]+)', SubmissionDetailAPI.as_view(), name='problem detail'),
    url(r'^abstract/(?P<id>[\d]+)', SubmissionAbstractAPI.as_view(), name='problem detail'),
    # url(r'^tag/(?P<name>[\w]+)', TagAIP.as_view()),
]
