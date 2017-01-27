from handler import *
from model_post import *
from model_comment import *
from google.appengine.ext import ndb


class CommentEdit(BlogHandler):

    def get(self, post_id, comment_user_id, comment_post_id):
                    # 3 args for routes set

        if self.user and self.user.key.id() == int(comment_user_id):
            postkey = ndb.Key('Post', int(post_id), parent=blog_key())
            key = ndb.Key('Comment', int(comment_post_id), parent=postkey)
            comm = key.get()
            self.render('edit_comment.html',
                        comment=comm.comment,
                        user_name=comm.user_name,
                        created=comm.created,
                        post_id=post_id)
                        #  html variable=database.attribute
    	elif not self.user:
            self.redirect('/login')

        else:
            self.write('You are NOT the Author!')

    def post(self, post_id, comment_user_id, comment_post_id):

        postkey = ndb.Key('Post', int(post_id), parent=blog_key())
        key = ndb.Key('Comment', int(comment_post_id), parent=postkey)
        com = key.get()

        if self.user and self.user.key.id() == int(comment_user_id):
            edited_comment = self.request.get('comment')

            if edited_comment:
                com.comment = edited_comment
                com.put()

                self.redirect('/%s' % str(post_id))
            else:
                error = "No Empty, please!"
                self.render("edit_comment.html",
                            comment=edited_comment,
                            error=error)
        else:
            self.write("Only Author Can Edit!")
