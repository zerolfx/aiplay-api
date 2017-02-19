from django.conf.urls import url
from .views import (
    UserRegisterAPI,
    TestViewAPI,
    UserAbstractAPI,
)

urlpatterns = [
    url(r'^register/', UserRegisterAPI.as_view(), name="register"),
    url(r'^test/', TestViewAPI.as_view()),
    url(r'^(?P<username>[\w-]+)/$', UserAbstractAPI.as_view(), name="abstract user")
]
