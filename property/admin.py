from django.contrib import admin
from .models import Property, PropertyReview, PropertyImages, Place, Category, PorpertyBook
# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'place', 'category', 'created_at', 'slug')
    list_filter = ('place', 'category')
    search_fields = ('name', 'description', 'place__name', 'category__name')
    ordering = ('-created_at',)
    
@admin.register(PropertyReview)
class PropertyReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'porperty', 'rate', 'feedback', 'created_at')
    list_filter = ('porperty',)
    search_fields = ('author__username', 'porperty__name')
    ordering = ('-created_at',)
    
@admin.register(PropertyImages)
class PropertyImagesAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')
    list_filter = ('property',)
    search_fields = ('property__name',)
    ordering = ('-property__created_at',)
    
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(PorpertyBook)
class PorpertyBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'porperty', 'date_from', 'date_to', 'guest', 'children', 'created_at')
    list_filter = ('porperty',)
    search_fields = ('user__username', 'porperty__name')
    ordering = ('-created_at',)
    
    
    
    