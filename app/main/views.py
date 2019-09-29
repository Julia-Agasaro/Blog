from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Blog, User,Comment,PhotoProfile
from .forms import BlogForm, CommentForm
from flask.views import View,MethodView
from .. import db,photos
import markdown2


# Views
@main.route('/', methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    blog = Blog.query.all()
    title = 'Home'
    
    

    return render_template('home.html', title = title, blog = blog)
    


@main.route('/blogs/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        user_id = current_user
        new_blog = Blog(user_id =current_user._get_current_object().id, title = title,description=description)
        db.session.add(new_blog)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('blogs.html', title='New Blog',
                           form=form, legend='New Blog')

@main.route('/comment/new/<int:blog_id>', methods = ['GET','POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    blog=Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, blog_id = blog_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', blog_id= blog_id))

    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    return render_template('comments.html', form = form, comment = all_comments, blog= blog )

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    get_blogs = Blog.query.filter_by(user_id = current_user.id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, description = get_blogs)


@main.route('/user/<uname>',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/profile/delete/<int:blog_id>', methods = ['GET', 'POST'])
@login_required
def delete(blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    
    user = current_user
    
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.profile',uname=uname))
    return render_template('profile/profile.html',user =user)


@main.route("/profile/<int:blog_id>/update_blog", methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    form = BlogForm()
    if form.validate_on_submit():
        Blog.title = form.title.data
        Blog.description = form.description.data
        db.session.commit()
        flash('Your blog has been updated!', 'success')
        return redirect(url_for('main.profile',uname=uname))
    elif request.method == 'GET':
        form.title.data = blog.title
        form.description.data = blog.description
    return render_template('blogs.html', title='Update blog',
                           form=form, legend='Update blog')
    