from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile,Project
import datetime as dt 
from .forms import CreateProfileForm,ProjectForm
from django.http import HttpResponseRedirect, Http404
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

# Display projects 
def home(request):
  title="awwwards"
  date=dt.date.today()
  projects =Project.display_all_projects()
  return render(request, 'home.html', {"date":date, "title":title, "projects":projects})


# Display Profile 
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


# Add Project 
def create_project(request):
  title="Add Project"
  if request.method == "POST":
    form = ProjectForm(request.POST, request.FILES)
    current_user=request.user
    try:
      profile = Profile.objects.get(user=current_user)
    except Profile.DoesNotExist:
      raise Http404()
    if form.is_valid():
      project = form.save(commit=False)
      project.profile = profile
      project.save()
    return redirect('home')
  else:
    form=ProjectForm()
  return render(request, 'projects/create_project.html',{"form": form, "title":title})

# Display project 
def disp_project(request,project_id):
  project=Project.objects.get(pk=project_id)
  title=project.name.title()
  
  return render(request, 'projects/project.html', {"title": title, "project": project})


#Search Project 
def search_project(request):
  if request.method == 'GET':
    title="Search"
    search_results=Project.objects.filter(name__icontains = name).all()
    print(search_results)

    return render(request. 'search_results.html',)

  else:
    message="You haven't searched for any project"
  
  return render(request, 'search_results.html', {"message":message})
