from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('(?P<filter>[\w\-]+)', views.index, name='index'),
]
