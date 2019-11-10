from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from .models import FukushuModel
from django.urls import reverse_lazy
# Create your views here.


class FukushuList(ListView):
    template_name = 'list.html'
    model = FukushuModel

class FukushuDetail(DetailView):
    template_name = 'detail.html'
    model = FukushuModel

class FukushuCreate(CreateView):
    template_name = 'create.html'
    model = FukushuModel
    fields = ('title','problem1','date1','problem2','date2','problem3','date3','problem4','date4')
    success_url = reverse_lazy('list')

class FukushuDelete(DeleteView):
    template_name = 'delete.html'
    model = FukushuModel
    success_url = reverse_lazy('list')

class FukushuUpdate(UpdateView):
    template_name = 'update.html'
    model = FukushuModel
    fields = ('title', 'problem1', 'date1', 'problem2', 'date2', 'problem3', 'date3', 'problem4', 'date4')
    success_url = reverse_lazy('list')