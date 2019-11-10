from django import forms

class HelloForm(forms.Form):
    bunsekiCD=forms.CharField(label="分析CD")
    bunsekichi=forms.FloatField(label="分析値")
    tanka=forms.IntegerField(label="単価")
    
    
    
