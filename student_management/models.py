from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    Roll_no=models.IntegerField(default=0)
    Name=models.CharField(max_length=30)
    Class=models.CharField(max_length=10)
    School=models.CharField(max_length=30)
    Mobile=models.IntegerField(default=0)
    Address=models.CharField(max_length=10)

class StudentAcademics(models.Model):
    Roll_no=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Biology=models.IntegerField()
    English=models.IntegerField()
    
   