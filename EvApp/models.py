from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=200,null=False)
    image=models.ImageField(upload_to='image',null=False)
    description=models.TextField(null=True)


    def __str__(self):
        return self.name
    
class CustUser(AbstractUser):
    is_officer=models.BooleanField(default=False)
    departments=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

class Complaint(models.Model):
    username=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    address=models.TextField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    email=models.EmailField(null=True)
    complaint_description=models.TextField()
    image=models.ImageField(upload_to='images',null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    feedback=models.TextField(null=True)
    detail_head=models.CharField(max_length=25,null=True)
    detail_report=models.TextField(null=True)




    def __str__(self):
        return self.complaint_description
    



    


