from django.shortcuts import render
from models import  bug
# Create your views here.

def index(request):
    return render(request, 'inex.html', {})


def addcotant(request):
        content = request.POST["content"]
        contract = request.POST["contract"]
        check_box_list = request.REQUEST.getlist('check_box_list')
        select = request.POST["contract_way"]
        img = request.FILES['photo']
        feedback = bug()
        feedback.content = content
        feedback.contract = contract
        question = ','.join(check_box_list)
        feedback.question = question
        image = img
        feedback.image.put(image, filename=img._name)
        feedback.contract_way = select
        feedback.save()

        return  render(request, 'inex.html', {'feedback': feedback})

