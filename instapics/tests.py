from django.test import TestCase
from .models import Profile,Posts,tag

class ProfileTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Profile(first_name = 'Wanjiku',last_name='Kariuki',username='ciku_k',email='sheekokariuki@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.wanjiku,Profile))

    def test_save(self):
        self.wanjiku.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
   
class PostsTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Posts(caption = 'Wanjiku is amazing')

    def test_instance(self):
        self.assertTrue(isinstance(self.wanjiku,Posts))

    # def test_save(self):
    #     self.wanjiku.save_posts()
    #     postss = Posts.objects.all()
    #     self.assertTrue(len(postss)>0)
    