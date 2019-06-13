from django.shortcuts import render
from testapp.models import employee
from django.db.models.functions import Lower

def display(request):
    e1=employee.objects.get_queryset1()     #objects is not necessary we can write anything but then change in models.py
    dict={'e1':e1}
    return render(request,"Testapp/list.html",context=dict)
