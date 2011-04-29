from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template

from dddm.session.models import Session, Slot
from dddm.fav.models import Fav

register = template.Library()

class get_favs(Tag):
    """
    Fetches all sessions
    
    Usage:
    {% get_favs for user as favs %}
    {% for f in favs %}
    """
    
    options = Options(
        'for',
        Argument('user'),
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, user, varname):
        favs = []
        
        for slot in Slot.objects.all():
            qs = Fav.objects.filter(user=user).filter(session__slot=slot).order_by("session__room")
            sessions = []
            
            if qs:
                for f in qs:
                    speaker = "%s %s" % (f.session.speaker.first_name, f.session.speaker.last_name) if f.session.speaker else None
                    sessions.append({"speaker": speaker,
                                     "title": f.session.title,
                                     "url": f.session.get_absolute_url(),
                                     "excerpt": f.session.excerpt,
                                     "room": f.session.room,
                                     "is_break": f.session.is_break,
                                     "id": f.session.id})
            
            if len(sessions) > 0:
                favs.append({"start": slot.start, "end": slot.end, "sessions": sessions})
        
        if varname:
            context[varname] = favs
            return ''
        else:
            return favs

register.tag(get_favs)