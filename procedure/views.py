from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Subject, refPost

# Create your views here.

def schedule(request):
    return render(request, 'schedule.html')
    
def create(request):
    return render(request, 'create.html')

def list(request):
    return render(request, 'list.html')

def procedure(request):
    """Whole QuerySet of models (User, Subject, refPost)"""
    #user = User.objects.all()
    subject = Subject.objects.all()
    ref = refPost.objects.all()

    """particular QuerySet of models (User, Subject, refPost)"""
    """====================================================================================================================================================="""

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # *all() : Returns a copy of the current QuerySet (or QuerySet subclass). 
    # This can be useful in situations where you might want to pass in either a model manager or a QuerySet and do further filtering on the result.
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # *get() : there is only one object that matches your query, you can use the get() method on a Manager which returns the object directly:
    # -> If there are no results that match the query, get() will raise a DoesNotExist exception.
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # *filter() : always give you a QuerySet, even if only a single object matches the query - in this case, it will be a QuerySet containing a single element.
    # -> single element with filter() : using filter() with a slice of [0]
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    """
    user_1 = User.objects.get(user_name="khyst")
    subject_1 = Subject.objects.get(title="Python Learnig")
    ref_1 = refPost.objects.filter()
    """

    
    # *** Exception of Method: get() *** ( from django.core.exceptions )
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # get() raises MultipleObjectsReturned 
    # if more than one object was found. The MultipleObjectsReturned exception is an attribute of the model class.
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # get() raises a DoesNotExist exception 
    # if an object wasn’t found for the given parameters. This exception is an attribute of the model class
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    user_1 = User.objects.filter()
    subject_1 = Subject.objects.filter()
    ref_1 = refPost.objects.filter()
    """

    """====================================================================================================================================================="""

    #user_1 = User.objects.get(user_name="khyst")
    #subject_1 = Subject.objects.get(title="Python Learnig")
    #ref_1 = refPost.objects.filter()
  
    # Backward Accessing
    """   
    querysetOfUsertoSubject = user_1.subject_set(title="Python Learning")
    querysetOfUsbjectorefPost = subject_1.refpost_set()
    """
    
    # Foreward Accessing
    # querysetOfSubjecttoUser = subject_1.user.user_name
    # querysetOfrefPosttoSubject = ref_1.subject.title

    paginator = Paginator(subject,5)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
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

