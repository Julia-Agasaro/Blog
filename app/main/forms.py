from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
	
class PitchForm(FlaskForm):
	title = StringField('Pitch Title', validators=[Required()])
	description = TextAreaField("What would you like to pitch ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('religious pitch','Religious pitch'), ('interviewpitch','Interview pitch'),('pickuplines','Pickuplines'),('fashion pitch','Fashion pitch')],validators=[Required()])
	submit = SubmitField('Submit')


class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class DownvoteForm(FlaskForm):
	submit = SubmitField()