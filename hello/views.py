from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

def index(request):
    params = {
            'title' : 'Hello/Index',
            'message'   : 'your data',
            'form'   :HelloForm()
            }
    if (request.method=="POST"):
        params['message']="分析CD"+request.POST["bunsekiCD"]+"分析値"+request.POST["bunsekichi"]+"単価"+request.POST["tanka"]
        params['form']=HelloForm(request.POST)
        
    
    return render(request,"hello/index.html",params)


def form(request):
    bunsekiCD=request.POST['bunsekiCD']
    params = {
            'title':'Hello/form',
            'bunsekiCD':'分析CDは'+bunsekiCD+"です",
            'goto'  : 'index',
            }
    return render(request,'hello/index.html',params)