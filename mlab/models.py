from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dob = models.DateField()
    phno = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    def _str_(self):
        return self.user.username

class Tests(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()

class USER_RESULT(models.Model):
    userid   = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    testid   = models.ForeignKey(Tests,default=None,on_delete=models.CASCADE)
    testdate = models.DateField()
    testresult = models.FileField(upload_to='testresult')

    def _str_(self):
        return self.id


class general_user(models.Model):
    tstno  =  models.IntegerField()
    phno   =   models.IntegerField()
    tstrst =  models.FileField(upload_to='generalresult')
    def _str_(self):
        return self.id

class bloodsugar(models.Model):
    userid      = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    testdate    = models.DateField()
    observedval = models.IntegerField()
    fasting     = models.BooleanField (default=0)
    def _str_(self):
        return self.id

class cholesterol(models.Model):
    userid           = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    testdate         = models.DateField()
    totalcholesterol = models.IntegerField()
    ldl              = models.IntegerField()
    hdl              = models.IntegerField()
    triglycerides    = models.IntegerField()
    def _str_(self):
        return self.id

class urinalysis(models.Model):
    userid           = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    testdate         = models.DateField()
    color            = models.TextField()
    turpidity        = models.TextField()
    ph               = models.FloatField()
    glucose          = models.TextField()
    bilirubin        = models.TextField()
    blood            = models.TextField()
    protien          = models.TextField()
    leukocyte        = models.TextField()
    def _str_(self):
        return self.id

