from django.contrib.auth.models import User
from django.db import models
import random


def _random_avatar():
    return "/static/avatar/avatar-" + str(random.randint(1, 2)) + ".jpg"


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.CharField(max_length=50, default=_random_avatar())
    first_name = models.CharField('First Name', max_length=30, blank=True)
    last_name = models.CharField('Last Name', max_length=30, blank=True)
    birth_date = models.DateField('Birth Date', blank=True, null=True)
    country = models.CharField('Country', max_length=30, blank=True)
    city = models.CharField('City', max_length=30, blank=True)
    organization = models.CharField('Organization', max_length=80, blank=True)

    rating = models.IntegerField('rating', default=0)

    def __str__(self):
        return self.user.username + '-Profile'
