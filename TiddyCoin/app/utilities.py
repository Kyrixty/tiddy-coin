import hashlib
import random
import string
import os

class Utility:
    '''
    Provides useful general functions--such as generating a random string--of which 
    can be useful to multiple programs in the application.
    '''

    def genRandomString(size=10, chars=string.ascii_letters + string.digits):
        '''
        Returns a random string with a default size of 10, using the string module.

        Usage: genRandomString() --> Will return a random string with a size of (size, default is 10).
        '''

        return ''.join(random.choices(chars, k=size))

    def hash_pass(password):
        #Hashes password with a randomly generated salt.
        salt = self.genRandomString(size=64)

        return hashlib.sha384(str(salt+password).encode()).hexdigest()
    
    def hash_pass_with_salt(password, salt):
        #Hashes password with a salt provided.
        return hashlib.sha384(str(salt+password).encode()).hexdigest()
    
    def get_site_news():
        basedir = os.path.dirname(__file__)

        with open(basedir+"\\Site News.txt", mode="r") as f:
            return f.read()