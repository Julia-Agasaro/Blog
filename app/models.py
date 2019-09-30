from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Quotes:
  '''
  Quotes class to define Quote Objects
  '''
  def __init__(self,id,author,quote,permalink):
      self.id =id
      self.author = author
      self.quote = quote
      self.permalink = "http://quotes.stormconsultancy.co.uk/quotes/31"
  def hello(self):
        self.s = requests.Session()
        self.s.headers.update()
        return True
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Blog(db.Model):
    '''
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    comment = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')
    date_posted = db.Column(db.DateTime)
    
    
    
    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.order_by(blog_id=id).desc().all()
        return blogs
    def __repr__(self):
        return f'Blog {self.description}'

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.Text)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    

    
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"
class Subscription(db.Model):
   __tablename__ = 'subscribers'
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(100), unique=True)
   name = db.Column(db.String(100))
   def __repr__(self):
       return f'User {self.name}'
