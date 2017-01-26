from google.appengine.ext import ndb


class Like(ndb.Model):
	post_id = ndb.IntegerProperty(required = True)
	user_id = ndb.IntegerProperty(required = True)
	#created = ndb.DateTimeProperty(auto_now_add = True)
