from django.contrib import admin
from .models import Resume
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
	list_display=[
		'user_job',
		'user_full_name', 
	]
	fieldsets=[
		('User Info', {
			'fields' : [
				'user_image',
				'user_full_name',
				'user_job',
				'user_description',
				]
			}
		),
		('User Experience', {
			'fields' : ['user_experience',]
			}
		),
		('User Knowledge', {
			'fields' : ['user_knowledge']
			}
		),
		('User Skill', {
			'fields' : ['user_skill']
			}
		),
		('Achivement', {
			'fields' : ['user_achievement']
			}
		),
		('Extra Information', {
			'fields' : ['extra_info']
			}
		),
	]

	formfield_overrides={
        models.TextField : {'widget' : TinyMCE},
    }

admin.site.register(Resume, ResumeAdmin)	