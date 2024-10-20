from django.db import models


class Company(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	picture = models.ImageField(upload_to='static/images/company')
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'Company'
		ordering = ['date']
		verbose_name = 'Company'


class Employees(models.Model):
	name = models.CharField(max_length=150)
	surname = models.CharField(max_length=150)
	picture = models.ImageField(upload_to='static/images/employees')
	age = models.IntegerField()
	position = models.CharField(max_length=15)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'Employees'
		ordering = ['name']


class Report(models.Model):
	email = models.EmailField()
	date = models.DateField(auto_now_add=True)
	name = models.CharField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'Report'
		ordering = ['date']
