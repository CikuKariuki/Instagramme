from django.db import models

class tag(models.Model):
    tag = models.CharField(max_length = 100)

    def __str__(self):
        return self.tag

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 15,blank = True)
    
    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']

    def save_profile(self):
        self.save()

    # @classmethod
    # def search_by_username(cls,search_term):
    #     profile = cls.objects.filter(username__icontains=search_term)
    #     return profile

class Posts(models.Model):
    # images = models.ImageField(upload_to_posts.html)
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
    def search_by_tag(cls,search_term):
        posts = cls.objects.filter(tag__icontains=search_term)
        return posts