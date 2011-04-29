from django.db import models
from django.utils.hashcompat import md5_constructor
from django.contrib.auth.models import User
import urllib


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
    
    
    def get_absolute_url(self):
        return "/user/%d" % self.user.pk
    
    def get_gravatar(self, size=80, default='wavatar'):
        """ Get's a Gravatar for a email address.
        From: https://github.com/bread-and-pepper/django-userena
    
        :param size:
            The size in pixels of one side of the Gravatar's square image.
            Optional, if not supplied will default to ``80``.
    
        :param default:
            Defines what should be displayed if no image is found for this user.
            Optional argument which defaults to ``identicon``. The argument can be
            a URI to an image or one of the following options:
    
                ``404``
                    Do not load any image if none is associated with the email
                    hash, instead return an HTTP 404 (File Not Found) response.
    
                ``mm``
                    Mystery-man, a simple, cartoon-style silhouetted outline of a
                    person (does not vary by email hash).
    
                ``identicon``
                    A geometric pattern based on an email hash.
    
                ``monsterid``
                    A generated 'monster' with different colors, faces, etc.
    
                ``wavatar``
                    Generated faces with differing features and backgrounds
    
        :return: The URI pointing to the Gravatar.
    
        """
        base_url = 'http://www.gravatar.com/avatar/'
    
        gravatar_url = '%(base_url)s%(gravatar_id)s?' % \
                {'base_url': base_url,
                 'gravatar_id': md5_constructor(self.user.email.lower()).hexdigest()}
    
        gravatar_url += urllib.urlencode({'s': str(size),
                                          'd': default})
        return gravatar_url

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])