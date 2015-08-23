from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Companies"

class Employment(models.Model):
	company = models.ForeignKey(Company, related_name='employment')
	position = models.CharField(max_length=200)
	start_date = models.DateField('start date')
	end_date = models.DateField('end date')
	
	def __str__(self):
		return self.position

class Duty(models.Model):
	employment = models.ForeignKey(Employment, related_name='duty')
	task = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.task

	class Meta:
		verbose_name_plural = "Duties"
