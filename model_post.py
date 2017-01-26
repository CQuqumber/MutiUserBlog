from handler import *

from google.appengine.ext import ndb



class Post(ndb.Model):
    '''Table for Post'''
    author = ndb.StringProperty(required = True)
    subject = ndb.StringProperty(required = True)
    content = ndb.TextProperty(required = True)
    user_id = ndb.IntegerProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    likes = ndb.IntegerProperty(required=True,default=0)
    last_modified = ndb.DateTimeProperty(auto_now = True)

    def render(self,current_user_id):
        key = ndb.Key('User', int(self.user_id), parent=users_key())  #db.Key.from_path() => ndb.Key()
        user = key.get()

        self._render_text = self.content.replace('\n', '<br>')
        #return render_str("post.html")
        return render_str("index.html", p = self, current_user_id=current_user_id, author=user.name)



