from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Subject, Posting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.

def schedule(request):
    return render(request, 'schedule.html')

def subject_create(request):
    #subject = Subject.objects.create(author = request.user)
    #print(subject)

    subject = Subject()

    if request.user.is_authenticated:
        # print('user is authenticated')

        subject.author = request.user

        # print(request.POST['title'])
        # print(request.POST['sub'])
        # print(request.POST['desc'])
        # print(request.POST['category'])

        subject.title = request.POST['title']
        subject.sub = request.POST['sub']
        subject.desc = request.POST['desc']
        subject.category = request.POST['category']

        subject.save(force_insert=True)

        return redirect('create')

    else:
        print('user is un_authenticated')
        return redirect('create')

def posting_create(request):

    #subject = Subject.objects.get(sub_id=request.POST['category'])
    posting = Posting()
    subject = Subject.objects.filter(pk=1)
    instance_of_posting = subject.posting

    print("============================================")
    print(instance_of_posting)
    print("============================================")

    if request.user.is_authenticated:

        instance_of_posting.author = request.user
        #posting.post_obj = subject.title

        instance_of_posting.post_title = request.POST['p_title']
        instance_of_posting.post_link_1 = request.POST['link1']
        instance_of_posting.post_link_1 = request.POST['link2']

        #posting.category = request.POST['category']

        #posting.tag = request.POST['tag']
        instance_of_posting.post_file = request.POST['file']

        #posting.reference = request.P
        instance_of_posting.post_desc = request.POST['contents']

        #instance_of_posting.save(force_insert=True)

        return redirect('create')
        
    else:
        print('user is un_authenticated')
        return redirect('create')

def create(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.filter(author=request.user)

        paginator = Paginator(subjects,3)
        page = request.GET.get('page')
        subject_post = paginator.get_page(page)

        return render(request, 'create.html', {'subject': subjects, 'subject_post':subject_post})
    else:
        return render(request, 'create.html')


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
    
    paginator = Paginator(subject,6)
    page = request.GET.get('page')
    subject_post = paginator.get_page(page)
    
    return render(request, 'plan.html', { 'subject':subject, 'ref':ref, 'subject_post':subject_post }) # Dictionery 형태로 QuereySet을 전달

"""
    - ICON class name -
    *Developing : ni ni-atom / *License : ni ni-badge / *Blog : fa fa-home / *Language : / *Brain : / *Psychology : / *Workout :  / *Activity :
"""

def swtich_icon(request):
    pass

