# from django.http import HttpResponse
from django.shortcuts import render

from. models import place
from.models import names
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=names.objects.all()

    return  render(request,'index.html',{'result':obj,'result1':obj1})

# def add(request):
#     x = int(request.GET['no1'])
#     y = int(request.GET['no2'])
#     a = x + y
#     b= x - y
#     c= x * y
#     d= x / y
#     return render(request, 'alu.html', {'result1': a,'re2':b,'re3':c,'re4':d})
