from .models import Project,Profile,Vote
from django.forms import ModelForm
from django import forms

class CreateProfileForm(ModelForm):
  class Meta:
    model=Profile
    exclude =['user']

class ProjectForm(ModelForm):
  class Meta:
    model=Project
    exclude=['profile', 'post_date',]

    