# Register your models here.
from django.contrib import admin
from .models import category, post, PostImage
# Register your models here.

admin.site.register(category)
admin.site.site_header = 'ESAM JUNIOR ENTREPRISE'

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass