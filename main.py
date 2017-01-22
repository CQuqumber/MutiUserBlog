import webapp2

from model_post import *
from model_user import *
from model_comment import *
from model_like import *

from controller_post import *
from controller_user import *

from handler import *



#remark : delete welcome.html

app = webapp2.WSGIApplication([('/', Welcome),  #base.html
                               ('/blog/?', MainPage),   #index.html
                               ('/signup', Register),   #signup-for.html
                               ('/login', Login),   #login-form.html
                               ('/logout', Logout), #index.html
                               ('/blog/newpost', NewPost),  #newpost.html
                               ('/blog/([0-9]+)', PostPage),  #permalink.html
                               ('/blog/([0-9]+)/edit', Edit),
                               ('/blog/([0-9]+)/delete/([0-9]+)', DropPost)
                               ],
                              debug=True)   #never "deploy" an application with debug_mode=True
