from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Extends the User model and adds some 
    extra info about each member.
    """
    user = models.ForeignKey(User, unique=True)
    company = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    website = models.URLField(verify_exists=False, max_length=200, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    facebook = models.URLField(verify_exists=False, max_length=200, blank=True)
    linkedin = models.URLField(verify_exists=False, max_length=200, blank=True)
    forrst = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    delicious = models.CharField(max_length=50, blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])