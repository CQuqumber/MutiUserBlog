from handler import *

from google.appengine.ext import ndb



class Post(ndb.Model):
    '''Table for Post'''
    #author = ndb.StructuredProperty(User)
    subject = ndb.StringProperty(required = True)
    content = ndb.TextProperty(required = True)
    user_id = ndb.IntegerProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    likes = ndb.IntegerProperty(default=0)
    last_modified = ndb.DateTimeProperty(auto_now = True)

    def render(self):
        key = ndb.Key('User', int(self.user_id), parent=user_key())  #db.Key.from_path() => ndb.Key()
        user = key.get()

        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self, current_user_id=current_user_id, author=user.name)




