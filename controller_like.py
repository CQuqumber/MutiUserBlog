from handler import *
#from model_post import *
#from model_user import User
from model_like import *
from google.appengine.ext import ndb


class LikePost(BlogHandler):
    def get(self, post_id):
        key = ndb.Key('Post', int(post_id), parent=blog_key())
        post = key.get()
        if self.user and self.user.key.id() == post.user_id:
            error = "No Permission to Like Your Post!"
            self.render('base.html', error = error)

    	elif not self.user:
			self.redirect('/login')

    	else:      #For : check others already like or not

            like = Like.query(Like.user_id == self.user.key.id(), 
                                Like.post_id == post.key.id()).fetch()
            #like = Like.all().filter('user_id =', user_id).filter('post_id =', post_id).get()

            if like:    #   For already like
                self.redirect('/')

            else:   # non like
                like = Like(parent=key,
                            user_id=self.user.key.id(),
                            post_id=post.key.id())

                post.likes += 1
                    # likes = post model attribute
                like.put()
                post.put()

                self.redirect('/')

