#import os
from handler import *

from google.appengine.ext import db

##### blog stuff


class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    #author = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    #user = db.UserProperty(required = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)



class Like(db.Model):
    """docstring for Like"""
    like_post = db.ReferenceProperty(Post, required = True)
    like_author = db.ReferenceProperty(User, required = True)
    like_create = db.DateTimeProperty(auto_now_add = True)
               #ReferenceProperty(reference_class=None, verbose_name=None, collection_name=None, ...)
    @classmethod
    def clickLike(cls, post_id):
        c = Like(like_post = post_id,
                    like_author = like_author)
        c.put()
        return c.key.id_or_name()


