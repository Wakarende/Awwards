from rest_framework import serializers
from .models import Project,Profile,User

class ProjectSerializer(serializers.ModelSerializer):
  class Meta :
    model = Project
    fields = ('name', 'description','screenshot', 'link', 'profile', 'post_date', 'average_design', 'average_content', 'average_score', 'average_usability')

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('user', 'bio', 'profile_pic', 'email','location', 'link')

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  projects = ProjectSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ['id', 'url', 'username', 'profile', 'projects']
