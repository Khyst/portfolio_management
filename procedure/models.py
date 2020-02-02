from django.db import models

class Subject(models.Model):

    #author = models.OneToOneField(User, on_delete=models.CASCADE)
    #author은 User과 subject를 1:N 구조로 이어주는 Key

    title = models.CharField(max_length=100)
    procedure = models.IntegerField()
    this_week_proceed = models.IntegerField()
    last_study = models.DateTimeField()
    time = models.IntegerField()
    category = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class refPost(models.Model):
    obj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #obj는 Subject과 refPost를 1:다 구조로 이어주는 Key
    o_id = models.IntegerField(default=0)
    reference = models.TextField()
    comment = models.TextField()
    intro_image = models.ImageField()

    def __str__(self):
        return self.title

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

