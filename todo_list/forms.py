from django import forms
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
        widgets = {
            'item': forms.TextInput(attrs={
                'class': 'form-control mr-sm-2',
                'placeholder': 'Add a new task...'
            })
        }
