from handler import *
from model_post import *
from model_user import *
from model_comment import *

from google.appengine.ext import ndb

class CommentPost(BlogHandler):

    def get(self,post_id,user_id):      #route set /([0-9]+)/comment/([0-9]+)
        if self.user:
            self.render('comment.html')
        else:
            self.redirect('/login')

    def post(self, post_id, user_id):

        if not self.user:
            return

        key = ndb.Key('Post',int(post_id), parent=blog_key())
        #post = key.get()
        comment = self.request.get('comment')
        user_name = self.user.name
        c = Comment(parent=key, user_id=int(user_id), comment=comment, user_name=user_name)
        c.put()
        self.redirect('/' + post_id)
'''
        if not comment:
            error = 'No Empty Comment, Plz!'
            self.render('comment.html',error=error)

        else:
            c = Comment(parent=key, 
                        user_id=int(user_id), 
                        comment=comment, 
                        user_name=user_name)
            c.put()

            self.redirect('/%s' %str(post.key.id()))

'''
