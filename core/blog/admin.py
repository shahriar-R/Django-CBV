from django.contrib import admin
from .models import Post,Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','status','category','create_date']


admin.site.register(Post)
admin.site.register(Category)