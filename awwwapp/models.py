from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
  user=models.OneToOneField(User, on_delete = models.CASCADE)
  image=CloudinaryField('Profile Picture')
  bio =  models.TextField()
  location = models.CharField(max_length = 40)
  email = models.EmailField()
  link = models.URLField()

  def __str__(self):
    return self.user.username

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete() 

  def edit_bio(self, new_bio):
    self.bio = new_bio
    self.save()

class Project(models.Model):
  name=models.CharField(max_length = 30)
  proj_img=CloudinaryField('Project screenshot')
  desc=models.TextField()
  link = models.URLField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  post_date = models.DateTimeField(auto_now_add=True, null = True)

  def __str__(self):
    return self.name

  def save_project(self):
    self.save()

  def delete_project(self):
    self.delete()

  @classmethod
  def display_all_projects(cls):
    return cls.objects.all()

  @classmethod 
  def search_project(cls,name):
    return Project.objects.filter(name__icontains = name)

  @classmethod
  def get_user_projects(cls,profile):
    return cls.objects.filter(profile=profile)

  class Meta:
    ordering = ['-post_date']