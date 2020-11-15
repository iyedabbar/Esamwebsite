from django.contrib import admin
from .models import event, PostImage



class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(event)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = event

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass