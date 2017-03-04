from django.db import models
from jsonfield import JSONField
import json
from tagging.registry import register
from tagging.fields import TagField


def get_default_properties():
    return json.dumps({"max_time": 1000,
                       "max_sum_time": 10000,
                       "max_memory": 256
                      }
                     )
STATUS_CHOICES = (
    ('r', 'Removed'),
    ('a', 'Available'),
)
COMBAT_TYPE_CHOICES = (
        (1, 'Single'),
        (2, 'Combat'),
)


class Problem(models.Model):
    id = models.IntegerField('#', primary_key=True)
#     tags = TagField()
    title = models.CharField('Title', max_length=70)
    properties = JSONField('properties', default=get_default_properties)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES, default='a')
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(str(self.id), self.title)

register(Problem)
