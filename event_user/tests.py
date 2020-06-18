from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.db.utils import IntegrityError

# Create your tests here.
class UserTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='tester',
      first_name='Tester',
      last_name='TESTER',
      email = 'tester@email.com',
      password = 'password'
    )
  def test_method(self):
    self.assertIsInstance(self.user, CustomUser)
    self.assertEqual(self.user.email, 'tester@email.com')
    self.assertEqual(self.user.username, 'tester')
    self.assertIsNotNone(self.user.password)

  def test_no_dupe_email(self):

    try:
      user2 = get_user_model().objects.create_user(
      username='nottester',
      first_name='Nottester',
      last_name='NOTTESTER',
      email = 'tester@email.com',
      password = 'notpassword'
      )
    except IntegrityError:
      print('all good')
    else:
      self.fail('not possible')