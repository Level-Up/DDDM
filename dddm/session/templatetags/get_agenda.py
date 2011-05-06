from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template

from dddm.session.models import Session, Slot

register = template.Library()

class get_agenda(Tag):
    """
    Fetches all sessions
    
    Usage:
    {% get_agenda as agenda %}
    {% for session in agenda %}
    """
    
    options = Options(
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, varname):
        agenda = []
        
        for slot in Slot.objects.all():
            qs = Session.objects.filter(slot=slot).order_by("room")
            sessions = []
            
            if qs:
                for s in qs:
                    speaker = "%s %s" % (s.speaker.first_name, s.speaker.last_name) if s.speaker else None
                    speaker_id = s.speaker.pk if s.speaker else None
                    sessions.append({"speaker": speaker,
                                     "speaker_id": speaker_id,
                                     "title": s.title,
                                     "url": s.get_absolute_url(),
                                     "excerpt": s.excerpt,
                                     "room": s.room,
                                     "is_break": s.is_break})
            
            agenda.append({"start": slot.start, "end": slot.end, "sessions": sessions})
        
        if varname:
            context[varname] = agenda
            return ''
        else:
            return agenda

register.tag(get_agenda)