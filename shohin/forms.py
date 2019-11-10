from django import forms
from .models import Shohin

class ShohinForm(forms.ModelForm):
    class Meta:
        model=Shohin
        exclude=()
        fields=['shohinmei','tenmei','kakaku','create_at']

class FindForm(forms.Form):
    find = forms.CharField(label='検索',required=False)