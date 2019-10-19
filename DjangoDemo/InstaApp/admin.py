from django.contrib import admin

from InstaApp.models import Post, InstaUser

# Register your models here.
admin.site.register(Post)
#在admin这个app里面注册Post这个model
admin.site.register(InstaUser)
