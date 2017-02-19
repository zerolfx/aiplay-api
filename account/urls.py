from django.conf.urls import url
from .views import (
    UserRegisterAPI,
    TestViewAPI,
    UserAbstractAPI,
    UserDetailAPI,
)

urlpatterns = [
    url(r'^register/', UserRegisterAPI.as_view(), name="register"),
    url(r'^test/', TestViewAPI.as_view()),
    url(r'^abstract/(?P<username>[\w-]+)/$', UserAbstractAPI.as_view(), name="user abstract"),
    url(r'^detail/(?P<username>[\w-]+)/$', UserDetailAPI.as_view(), name="user detail"),
]
