from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Subject, Posting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.

def schedule(request):
    return render(request, 'schedule.html')
    
def create(request):
    if request.user.is_authenticated:
        subject = Subject.objects.filter(author = request.user)
        ref = Posting.objects.filter(author = request.user)
        
    else:
        subject = Subject.objects.filter(title = "none")
        ref = Posting.objects.filter(post_id = -1)

    """sub_title = request.GET['p_title']
    link1 = request.GET['link1']
    link2 = request.GET['link2']
    category = request.GET['category']
    tag = request.GET['tag']
    file = request.GET['file']
    contents = request.GET['contents']
    """

    return render(request, 'create.html', {'subject':subject, 'ref':ref })

def list(request):
    return render(request, 'list.html')

def procedure(request):
    if request.user.is_authenticated:
        subject = Subject.objects.filter(author = request.user)
        #ref = Posting.objects.filter(author = request.user)
    else:
        subject = Subject.objects.filter(title = "none")
        #ref = Posting.ojbects.filter(title = "none")

    ref = Posting.objects.all()
    
    paginator = Paginator(subject,5)
    page = request.GET.get('page')
    subject_post = paginator.get_page(page)
    
    return render(request, 'plan.html', { 'subject':subject, 'ref':ref, 'subject_post':subject_post }) # Dictionery 형태로 QuereySet을 전달

"""
    - ICON class name -

    *Developing : ni ni-atom
    *License : ni ni-badge
    *Blog : fa fa-home
    *Language :
    *Brain :
    *Psychology :
    *Workout : 
    *Activity :

"""
def swtich_icon(request):
    pass

