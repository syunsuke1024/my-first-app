from django.urls import path
from . import views

app_name='kounyu'
urlpatterns = [
    path('kounyu_list/',views.KounyuListView.as_view(),name='kounyu_list'),
    path('kounyu_create/',views.KounyuCreateView.as_view(),name='kounyu_create'),
    path('create_done/',views.create_done, name='create_done'),
]