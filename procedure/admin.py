from django.contrib import admin
from .models import Subject, Posting, timeAmount, schedule

# Register your models here.
#admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Posting)
admin.site.register(timeAmount)
admin.site.register(schedule)