from google.appengine.ext import ndb


class Comment(ndb.Model):
	"""Comment Table including [ user_name, user_id, content, created, and last_modified ]"""
	user_name = ndb.TextProperty(required = True)
	user_id = ndb.IntegerProperty(required=True)
    content = ndb.TextProperty(required = True)
    created = ndb.DateTimeProperty(auto_now_add = True)
    last_modified = ndb.DateTimeProperty(auto_now=True)
