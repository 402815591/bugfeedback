# -*- coding: UTF-8 -*-
from django.shortcuts import render
from models import  bug
from models import  Imgfiles
from django.forms import CharField
from django import forms
# Create your views here.



class check_forms(forms.Form):
    content = forms.CharField(error_messages={"required": "反馈内容错误", })
    contract = forms.IntegerField(error_messages={"required": "联系方式错误", })
    contract_way = forms.CharField(error_messages={"required": "联系方式错误", })



    def clean(self):

        try:
            content = self.cleaned_data['content']
        except Exception as e:
            print 'except: ' + str(e)
            raise forms.ValidationError(u"建议内容不能为空")

        try:
            contract = self.cleaned_data['contract']
        except Exception as e:
            print 'except: ' + str(e)
            raise forms.ValidationError(u"联系方式不能为空")

        try:

            question = self.data['check_box_list']
            print question
        except Exception as e:
            print 'except: ' + str(e)
            raise forms.ValidationError(u"反馈的问题不能为空")

        return self.cleaned_data



def index(request):
    feedback = bug()
    if request.method == 'POST':
        try:
            feedback_form = check_forms(request.POST)

        except Exception as e:
            print str(e),

        if feedback_form.is_valid():
            check_box_list = request.REQUEST.getlist('check_box_list')
            if check_box_list:
                print "check success"
                try:
                    content = feedback_form.cleaned_data['content']
                    contract = feedback_form.cleaned_data['contract']
                    select = feedback_form.cleaned_data["contract_way"]

                    check_box_list = request.REQUEST.getlist('check_box_list')
                    question = ','.join(check_box_list)

                    img = request.FILES.getlist('photo')
                    for f in img:
                        print f, f._name
                        feedbackimg = Imgfiles()
                        feedbackimg.img_content.put(f, filename=f._name)
                        feedback.image.append(feedbackimg)

                    feedback.content = content
                    feedback.contract = contract
                    feedback.contract_way = select
                    feedback.question = question

                    feedback.save()

                except Exception as e:
                    print str(e)
            else:
                print "checklist not here"
            return render(request, 'inex.html', {'feedback_form': feedback_form})
    else:
        return render(request, 'index.html', {})
