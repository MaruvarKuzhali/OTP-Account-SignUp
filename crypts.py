#This python file handles the hashing of password
import config #context is stored in config.py to hide the hashing method

def encrypt(password):
    '''
        Function Description : This function hash the password which is to be stored.
        Arguments :
            password = string (plain text password entered by user)
        Returns :
            string (hashed password to be written in datasheet)
    '''
    return config.context.hash(password)

def decrypt(hashed_password, password):
    '''
        Function Description : This function compares the hashed password stored and user entered password
                                using passlib in-built verify method.
        Arguments :
            1.hashed_password = string (password from datasheet)
            2.password = string (test password to be compared)
        Returns :
            bool (TRUE if it matches, FALSE if it doesn't match)
    '''
    return config.context.verify(password, hashed_password)
