import re
import json
import datetime

from app         import db, utilities
from flask_login import UserMixin

class VCUser(UserMixin, db.Model):
    '''
    Used to create, edit, store, and 
    retrieve information about users.
    '''
    __tablename__ = "VCUsers"
    #Account information (username, email, password, etc)
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    salt = db.Column(db.String(64), index=True, unique=True)

    #Store information about users (problems posted, points, etc)
    problem_posts = db.Column(db.String(1024), index=True) #Holds problem IDs.
    points = db.Column(db.Integer, index=True)

    def __repr__(self):
        return "<VCUser object {}>".format(self.username)
    
    def set_password(self, password):
        salt = utilities.Utility.genRandomString(size=64)
        self.password_hash = utilities.Utility.hash_pass_with_salt(password, salt)
        self.salt = salt
    
    def check_password(self, password):
        salt = self.salt
        password_hash = utilities.Utility.hash_pass_with_salt(password, salt)

        if password_hash==self.password_hash:
            return True
        return False
    
    def check_email(self):
        if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', self.email):
            return True
        return False

class Problem(db.Model):
    '''
    Used to create, edit, store,
    and retrieve information
    regarding a problem.

    TODO: Figure out which values need to be unique.
    '''

    __tablename__ = "VCProblems"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    author = db.Column(db.String(64), index=True)
    description = db.Column(db.String(250), index=True)
    test_inputs = db.Column(db.String(1024), index=True) #includes expected outputs
    difficulty = db.Column(db.String(10), index=True)
    timestamp = db.Column(db.String(32), index=True)

    def __repr__(self):
        return "<Problem object {}>".format(self.id)

    def get_test_inputs(self):
        return self.test_inputs
    
    def get_test_inputs_as_json(self):
        '''
        We're storing test_inputs as jsonified text,
        this function will be useful to keep text
        short and concise.
        '''
        return json.loads(self.test_inputs)
    
    def get_description(self):
        return self.description
    
    def get_author(self):
        return self.author
    
    def set_timestamp(self):
        self.timestamp = str(datetime.datetime.now())
    
    def get_comments(self):
        pass #Do we want to add comments to problems?