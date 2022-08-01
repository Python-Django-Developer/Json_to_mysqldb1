from django.shortcuts import render
from .models import Countriesdata


def index(request):
    emps=Countriesdata.objects.all()
    context={
        'emps':emps
    }
    return render(request,'index.html', context)