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
      user=self.user, profile_pic="default.jpg", bio="Test profile"
    )


  def test_instance(self):
    self.assertTrue(isinstance(self.profile_test, Profile))

