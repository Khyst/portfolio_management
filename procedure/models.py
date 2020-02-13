from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver

class Profile(models.Model):  
    """ 유저 개인정보 """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.TextField(default="소개하는 글이 없습니다.")
    detail = models.TextField(default="자세한 정보 글이 없습니다.")
    birth_date = models.DateField(null=True, blank=True)


    """ 유저 주소정보 """
    address = models.CharField(max_length=40, blank=True)
    statue = models.CharField(max_length=10)
    county = models.CharField(max_length=10)
    postcode = models.CharField(max_length=6)

    """ 유저 활동량 """
    countProject = models.IntegerField(null=True, blank=True, default=0)
    countPortfolio = models.IntegerField(null=True, blank=True, default=0)
    countComment = models.IntegerField(null=True, blank=True, default=0)


    """Django User model 내장 필드"""
    # username 
    # last_name
    # first_name
    # email

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()

class Subject(models.Model):

    #author = models.OneToOneField(User, on_delete=models.CASCADE)
    #author은 User과 subject를 1:N 구조로 이어주는 Key

    author = models.ForeignKey(User, on_delete=models.CASCADE, default="") # User accout와 연결
    title = models.CharField(max_length=100)
    procedure = models.IntegerField()

    # 초기에 Subject작성시 NULL인 상태로 생성
    this_week_proceed = models.IntegerField(null=True)
    last_study = models.DateTimeField(null=True)
    time = models.IntegerField(null=True)

    category = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Posting(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    post_obj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #obj는 Subject과 Posting를 1:다 구조로 이어주는 Key

    post_id = models.IntegerField(default=0)
    post_title = models.CharField(default="", max_length=200)

    reference = models.TextField()
    description = models.TextField()

    intro_image = models.ImageField()

    def __str__(self):
        return self.post_title

class timeAmount(models.Model):
    totalWeeklyAmount = models.IntegerField()
    totalMonthlyAmount = models.IntegerField()

    def __str__(self):
        return self.title

class schedule(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()

    # period_date is (start_date ~ end_date)
    start_date = models.DateField()
    end_date = models.DateField()

    category = models.IntegerField()
    is_repeat_event = models.BooleanField()


    def __str__(self):
        return self.title

