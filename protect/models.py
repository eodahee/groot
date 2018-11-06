from django.db import models

class Member(models.Model) :
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_phonenumber = models.IntegerField()
    user_address = models.CharField(max_length=50)