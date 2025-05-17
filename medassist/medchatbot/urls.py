from django.urls import path
from . import views

urlpatterns = [
    path('', views.medchat, name='medchat'),

]
