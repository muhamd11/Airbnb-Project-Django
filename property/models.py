from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Class Property
class Property(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place', related_name='property_place' ,on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='property_category' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug': self.slug})

    
# Class PropertyImages 
class PropertyImages(models.Model):
    property  = models.ForeignKey(Property, related_name='property_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')  
    
    def __str__(self):
        return str(self.property)



# Class Place
class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')
    
    def __str__(self):
        return self.name



# Class Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name        



# Class PropertyReview
class PropertyReview(models.Model):
    author = models.ForeignKey(User, related_name='review_author' ,on_delete=models.CASCADE)
    porperty = models.ForeignKey(Property, related_name='review_property' ,on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.porperty)


    
COUNT = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)    
class PorpertyBook(models.Model):
    porperty = models.ForeignKey(Property, related_name='book_property' ,on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='book_user' ,on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.CharField(max_length=2, choices=COUNT)
    children = models.CharField(max_length=2, choices=COUNT)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.porperty)