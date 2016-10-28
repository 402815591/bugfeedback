from django.shortcuts import render
from models import  bug
from models import  Imgfiles
# Create your views here.


def index(request):
    return render(request, 'inex.html', {})

def addcotant(request):
        content = request.POST["content"]
        contract = request.POST["contract"]
        check_box_list = request.REQUEST.getlist('check_box_list')
        select = request.POST["contract_way"]
        img = request.FILES.getlist('photo')
        # print img
        feedback = bug()
        feedback.content = content
        feedback.contract = contract
        question = ','.join(check_box_list)
        feedback.question = question
        feedback.contract_way = select

        for f in img:
            print f, f._name
            feedbackimg = Imgfiles()
            feedbackimg.img_content.put(f, filename=f._name)
            feedback.image.append(feedbackimg)
        feedback.save()
        return  render(request, 'inex.html', {'feedback': feedback})
