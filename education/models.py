from django.db import models

class School(models.Model):
	name = models.CharField(max_length=500)
	location = models.CharField(max_length=500)

	def __str__(self):
		return self.name;
	class Meta:
		verbose_name_plural = "Universities"	

class Education(models.Model):
	school = models.ForeignKey(School, related_name='school')
	degree = models.CharField(max_length=500)
	start_date = models.DateField('start date')
	end_date = models.DateField('end date')

	def __str__(self):
		return self.degree;