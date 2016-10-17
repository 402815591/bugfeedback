from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'inex.html', {})

#
# entry = TestModel(test_key='arthur')
# entry.test_value = 'Wang'
# entry.save()