from django.db import models



class sms(models.Model):

    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    percentage=models.IntegerField()
    year=models.IntegerField()
    location=models.CharField(max_length=49)
    college=models.CharField(max_length=50)
    universsity=models.CharField(max_length=50)
