from django.db import models
from datetime import datetime
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User

import string
from dddm.lib.summarize import SimpleSummarizer


class Slot(models.Model):
    """
    The available time slots
    """
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        ordering = ["start"]

    def __unicode__(self):
        return "%s - %s" % (self.start, self.end)


class Session(models.Model):
    """
    The juicy bit. 
    """
    speaker = models.ForeignKey(User, blank=True, null=True)
    slot = models.ForeignKey(Slot)
    title = models.CharField(max_length=100)
    slug = AutoSlugField('slug', max_length=50, unique=True, populate_from=('title',))
    excerpt = models.CharField(max_length=200, blank=True,
                               help_text="""Optional. If no excerpt is entered one will be
                                            generated from the description.""")
    description = models.TextField(blank=True)
    room = models.CharField(max_length=1,
                            choices=[(string.letters[x],string.letters[x]) for x in range(0,5)],
                            blank=True)
    is_break = models.BooleanField(default=False)

    class Meta:
        ordering = ["slot", "room"]
    
    def get_absolute_url(self):
        return '/session/%s' % self.slug

    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
        Generate an excerpt automatically if one does not exist.
        """

        if self.description and not self.excerpt:
            ss = SimpleSummarizer()
            self.excerpt = ss.summarize(self.description, 1)[:200]

        super(Session, self).save(*args, **kwargs)
