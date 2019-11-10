from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Photo

def index(request):
    photos=Photo.objects.all().order_by('-created_at')
    return render(request,'photosns/index.html',{'photos':photos})

def users_detail(request,pk):
    user = get_object_or_404(User,pk=pk)
    return render(request,'photosns/users_detail.html',{'user':user})