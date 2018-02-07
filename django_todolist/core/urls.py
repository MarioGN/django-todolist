from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete_task, 'delete'),
    path('<str:filter>/', views.index, name='index_filter'),
]
