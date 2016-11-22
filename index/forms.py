# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       forms
Date Created:   2015-12-12 21:11
Description:

"""
from django import forms
from duckadmin import DuckForm
from redis import StrictRedis
from models import bug as Bug, Imgfiles

redis_client = StrictRedis(decode_responses=True)


class MyRedisForm(DuckForm):
    app_label = 'index'
    model_name = 'Feedback'
    verbose_name = 'Feedback'
    pk_name = 'id'

    id = forms.CharField(max_length=32)
    handle_status = forms.BooleanField(required=False)
    question = forms.CharField(max_length=255)
    content = forms.CharField(max_length=300)
    # image = forms.Imgfiles()
    contract_way = forms.CharField(max_length=255)
    contract = forms.IntegerField()

    @classmethod
    def get_count(cls, request):
        return Bug.objects.count()

    @classmethod
    def get_data(cls, request, start=None, stop=None):
        return Bug.objects.order_by("-subtime")

    @classmethod
    def get_data_by_pk(cls, request, pk):
        data = Bug.objects(pk=pk).first().to_json()
        import json
        _data = json.loads(data)
        _data["id"]=pk
        return _data

    @classmethod
    def create_data(cls, request, data):
        Bug(**data).save()

    @classmethod
    def update_data(cls, request, data):
        # pk = data['id']
        Bug(**data).save()
