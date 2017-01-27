from handler import *
from model_post import *
from model_comment import *
from google.appengine.ext import ndb


class MainPage(BlogHandler):
    def get(self):
    	posts = Post.gql("order by created desc")
        #   .fetch() returns a list, get() returns the first result,
        if posts:
            return self.render('front.html', posts=posts)


class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            return self.redirect('/login')

        subject = self.request.get('subject')
        #   retrieve from newpost.html
        content = self.request.get('content')
        author = self.user.name
        if subject and content:
            p = Post(parent=blog_key(), subject=subject,
                content=content, author=author, user_id=self.user.key.id())

            p.put()
            self.redirect('/%s' % str(p.key.id()))
        else:
            error = "subject and content, please!"
            return self.render("newpost.html",
                subject=subject, content=content, error=error)
            #  newpost.html variables has subject, content, and error


class PostPage(BlogHandler):
    def get(self, post_id):
        key = ndb.Key('Post', int(post_id),
        parent=blog_key())

        post = key.get()

        comments = Comment.query(Comment.post_id == post.key.id())\
            .order(-Comment.created).fetch()

        if not post:
            self.error(404)
        else:
            return self.render("post.html",
                post=post, comments=comments)
        #   post.html variable must be 'post' and ' comments'
