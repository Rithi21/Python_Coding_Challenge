class User:
    def __init__(self, user_id, username, password, role):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__role = role
    def get_user_id(self):
        return self.__user_id
    def set_user_id(self,user_id):
        self.__user_id=user_id
    def get_username(self):
        return self.__username
    def set_user_id(self,username):
        self.__username=username
    def get_password(self):
        return self.__password
    def set_user_id(self,password):
        self.__password=password
    def get_role(self):
        return self.__role
    def set_role(self,role):
        self.__role=role
    

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}, Role: {self.role}"
