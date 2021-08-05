
from django.contrib import admin
from django.urls import path
from .import views

app_name = 'board'

urlpatterns = [
    path('', views.board_dashboard, name="dashboard"),
    path('project/', views.project, name="thisproject")

]
