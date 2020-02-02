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
