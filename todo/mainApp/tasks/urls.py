from unicodedata import name
from django.urls import path
from .import views
# urlpatterrns = [
#     path('', views.index)
# ]

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name= "update_task"),
    path('delete/<str:pk>/', views.deleteTask, name= "delete")
]