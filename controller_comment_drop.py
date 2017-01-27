from handler import *
from model_post import *

from google.appengine.ext import ndb

'''
class CommentDrop(BlogHandler):
    def get(self, post_id):

        key = ndb.Key('Post', int(post_id), parent=blog_key())
        post = key.get()

        if self.user and self.user.key.id() == post.user_id:
            key = ndb.Key('Post', int(post_id), parent=blog_key())
            post = key.get()
            key.delete()

            self.redirect('/%s' %str(post.key.id()))

        elif not self.user:
            self.redirect('/login')

        else:
            error = "Not Your Comment!"
            self.render('after_comment.html', post=post, error=error)
'''