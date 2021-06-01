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


class TestProject(TestCase):
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

  def test_display_all_projects(self):
    project=Project.display_all_projects()
    self.assertTrue(len(project)>0)

  def test_search_project(self):
    project=Project.search_project('test')
    self.assertEqual(len(project),1)


class TestRating(TestCase):
  def setUp(self):
    self.user = User(username="joy", email="joy@gmail.com", password="1234")
    self.profile = Profile(bio="Test profile", user=self.user)
    self.project = Project(id=1,name="test", proj_img="img.png",desc="description", link="link", profile=self.profile  )
    self.rating = Rate(id=1, design=5, usability=7, content=9, user=self.user, project=self.project)

    self.user.save()
    self.profile.save()
    self.project.save()
    self.rating.save()


  def tearDown(self):
    Profile.objects.all().delete()
    Project.objects.all().delete()
    Rate.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.rating, Rate))

  def test_save_rating(self):
    rating=Rate.objects.all()
    self.assertTrue(len(rating)>0)

