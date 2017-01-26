from google.appengine.ext import ndb

class Comment(ndb.Model):
	"""docstring for Comment"""
	user_name = ndb.StringProperty(required=True)
	user_id = ndb.IntegerProperty(required=True)
	comment = ndb.TextProperty(required=True)
	created = ndb.DateTimeProperty(auto_now_add=True)
	last_modified = ndb.DateTimeProperty(auto_now=True)

