from handler import *

from google.appengine.ext import ndb



class Post(ndb.Model):
    '''Table for Post'''
    author = ndb.StructuredProperty(User)
    subject = ndb.StringProperty(required = True)
    content = ndb.TextProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    likes = ndb.IntegerProperty(default=0)
    last_modified = ndb.DateTimeProperty(auto_now = True)
'''
    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)
'''


class Comment(ndb.Model):
    """Table for Comment"""
    post_id = ndb.IntegerProperty(required = True)
    author = ndb.StructuredProperty(User)
    content = ndb.StringProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)



class Like(ndb.Model):
    """Table for Like"""
    post_id = ndb.IntegerProperty(required = True)
    author = ndb.StringProperty(required = True)
               #ReferenceProperty(reference_class=None, verbose_name=None, collection_name=None, ...)



