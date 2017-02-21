from django.db import models
from problem.models import Problem
from account.models import User

LANG_CHOICES = (
        ('c', 'C++'),
        ('j', 'Java'),
        ('p', 'Python')
    )


class Submission(models.Model):
    problem = models.ForeignKey(Problem)
    author = models.ForeignKey(User)
    language = models.CharField('Language', max_length=1, choices=LANG_CHOICES)
    code = models.TextField('Code')
    submit_time = models.DateTimeField('Submit Time', auto_now_add=True)
