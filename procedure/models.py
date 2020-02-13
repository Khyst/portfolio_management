from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver


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

