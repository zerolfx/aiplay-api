from django.contrib.auth.models import AbstractUser
from django.db import models
import random


def _random_avatar():
    return "/static/avatar/avatar-" + str(random.randint(1, 2)) + ".jpg"


class User(AbstractUser):
    avatar = models.CharField(max_length=50, default=_random_avatar)
    about = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField('Birth Date', blank=True, null=True)
    country = models.CharField('Country', max_length=30, blank=True)
    city = models.CharField('City', max_length=30, blank=True)
    organization = models.CharField('Organization', max_length=80, blank=True)
    rating = models.IntegerField('rating', default=0)

    class Meta:
        db_table = 'user'
