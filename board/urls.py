from projectmanagement.views import add_card
from django.contrib import admin
from django.urls import path
from .import views

app_name = 'board'

urlpatterns = [
    path('', views.board, name="myboard")
]
