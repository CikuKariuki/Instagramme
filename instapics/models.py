from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    profile_photo = models.ImageField(upload_to='profiles/')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        

    def save_profile(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    # @classmethod
    # def search_by_username(cls,search_term):
    #     profile = cls.objects.filter(username__icontains=search_term)
    #     return profile


class Posts(models.Model):
    images = models.ImageField(upload_to='posts/')
    caption = models.TextField()
    profile = models.ForeignKey(Profile)
    tag = models.ManyToManyField(tag)

    # def save_posts(self):
    #     self.save()

    # @classmethod
    # def search_by_profile(cls,search_term):
    #     posts = cls.objects.filter(profile__icontains=search_term)
    #     return posts

    @classmethod
    def search_by_tag(cls, search_term):
        posts = cls.objects.filter(tag__tag__icontains=search_term)
        return posts


class Comments(models.Model):
    comments = models.CharField(max_length=100)
    user_id = models.ForeignKey(
        User, blank=True, on_delete=models.CASCADE, related_name='user', null=True)
    posts_id = models.ForeignKey(
        Posts, blank=True, on_delete=models.CASCADE, related_name='posts_comments', null=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comments
from django.contrib.auth.decorators import login_required
