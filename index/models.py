from django.db import models
# Create your models here.
# from django.db.models import *
# from django.db.models import CharField
# from functools import partial
# from mongoengine import *
# StringField = partial(CharField, max_length=255)
from mongoengine import *
from gridfs import *
from datetime import timedelta
from mongoengine.base import BaseField
from mongoengine.fields import IntField, StringField
from django.db.models.fields.files import FieldFile

from bson import ObjectId


connect('test2', host='192.168.100.201', port=27017)

class Imgfiles(EmbeddedDocument):
    img_content = FileField(collection_name='fs')
    # img_content2 = FileField(collection_name='fs')
    # img_content3 = FileField(collection_name='fs')


class bug(Document):
    question = StringField()
    content = StringField(max_length=300)
    image = ListField(EmbeddedDocumentField('Imgfiles'))
    contract_way = StringField()
    contract = IntField(max_length=15)

