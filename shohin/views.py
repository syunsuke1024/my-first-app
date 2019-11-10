from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Shohin
from .forms import ShohinForm
from .forms import FindForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def index(request,num=1):
    data=Shohin.objects.all()
    page=Paginator(data,3)
    params = {
        'title': 'Shohin',
        'message':'',
        'data':page.get_page(num),
    }

    return render(request, "shohin/index.html", params)
#@login_required
def create(request):
    if (request.method=='POST'):
        obj=Shohin()
        shohin=ShohinForm(request.POST,instance=obj)
        shohin.save()
        return redirect(to='/shohin')
    params={
        'title':'Shohin',
        'form':ShohinForm(),
    }
    return render(request,'shohin/create.html',params)

def edit(request,num):
    obj=Shohin.objects.get(id=num)
    if (request.method=='POST'):
        shohin=ShohinForm(request.POST,instance=obj)
        shohin.save()
        return redirect(to='/shohin')
    params={
        'title':'shohin',
        'id':num,
        'form':ShohinForm(instance=obj),
    }
    return render(request,'shohin/edit.html',params)

def delete(request,num):
    shohin=Shohin.objects.get(id=num)
    if (request.method=='POST'):
        shohin.delete()
        return redirect(to='/shohin')
    params={
        'title':'Shohin',
        'id':num,
        'obj':shohin,
    }
    return render(request,'shohin/delete.html',params)
@login_required
def find(request,num=1):

    if (request.method=='POST'):
        msg='search result'
        form=FindForm(request.POST)
        str=request.POST['find']
        data=Shohin.objects.filter(Q(tenmei__icontains=str) | Q(shohinmei__icontains=str) | Q(kakaku__icontains=str))
        page = Paginator(data, 5)
    else:
        msg='商品名、店名、価格に含まれる文字で検索します'
        form=FindForm()
        data=Shohin.objects.all()
        page = Paginator(data, 5)
    params={
        'title':'Shohin',
        'message':msg,
        'form':form,
        'data':page.get_page(num),
    }
    return render(request,'shohin/find.html',params)