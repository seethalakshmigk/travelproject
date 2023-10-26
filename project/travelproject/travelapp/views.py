from django.shortcuts import render

from . models import *


def datas(request):
    product_data=Places.objects.all()
    return render(request,'details.html',{'products':product_data})
