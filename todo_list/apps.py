from django.apps import AppConfig
from .models import forms
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
