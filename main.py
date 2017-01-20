import webapp2
from model_post import *
from controller_post import *
from controller_user import *
from model_user import *
from handler import *



#remark : delete welcome.html

app = webapp2.WSGIApplication([('/', Welcome),
                               ('/blog/?', MainPage),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ],
                              debug=True)   #never "deploy" an application with debug_mode=True
