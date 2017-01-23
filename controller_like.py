from handler import *
from model_post import *
from google.appengine.ext import ndb


class Like(BlogHandler):
    def get(self, post_id):
        key = ndb.Key('Post', int(post_id), parent=blog_key())
        post = key.get()

        if self.user and self.user.key.id() == post.user_id:
            error = "CANT like your own post"
            self.render('index.html', error = error)

    	elif not self.user:
			self.redirect('/login')

    	else:      #check others already like or not
            user_id = self.user.key.id()
            post_id = post.key.id()

            like = Like.query(user_id =='user_id', 
                            post_id == 'post_id')

            if like:    #already like
                self.redirect('/blog/%s' % str(post.key.id()))

            else:   # non like
                like = Like(parent=key,
                            user_id=self.user.key.id(),
                            post_id=post.key.id())

                post.likes += 1

                like.put()
                post.put()

                self.redirect('/blog/%s' % str(post.key.id()))

