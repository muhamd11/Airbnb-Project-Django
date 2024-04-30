from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post_images/")
    tags = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='post_author' ,on_delete=models.CASCADE)
    description = models.TextField(max_length=15000)
    category = models.ForeignKey('Category', related_name='post_category',on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name    
    
