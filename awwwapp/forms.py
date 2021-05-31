from .models import Project,Profile,Rate
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

class RateForm(ModelForm):
  class Meta:
    model=Rate
    fields=['design','usability','content']
    
class UpdateProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['location',' image','bio','email']

