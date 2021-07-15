from django.db import models

# Create your models here.
class Job(models.Model):
	job_title = models.CharField(max_length=30)
	job_type = models.CharField(max_length=30)
	job_description = models.CharField(max_length=30)

class User(models.Model):
	pass