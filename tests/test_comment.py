import unittest
from app.models import Pitch, User, Comment
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch_content = "pitch", pitch_category='fashion')
        self.new_comment = Comment(comment_content = "true", pitch=self.new_pitch)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"true")
        self.assertEquals(self.new_comment.pitch,self.new_pitch, 'pitch ')