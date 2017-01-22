from handler import *
from model_post import *
from google.appengine.ext import ndb


class Edit(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user_id:
            self.render('editpost.html', 
                        subject=post.subject,
                        content=post.content, 
                        post_id=post_id)

    	elif not self.user:
			self.redirect('/login')

    	else:
			self.write('Do not guess the postid')

    def post(self, post_id):

        if not self.user:
            self.redirect('/login')

        if self.user and self.user.key.id() == post.user_id:
            subject = self.request.get('subject')
            content = self.request.get('content')

            if subject and content:
                key = ndb.Key('Post', int(post_id), parent=blog_key())
                post = key.get()

                post.subject = subject
                post.content = content

                post.put()

                self.redirect('/blog/%s' % str(post.key.id()))
            else:
                error = "subject and content, please!"
                self.render("newpost.html", 
                            subject=subject, 
                            content=content, 
                            error=error)
        else:
            self.write("You are not author!")
