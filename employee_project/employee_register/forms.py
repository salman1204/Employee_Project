from django import forms
from django.forms import ModelForm
from .models import *

# Create the form class.


class PersonalForm(ModelForm):
    YEARS = [x for x in range(1940, 2021)]
    date_birth = forms.DateField(initial="1993-5-27", widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model = personal_info
        fields = "__all__"


class JobForm(ModelForm):
    class Meta:
        model = job_info
        fields = "__all__"
