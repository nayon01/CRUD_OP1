from .views import *
from django.urls import path

urlpatterns = [
    path('', HomePage, name='homepage'),
    path('allProfile/', AllProfile, name='allProfile'),
    path('update/<id>/', Update, name='update'),
    path('delete/<id>/', Delete, name='delete'),
    path('view/<id>/', view, name='view'),



]
