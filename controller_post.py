from handler import *
from model_post import *

def blog_key(name = 'default'):
    return ndb.Key('blogs', name)	#db.Key.from_path() => ndb.Key()

class MainPage(BlogHandler):
    def get(self):
    	posts = Post.query()
        if posts:
        	self.render('index.html', posts = posts)

class PostPage(BlogHandler):
    def get(self, post_id):
        key = ndb.Key('Post', int(post_id), parent=blog_key())	#db.Key.from_path() => ndb.Key()
        post = key.get()	#db.get(key); NDB  key.get()

        if not post:
            self.error(404)
            return
        self.render("permalink.html",
        			post = post)

class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(),
            			subject = subject,
            			content = content)
            p.put()
            self.redirect('/blog/%s' % str(p.key.id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)

