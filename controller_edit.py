from handler import *
from model_post import *
from google.appengine.ext import ndb


class Edit(BlogHandler):
    def get(self, post_id):
        key = ndb.Key('Post', int(post_id), parent=blog_key())
        post = key.get()

        if self.user and self.user.key.id() == post.user_id:
            self.render('edit.html',
                        subject=post.subject,
                        content=post.content)

    	elif not self.user:
            self.redirect('/login')

        else:
            self.write('You are NOT the author!')

    def post(self,post_id):
        key = ndb.Key('Post', int(post_id), parent=blog_key())
        post = key.get()

        if not self.user:
            return self.redirect('/login')

        if self.user and self.user.key.id() == post.user_id:
            subject = self.request.get('subject')
            content = self.request.get('content')

            if subject and content:

                post.subject = subject
                post.content = content

                post.put()

                self.redirect('/%s' % str(post_id))
            else:
                error = "subject and content, please!"
                self.render("newpost.html",
                            subject=subject,
                            content=content,
                            error=error)
        else:
            self.write("You are not author!")
