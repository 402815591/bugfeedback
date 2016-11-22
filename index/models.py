
from mongoengine import *
from mongoengine.fields import IntField, StringField
from django.utils import timezone
import datetime


connect('test2', host='192.168.100.201', port=27017)


class Imgfiles(EmbeddedDocument):
    img_content = FileField(collection_name='fs')


class bug(Document):
    question = StringField()
    content = StringField(max_length=300)
    image = ListField(EmbeddedDocumentField('Imgfiles'))
    contract_way = StringField()
    contract = IntField(max_length=15)
    handle_status = BooleanField(default=False)
    subtime = DateTimeField(auto_now=True, default=datetime.datetime.now())
    updatebtime = DateTimeField(auto_now_add=True, default=timezone.now)


