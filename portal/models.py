from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.


class User(AbstractUser):
	department=models.CharField(max_length=50,null=False,blank=False)
	is_student=models.BooleanField(default=False)
	is_teacher=models.BooleanField(default=False)



class Document(models.Model):
	title = models.CharField(max_length=30, blank=False)
	document = models.FileField(upload_to='documents/', blank=False)
	message = models.TextField()
	uploaded_at = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.title

class student(models.Model):
	created = models.OneToOneField(User, on_delete=models.CASCADE)
	#code = models.CharField(max_length=10,unique=True)
	name= models.CharField(max_length=50)
	email = models.EmailField(max_length=50,null=False,blank=False)
	contact_no = models.CharField(max_length=10,null=False,blank=False)
	dept= models.CharField(max_length=50,null=False,blank=False)
	#image=models.ImageField(upload_to='image/%Y/%m/%d/',max_length=50,null=True,blank=True)
	address= models.CharField(max_length=100,null=False,blank=False)
	#parent
	father_name=models.CharField(max_length=50,null=False,blank=False)
	mother_name=models.CharField(max_length=50,null=False,blank=False)
	mobile_no=models.IntegerField(default=1,
        validators=[MaxValueValidator(9999999999), MinValueValidator(1)])
	parent_occu=models.CharField(max_length=50,null=False,blank=False)
	parent_income=models.CharField(max_length=50,null=False,blank=False)
	parent_qual=models.CharField(max_length=50,null=False,blank=False)
	#academic
	current_cgpa=models.CharField(max_length=50,null=False,blank=False)
	avg_cgpa=models.CharField(max_length=50,null=False,blank=False)
	ssc_marks=models.CharField(max_length=50,null=False,blank=False)
	hsc_marks=models.CharField(max_length=50,null=False,blank=False)
	stu_ach=models.CharField(max_length=50,null=False,blank=False)
	uploaded_at = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return "Proctor Form of user {}".format(self.created.username)
