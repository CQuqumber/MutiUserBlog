import webapp2

from model_post import *
from model_user import *
from model_comment import *
from model_like import *

from controller_post import *
from controller_user import *
from controller_edit import *
from handler import *




                              # Route
app = webapp2.WSGIApplication([('/', MainPage),  # welcome.html extrend base.html
                               ('/signup', Signup),   #signup-form.html
                               ('/login', Login),     #login-form.html
                               ('/logout', Logout),   #index.html
                               ('/newpost', NewPost),  #newpost.html
                               ('/([0-9]+)', PostPage),  #permalink.html
                               ('/([0-9]+)/like',Like),
                               ('/([0-9]+)/edit', Edit),   #edit.html
                               ('/([0-9]+)/delete', DropPost)
                               ],
                              debug=True)   #never "deploy" an application with debug_mode=True
