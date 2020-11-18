from django.urls import path

from app2 import views

app_name='app2'

urlpatterns=[
    path('specific_temp/',views.specific_temp,name='specific_temp'),
]