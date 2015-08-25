from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Companies"

class Employment(models.Model):
	company = models.ForeignKey(Company, related_name='employment')
	position = models.CharField(max_length=100)
	start_date = models.DateField('start date')
	end_date = models.DateField('end date', null=True, blank=True)
	
	def __str__(self):
		return self.position

class Duty(models.Model):
	employment = models.ForeignKey(Employment, related_name='duty')
	task = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.task

	class Meta:
		verbose_name_plural = "Duties"


class School(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.name;
		
	class Meta:
		verbose_name_plural = "Universities"	

class Education(models.Model):
	school = models.ForeignKey(School, related_name='school')
	degree = models.CharField(max_length=100)
	major = models.CharField(max_length=100)
	start_date = models.DateField('start date')
	end_date = models.DateField('end date', null=True, blank=True)

	def __str__(self):
		return self.degree;

class Skill(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Skills"

class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=5000)
	start_date = models.DateField('start date')
	end_date = models.DateField('end date', null=True, blank=True)

	def in_progress(self):
		return self.end_date is None
	in_progress.boolean = True
	in_progress.short_description = 'Still in progress?'

	def __str__(self):
		return self.name;

	class Meta:
		verbose_name_plural = "Projects"

class Biography(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	email = models.EmailField(max_length=254)
	github = models.URLField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Biographies"