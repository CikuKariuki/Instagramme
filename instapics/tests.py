from django.test import TestCase
from .models import Profile,Posts,tag

class ProfileTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Profile(first_name = 'Wanjiku',last_name='Kariuki',username='ciku_k',email='sheekokariuki@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.wanjiku,Profile))