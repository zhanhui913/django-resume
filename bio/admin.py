from django.contrib import admin

from .models import Company, Employment, Duty, School, Education, Skill, Project, Biography

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

class EducationInline(admin.TabularInline):
	model = Education
	extra = 1

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,   {'fields' : ['name']}),
		(None, {'fields' : ['location']})
	]
	inlines = [EducationInline]
	list_display = ('name','location')
	list_filter = ['location','name']
	search_fields = ['location','name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' : ['name']}),
	]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,   {'fields' : ['name']}),
		(None, {'fields' : ['description']}),
		('Duration', {'fields' : [('start_date','end_date')]})
	]
	list_display = ('name','description','in_progress')
	list_filter = ['start_date','end_date']
	search_fields=['name','description']

@admin.register(Biography)
class BioAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,   {'fields' : ['name']}),
		(None, {'fields' : ['description']}),
		(None, {'fields' : ['email']}),
		(None, {'fields' : ['github']}),
	]
	list_display = ('name','email','github')	