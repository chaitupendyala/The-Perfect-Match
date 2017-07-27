from django.db import models
from django.contrib.auth.models import User

class User_Male(models.Model):
    basic_details = models.OneToOneField(User,unique = True,on_delete=models.CASCADE)
    mobile_number = models.IntegerField()
    date_of_birth = models.DateField()
    profile_picture = models.FileField()
    premium_user = models.BooleanField(default=False)

class User_Female(models.Model):
    basic_details = models.OneToOneField(User,unique = True,on_delete=models.CASCADE)
    mobile_number = models.IntegerField()
    date_of_birth = models.DateField()
    profile_picture = models.FileField()
    premium_user = models.BooleanField(default = False)

class question_responses(models.Model):
    basic_details = models.OneToOneField(User,on_delete=models.CASCADE)
    question1 = models.CharField(max_length=3)
    question2 = models.CharField(max_length=3)
    question3 = models.CharField(max_length=3)
    question4 = models.CharField(max_length=3)
    question5 = models.CharField(max_length=3)
