from django.db import models

#Create your models here.
class naive_user(models.Model):
	GENDER =(('Male','Male'),
			('Female','Female'),
			('Prefer Not To Say','Prefer Not To Say'),
			)
	# datedue_calc = datetime.datetime.now()+datetime.timedelta(months=3)
	username = models.CharField(max_length=60,unique=True,primary_key=True)
	name = models.CharField(max_length=200,null=True) 
	gender = models.CharField(max_length=200,choices=GENDER,null=True)
	dob = models.DateTimeField(null=True)
	age = models.IntegerField(null=True)
	address = models.TextField(null=True)
	email = models.EmailField(null=True)
	contact = models.BigIntegerField(null=True)
	datecreated = models.DateTimeField(auto_now_add=True,null=True)
	# datedue = models.DateTimeField(null=True)
	medicalhistory = models.TextField(null=True)
	sideeffects = models.TextField(null=True)
	priscription = models.TextField(null=True)
	remarks = models.TextField(null=True)

	def __str__(self):
		return self.username

