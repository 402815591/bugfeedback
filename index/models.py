
from mongoengine import *
from mongoengine.fields import IntField, StringField


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
    handle_status = BooleanField(default=False)


