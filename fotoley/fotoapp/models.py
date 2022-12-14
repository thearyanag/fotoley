from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False , blank=True)
    def __str__(self):
        return self.user.username

# signal to create profile when user is created
from django.db.models.signals import post_save
def create_profile(sender, instance ,created ,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(user_profile)
        user_profile.save()
        
post_save.connect(create_profile, sender=User)

class Post(models.Model):
    user = models.ForeignKey(User,related_name="post", on_delete=models.DO_NOTHING)
    media = models.FileField(upload_to='media/' , blank=True)
    caption = models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (
            f"{self.user} "
            f"({self.date:%Y-%m-%d %H:%M}): "
            f"{self.caption[:30]}..."
        )

