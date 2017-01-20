#import os
from handler import *

from google.appengine.ext import db

##### blog stuff

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    #user = db.UserProperty(required = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)



class Like(db.Model):
    """docstring for Like"""
    article = db.ReferenceProperty(required = True)
    bloger = db.ReferenceProperty(required = True)

    @classmethod
    def by_article_id(cls, article_id):
        pass

    @classmethod
    def permit_like(cls, article_id, user_id):
        pass