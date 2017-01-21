#import os
from handler import *

from google.appengine.ext import ndb

##### blog stuff


class Post(ndb.Model):
    subject = ndb.StringProperty(required = True)
    content = ndb.TextProperty(required = True)
    #author = db.StringProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    last_modified = ndb.DateTimeProperty(auto_now = True)
    #user = db.UserProperty(required = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)



class Like(ndb.Model):
    """docstring for Like"""
    like_post = ndb.KeyProperty(Post, required = True)
    like_author = ndb.KeyProperty(User, required = True)
               #ReferenceProperty(reference_class=None, verbose_name=None, collection_name=None, ...)
    @classmethod
    def clickLike(cls, post_id):
        c = Like(like_post = str(post_id),
                    like_author = str(like_author))
        c.put()
        return c.key.id()


