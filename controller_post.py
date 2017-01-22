from handler import *
from model_post import *


def blog_key(name = 'default'):
    return ndb.Key('blogs', name)	#db.Key.from_path() => ndb.Key()


class MainPage(BlogHandler):
    def get(self):
    	posts = Post.gql("ORDER BY created DESC limit 10")
        if posts:
        	self.render('index.html', posts = posts)


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
            		content = content,
            		user_id = self.user.key.id())
            p.put()
            self.redirect('/blog/%s' % str(p.key.id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", 
            			subject=subject, 
            			content=content, 
            			error=error)	#newpost.html variables has subject, content, and error



class PostPage(BlogHandler):
    def get(self, post_id):
        key = ndb.Key('Post', int(post_id), parent=blog_key())	#db.Key.from_path() => ndb.Key()
        post = key.get()	#db.get(key) => NDB  key.get()

        if not post:
            self.error(404)
            return
        self.render("post.html",
        			post = post)	#post.html variable must be 'post'


class DropPost(BlogHandler):
	"""Remove Post"""
	def get(self, post_id):
		if self.user and self.user.key.id() == int:
			key = ndb.Key('Post', int(post_id), parent=blog_key())	#db.Key.from_path() => ndb.Key()
        	post = key.get()
        	post.delete()
        	self.redirect('/blog')


'''
if self.request.get("delete"):
                # check if the user is the author of this post
                if post.user.key().id() == User.by_name(self.user.name).key().id():
                    # delete the post and redirect to the main page
                    db.delete(key)
                    time.sleep(0.1)
                    self.redirect('/')
                    '''