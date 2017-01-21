import random
import hashlib
from string import letters
from google.appengine.ext import ndb


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

def users_key(group = 'default'):
    return ndb.Key('users', group)   #db.Key.from_path => ndb.Key

def blog_key(name = 'default'):
    return ndb.Key('blogs', name)

class User(ndb.Model):
    name = ndb.StringProperty(required = True)
    pw_hash = ndb.StringProperty(required = True)
    email = ndb.StringProperty()

    @classmethod
    def get_user_by_id(cls, userid):    #at { @ } : decorators >> User.by_id
        return User.get_by_id(userid)

    @classmethod
    def get_user_by_name(cls, name):    #at { @ } : decorators >> User.by_name
        user = User.query(User.name == name).fetch(1)
        for u in user:
            return u

    @classmethod
    def get_user_by_name_pw(cls, name, pw, email = None): #at { @ } : decorators >> User.register
        pw_hash = make_pw_hash(name, pw)
        return User(name = name,
                    pw_hash = pw_hash,
                    email = email)
    @classmethod
    def get_user_id(cls, user):
        return user.key.id()

    @classmethod
    def login(cls, name, pw):   #at { @ } : decorators >> User.login
        u = cls.get_user_by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u
