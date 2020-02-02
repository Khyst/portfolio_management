from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.show_calendar, name="calendar"),
    path('add_scehdule/', views.add_sch, name="add_schedule"),
]