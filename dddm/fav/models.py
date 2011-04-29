from django.db import models
from django.contrib.auth.models import User

from dddm.session.models import Session

class Fav(models.Model):
    """
    Store user's favourite sessions
    """
    user = models.ForeignKey(User)
    session = models.ForeignKey(Session)

    def __unicode__(self):
        return "%s - %s" % (self.user.email, self.session.title)
