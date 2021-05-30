from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project,Rate



# Create your tests here.
class TestProfile(TestCase):
  def setUp(self):
    self.user = User(username="joy")
    self.profile0 = Profile(bio="Test profile", user=self.user)
    self.user.save()

    self.profile_test = Profile(
      user=self.user, image="default.jpg", bio="Test profile"
    )


  def test_instance(self):
    self.assertTrue(isinstance(self.profile_test, Profile))


class TestComment(TestCase):
  def setUp(self):
    self.user = User(username="joy", email="joy@gmail.com", password="1234")
    self.profile = Profile(bio="Test profile", user=self.user)
    self.project = Project(name="test", proj_img="img.png",desc="description", link="link", profile=self.profile  )
    self.user.save()
    self.profile.save()
    self.project.save()

    
  def test_instance(self):
    self.assertTrue(isinstance(self.project, Project))

  def test_save_project(self):
    project= Project.objects.all()
    self.assertTrue(len(project) > 0)

  def test_delete_project(self):
    project= Project.objects.all()
    self.assertEqual(len(project), 1)
    self.project.delete_project()
    project1 = Project.objects.all()
    self.assertEqual(len(project1), 0)

  def test_get_user_projects(self):
    project=Project.get_user_projects(self.profile)
    self.assertTrue(len(project)>0)
