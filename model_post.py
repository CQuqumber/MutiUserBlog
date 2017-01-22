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

    def render(self):
        key = ndb.Key('User', int(self.user_id), parent=user_key())  #db.Key.from_path() => ndb.Key()
        user = key.get()

        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self, current_user_id=current_user_id, author=name)



class Comment(ndb.Model):
    """Table for Comment"""
    com_post_id = ndb.IntegerProperty(required = True)
    com_author = ndb.StructuredProperty(User)
    com_content = ndb.StringProperty(required = True)
    com_created = ndb.DateTimeProperty(auto_now_add = True)



class Like(ndb.Model):
    """Table for Like"""
    like_post_id = ndb.IntegerProperty(required = True)
    like_com_id = ndb.IntegerProperty(required = True)
    #author = ndb.StringProperty(required = True)
               #ReferenceProperty(reference_class=None, verbose_name=None, collection_name=None, ...)



