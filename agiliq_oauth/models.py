from django.db import models
from django.forms import ModelForm, Form
from django import forms

class UploadForm(Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	projects_url = forms.CharField(max_length = 255)
	code_url = forms.CharField(max_length = 200)
	resume = forms.FileField()