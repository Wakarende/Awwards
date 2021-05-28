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
  return render(request, "create_profile.html", {"form": form})
# @login_required(login_url="/accounts/login/")

def home(request):
  return render(request, 'home.html')

