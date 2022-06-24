from dataclasses import field
from django import forms
from .models import *


class TraineesForms(forms.ModelForm):
    class Meta:
        model = Trainees
        fields = '__all__'
