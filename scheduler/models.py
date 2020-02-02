from django.db import models

# Create your models here.
class Schedule(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    category = models.IntegerField()

    def __str__(self):
        return self.title
