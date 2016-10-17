from django.db import models
# Create your models here.
from django.db.models import *
from django.db.models import CharField
from functools import partial
# StringField = partial(CharField, max_length=255)
#
# class TestModel(Model):
#     test_key = StringField(required=True)
#     test_value = StringField(max_length=50)