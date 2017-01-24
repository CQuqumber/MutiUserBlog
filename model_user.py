import random
import hashlib

from string import letters
from google.appengine.ext import ndb


def users_key(group = 'default'):
    return ndb.Key('users', group)   #db.Key.from_path => ndb.Key


#   validate psw
def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in xrange(length))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)




class User(ndb.Model):
    name = ndb.StringProperty(required = True)
    pw_hash = ndb.StringProperty(required = True)
    email = ndb.StringProperty()

    @classmethod
    def get_user_id(cls, user):
        return user.key.id()


    @classmethod
    def register(cls, name, pw, email = None):  #at { @ } : decorators >> User.register
        pw_hash = make_pw_hash(name, pw)
        return User(parent = users_key(),
                    name = name,
                    pw_hash = pw_hash,
                    email = email)

    @classmethod
    def login(cls, name, pw):   #at { @ } : decorators >> User.login
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u

    @classmethod
    def by_id(cls, userid):    #at { @ } : decorators >> User.by_id
        return User.get_by_id(userid, parent=users_key())
                #get_by_id(id, parent=None, app=None, namespace=None, **ctx_options)
                #shorthand for Key(cls, id).get()

    @classmethod
    def by_name(cls, name):    #at { @ } : decorators >> User.by_name
        user = User.query(User.name == name).get()
        for u in user:                      #get() similiar fetch(1) always returns a list
            return u
