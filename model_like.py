from google.appengine.ext import ndb


class Like(ndb.Model):
    """Table for Like"""
    like_post_id = ndb.IntegerProperty(required = True)
    like_com_id = ndb.IntegerProperty(required = True)
    #author = ndb.StringProperty(required = True)
               #ReferenceProperty(reference_class=None, verbose_name=None, collection_name=None, ...)

