from django.db import models
# Create your models here.
# from django.db.models import *
# from django.db.models import CharField
# from functools import partial
# from mongoengine import *
# StringField = partial(CharField, max_length=255)
from mongoengine import *
connect('bugfeedback', host='192.168.100.201', port=27017)


class TESTTEST(Document):
    question = StringField()
    content = StringField(max_length=300)
    contract = IntField(max_length=15)
    image = FileField(upload_to='images/')

