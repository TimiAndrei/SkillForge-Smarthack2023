from user import user

class organization:
    def __init__(self, name, users = [], admin = None):
        self.name = name
        self.users = users
        self.admin = admin

    def getUsers(self):
        return self.users
    def getAdmin(self):
        return self.admin

    def addUser(self, user):
        self.users.append(user)
