from django import forms
from .models import Kounyu

class KounyuForm(forms.ModelForm):

    class Meta:
        model = Kounyu
        fields=['date','category','shozoku','shosha','tanka','kazu','memo']