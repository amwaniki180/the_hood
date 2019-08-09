from django.contrib import admin
from .models import Post,Project,Profile,Business
# Register your models here.

admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Project)
admin.site.register(Profile)
