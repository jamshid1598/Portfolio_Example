from django.shortcuts import render, redirect
from .models import Resume
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .NewUser import NewUserForm
from django.contrib import messages

# Create your views here.

def homepage(request):
	return render(
		request,
		'main/home.html',
		context={
				'info': Resume.objects.all
			}
		)


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "New account created: {}".format(username))
			login(request, user)
			messages.info(request, "You are now loged in {}".format(username))
			return redirect('main:homepage')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

			return render(
				request,
				"main/register.html",
				context={
					'form' : form
				}
			)

	form = NewUserForm
	return render(
		request,
		"main/register.html",
		context={
			'form' : form
		}
	)