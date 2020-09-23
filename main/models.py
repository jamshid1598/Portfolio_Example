from django.db import models

# Create your models here.


class Resume(models.Model):
	# python -m pip install Pillow
	user_image = models.ImageField(
		upload_to ='images', 
		max_length=255,
		default='/images/user_image.jpg')
	user_full_name = models.CharField(
		max_length=200,
		verbose_name='Full Name'
		)
	user_job=models.CharField(
		max_length=250,
		blank=True,
		null=True,
		default='Programmer',
		)
	user_description=models.CharField(
		blank=True,
		null=True,
		max_length=500
		)
	user_experience=models.TextField(
		verbose_name='My Experience as a Django Developer',
		default='No experience:)'
		)
	user_knowledge=models.TextField(
		verbose_name='What I Know'
		)

	user_skill=models.TextField(
		verbose_name='Education and Training',
		)
	user_achievement=models.TextField(
		blank=True,
		null=True,
		verbose_name='My Achievements'
		)
	extra_info=models.TextField(
		blank=True,
		null=True,
		verbose_name='Extra Information',
		default='No Information',
		)

	def __str__(self):
		return f"Hi I'm {self.user_full_name}!\n{self.user_description}"