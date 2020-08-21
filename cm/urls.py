from django.contrib import admin
from django.urls import path
from cm import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transfer_credit', views.transfer_credit, name='transfer_credit'),
    path('transfer_history', views.transfer_history, name='transfer_history'),
    path('user/<str:name>', views.user, name='user'),
    path('user/<str:name>/confirmation', views.confirmation, name='confirmation')
]