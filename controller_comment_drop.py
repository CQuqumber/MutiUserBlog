from handler import *
from model_post import *
from model_comment import *
from google.appengine.ext import ndb


class CommentDrop(BlogHandler):

    def get(self, post_id, comment_user_id, comment_post_id):
                    # 3 args for routes set

        if self.user and self.user.key.id() == int(comment_user_id):
            postkey = ndb.Key('Post', int(post_id), parent=blog_key())
            key = ndb.Key('Comment', int(comment_post_id), parent=postkey)
            comm = key.get()
            key.delete()
            self.redirect('/%s' % str(post_id))

        elif not self.user:
            self.redirect('/login')

        else:
            error = 'You Cant delete others post!'
            self.render('base.html', error=error)
