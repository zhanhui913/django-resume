from django.contrib import admin

from .models import School, Education


class EducationInline(admin.TabularInline):
	model = Education
	extra = 3

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,   {'fields' : ['name']}),
		('City', {'fields' : ['location'], 'classes':['collapse']})
	]
	inlines = [EducationInline]
	list_display = ('name','location')
	list_filter = ['location','name']
	search_fields = ['location','name']
