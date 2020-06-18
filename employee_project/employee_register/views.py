from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import *


# Create your views here.


def index(request):
    return render(request, "index.html", context={})


def personal_info(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse("employee_register:job_info"))
        else:
            print(form.errors)
    else:
        form = PersonalForm()

    return render(request, 'personal_info.html', {'form': form})


def job_info(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JobForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form = form.save()
            return HttpResponse("thank you")
        else:
            print(form.errors)
    else:
        form = JobForm()

    return render(request, 'job_info.html', {'form': form})
