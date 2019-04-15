from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from django.contrib.admin import widgets
from django.utils import timezone


class UserRegistrationForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'email', 'password1', 'password2']:
			self.fields[fieldname].label = None

	username = forms.CharField(
		required=True,
		label='Username',
		max_length=30,
	)
	email = forms.CharField(
		required=True,
		label='Email',
		max_length=100,
	)
	password1 = forms.CharField(
		required=True,
		label='Password',
		max_length=100,
	)
	password2 = forms.CharField(
		required=True,
		label='Repeat password',
		max_length=100,
	)

	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
		raise forms.ValidationError('Passwords do not match.')