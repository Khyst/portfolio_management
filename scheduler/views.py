from django.shortcuts import render, redirect
from .models import Schedule
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def show_calendar(request):
    schedules = Schedule.objects.all()
    #schedules(변수)에 Schedule(모델)의 쿼리셋을 담는다

    return render(request, 'calendar.html', {'schedules' : schedules})

def add_sch(request):
    schedule = Schedule()

    schedule.title = (request.POST.get('schedule_title'))
    schedule.contents = (request.POST.get('schedule_contents'))

    schedule.start_date = (request.POST.get('start_date'))
    schedule.end_date = (request.POST.get('end_date'))

    schedule.category = (request.POST.get('category'))

    schedule.save()

    return redirect('/scheduler/calendar/')

def json_serializer(request):
    schedules = Schedule.objects
    schedule_list = serializers.serialize('json', schedules)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")


    

