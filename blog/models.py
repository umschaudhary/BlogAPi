from django.db import models


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User')
    slug = models.SlugField(max_length=120, unique=True)
    title = models.CharField(max_length=120)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
