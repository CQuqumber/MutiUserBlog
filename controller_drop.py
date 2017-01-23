from handler import *
from model_post import *


from google.appengine.ext import ndb

class DropPost(BlogHandler):
    def get(self, post_id):

        key = ndb.Key('Post', int(post_id), parent=blog_key())
        post = key.get()

        if self.user and self.user.key.id() == post.user_id:
            key = ndb.Key('Post', int(post_id), parent=blog_key())
            post = key.get()
            key.delete()

            self.redirect('/')

        elif not self.user:
            self.redirect('/login')

        else:
            error = "This is not your post!"
            self.render('post.html',post=post, error=error)