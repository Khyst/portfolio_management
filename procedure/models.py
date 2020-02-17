from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

"""
                    << 모든 DB 초기화 >>

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
"""

class Subject(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="") # User accout와 연결
    title = models.CharField(max_length=100)
    procedure = models.IntegerField(default=0)

    this_week_proceed = models.IntegerField(null=True)
    last_study = models.DateTimeField(null=True)
    time = models.IntegerField(null=True)

    category = models.IntegerField(default=0)

class Posting(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    post_obj = models.ForeignKey(Subject, on_delete=models.CASCADE, default="")

    post_title = models.CharField(default="", max_length=200)
    reference = models.TextField()
    description = models.TextField()
    intro_image = models.ImageField(null=True)

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