from django.contrib import admin
from .models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'get_tags_list', 'created_at', 'author', 'description', 'category')
    list_filter = ('author', 'category')
    search_fields = ('title', 'description', 'author__username', 'category__name')
    ordering = ('-created_at',)

    def get_tags_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())
    get_tags_list.short_description = 'Tags' # rename this column in admin
    
    
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)    