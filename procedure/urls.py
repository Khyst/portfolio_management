from django.contrib import admin
from django.urls import path

import procedure.views

urlpatterns = [
    path('home/', procedure.views.procedure, name="dashboard"),
    path('plan/', procedure.views.procedure, name="plan"),
    path('detail/<pk>', procedure.views.procedure, name="detail"),
    path('create/', procedure.views.create, name="create"),
    path('subject_create/', procedure.views.subject_create, name="sub_create"),
    path('post_create/', procedure.views.posting_create, name="post_create"),
    path('list/', procedure.views.list, name="list"),
    path('schedule/', procedure.views.schedule, name="schedule"),
]
