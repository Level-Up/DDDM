# Developer Day Scotland

> This still a work in progress. There **will** be bugs.

Mobile version of the [DDD Scotland site](http://www.developerdeveloperdeveloper.com/scotland2011/). 
Primary aimed at the conference attendees it uses jQuery Mobile so it plays nicely with handhelds.

# Primary features

* Agenda/Session listing with search
* Session, Speaker, Attendee profiles
* Favourites for sessions (with clash checking)
* View who is attending what _(if they have favourited it)_

# Dependencies

*I think this is them all, really should have used virtualenv on this one...*

    South==0.7.2
    django-cms==2.1.0.rc2
    django-admin-tools==0.3.0
    django-lazysignup==0.7.0
    docutils==0.7
    nltk==2.0b9

# Installation

1. Install the dependencies
2. Clone this repo
3. Copy localsettings.example.py to localsettings.py and complete it
4. Run `python manage.py syncdb --all`
5. Run `python manage.py migrate --fake`
