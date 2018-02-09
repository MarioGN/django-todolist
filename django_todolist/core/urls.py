from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/<str:filter>', views.delete_task, name='delete'),
    path('complete/<int:pk>', views.complete_task, name='complete'),
    path('<str:filter>/', views.index, name='index_filter'),
]
