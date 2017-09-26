from datetime import datetime as dt
import django
django.setup()

from testapp.models import Note
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

user = User(username='you', email="your.mail@your.mail.com")
user.set_password('you')
user.save()

titles = ['thing', 'other thing', 'stuff', 'whatever', 'nothing']
bodies = ['Lots of writing about {title}'.format(title=title) for title in titles]

# Make some data
for i in range(5):
    note = Note(user=user, 
                pub_date=dt.now(),
                title=titles[i],
                body=bodies[i])
    note.save()
