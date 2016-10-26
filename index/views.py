from django.shortcuts import render
from models import  TESTTEST
# Create your views here.

def index(request):
    return render(request, 'inex.html', {})


def addcotant(request):
        content = request.POST["content"]
        contract = request.POST["contract"]
        check_box_list = request.REQUEST.getlist('check_box_list')
        img = request.FILES['photo']
        leeq = TESTTEST()
        leeq.content = content
        leeq.contract = contract
        question = ','.join(check_box_list)
        leeq.question = question
        leeq.image = img
        leeq.save()
        leeq.image.read()
        return  render(request, 'inex.html', {'leeq': leeq})
