import webapp2
from post import *
from registration import *
from data import *
from handler import *


class MainPage(BlogHandler):
    def get(self):
        self.render('welcome.html')


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ],
                              debug=True)
