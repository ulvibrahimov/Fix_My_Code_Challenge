#!/usr/bin/python3
"""
User class
"""
import hashlib
import uuid


class User():
    """ User class representation """

    def __init__(self):
        """ Initialize User """
        self.__password = None
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """ Password getter """
        return self.__password

    @password.setter
    def password(self, pwd):
        """ Password setter """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """ Check if password is valid """
        if pwd is None or type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        return self.__password == hashlib.md5(pwd.encode()).hexdigest().lower()


if __name__ == "__main__":
    print("Test User")
    user_1 = User()
    user_1.password = "Documentation"
    print("Is valid password 'Documentation': {}".format(user_1.is_valid_password("Documentation")))
    print("Is valid password 'documentation': {}".format(user_1.is_valid_password("documentation")))
    print("Is valid password 'Doc': {}".format(user_1.is_valid_password("Doc")))
