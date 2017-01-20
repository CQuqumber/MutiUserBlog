import webapp2
from model_post import *
from controller import *
from model_user import *
from handler import *


class MainPage(BlogHandler):
    def get(self):
        self.render('base.html')

#remark : delete welcome.html

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ],
                              debug=True)   #never "deploy" an application with debug_mode=True
