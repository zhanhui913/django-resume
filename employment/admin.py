from django.contrib import admin
from django.utils import timezone

from .models import Company, Employment, Duty

class DutyInline(admin.TabularInline):
	model = Duty
	extra = 5

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	fieldsets = [
		(None ,  {'fields' : ['name']}),
		('City', {'fields' : ['location']}),
	]
	list_display = ('name','location')

@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
	fieldsets = [
		(None , {'fields' : ['company']}),
		(None, {'fields' : ['position']}),
		('Duration', {'fields' : [('start_date','end_date')]})
	]
	list_display = ('position', 'company', 'start_date', 'end_date', 'duration')
	inlines = [DutyInline]

	def duration(self, obj):
		return (obj.end_date - obj.start_date)
