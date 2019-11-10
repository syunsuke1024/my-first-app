
from django.contrib import admin
from django.urls import path,include
from .views import FukushuList,FukushuDetail,FukushuCreate,FukushuDelete,FukushuUpdate

urlpatterns = [
    path('list/',FukushuList.as_view(),name='list'),
    path('detail/<int:pk>',FukushuDetail.as_view(),name='detail'),
    path('create/',FukushuCreate.as_view(),name='create'),
    path('delete/<int:pk>',FukushuDelete.as_view(),name='delete'),
    path('update/<int:pk>',FukushuUpdate.as_view(),name='update'),
]
