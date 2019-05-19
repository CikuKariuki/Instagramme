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

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']

class Posts(models.Model):
    # image = models.ImageField(upload_to_posts.html)
    caption = models.TextField()
    profile = models.ForeignKey(Profile)
    tag = models.ManyToManyField(tag)

    