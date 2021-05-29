from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile,Project
import datetime as dt 
from .forms import CreateProfileForm,ProjectForm

# Create your views here.

@login_required(login_url="/accounts/login/")
def create_profile(request):
  title="Create Profile"
  current_user = request.user
  if request.method == "POST":
    form = CreateProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      profile.save()

    return HttpResponseRedirect("/")

  else:
    form = CreateProfileForm()
  return render(request, "profile/create_profile.html", {"form": form,"title": title})
# @login_required(login_url="/accounts/login/")

def home(request):

  return render(request, 'home.html')


def profile(request, profile_id):
  title="Profile"
  try:
    user=User.objects.get(pk=profile_id)
    profile=Profile.objects.get(user=user)
    title=profile.user.username
    projects = Project.get_user_projects(profile.id)
    project_count=projects.count()
  
  except Profile.DoesNotExist:
    raise Http404()
  return render(request, "profile/profile.html", {"profile":profile, "projects":projects, "count":project_count, "title":title})