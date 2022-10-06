from email.headerregistry import Group
from django.contrib import admin

from django.contrib.auth.models import User, Group
# Register your models here.
from .models import Profile, Post

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email', 'password', 'last_login', 'date_joined']
    ordering = ('username',)
    inlines = (ProfileInline,)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post)
# admin.site.register(Profile)