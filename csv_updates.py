import pandas as pd
from crypts import *
filename = "Datasheet.csv"

def write_csv(mailid, password):
    '''
        Function Description : Inserts new entries in datasheet
        Arguments :
            1.mailid = string (mail id to be written)
            2.password = string (encrypts the plaintext and writes)
        Returns :
            Null
    '''
    df = pd.read_csv(filename)
    x = len(df)
    df.loc[x, "Email_id"]=mailid
    df.loc[x, "Password"]=encrypt(password)
    df.to_csv(filename, index=False)
    return

def check_credentials(mailid, password):
    '''
        Function Description : This checks the mail id and corresponding entered by user is correct and exists in data.
        Arguments :
            1.mailid = string (User entered mailid)
            2.password = string (User entered password)
        Returns :
            bool (TRUE if mailid and password is correct, FALSE if values are incorrect)
    '''
    df = pd.read_csv(filename)
    for i in range(len(df)):
        if(df.loc[i, "Email_id"]== mailid): 
            if decrypt(df.loc[i, "Password"], password):
                return True
    return False

def update_password(mailid, password):
    '''
        Function Description : This function updates the password value for the particular mail id provided.
        Arguments :
            1.mailid = string (mailid for which the corresponding password should be changed)
            2.password = string (password value to be updated)
        Returns :
            Null
    '''
    df = pd.read_csv(filename)
    for i in range(len(df)):
        if(df.loc[i, "Email_id"]== mailid):
            df.loc[i, "Password"] = encrypt(password)
    df.to_csv(filename, index=False)
    return

def check_mailid(mailid):
    '''
        Function Description : This checks whether the queried mail id exists in Datasheet
        Arguments :
            mailid = string (mail id which existence should be checked in data)
        Return :
            bool (TRUE if mail id is in datasheet, FALSE if it doesn't match with any entry in data)
    '''
    df = pd.read_csv(filename)
    for i in range(len(df)):
        if(df.loc[i, "Email_id"]== mailid):
                return True
    return False