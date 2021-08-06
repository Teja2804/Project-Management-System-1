
from django.contrib import admin
from django.urls import path
from .import views

app_name = 'board'

urlpatterns = [
    path('', views.board_dashboard, name="dashboard"),
    path('calendar/', views.calendar, name="calendar"),
    path('<slug:slug>/', views.project_detail ,name="detail")
]
