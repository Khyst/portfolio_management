from django.db import models
from django.contrib.auth.models import AbstractUser, User, UserManager

# Create your models here.
class MyUser(AbstractUser):
    address = models.CharField("주소지", max_length=60, null=True, blank=True)
    created_on = models.DateTimeField("등록일자", auto_now_add=True)
    updated_on = models.DateTimeField("수정일자", auto_now=True)
    statue = models.CharField("도/특별/광역시", max_length=12, null=True, blank=True)
    county = models.CharField("시/군/구", max_length=12, null=True, blank=True)
    postcode = models.CharField("우편번호", max_length=6, null=True, blank=True)

    desc = models.TextField("자세한 정보", null=True, blank=True)
    profile_img = models.ImageField(null=True)


"""class history(models.Model):
    #profile = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    history = models.CharField(max_length=20, null=True, blank=True)
"""