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


class AdminUser(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, role="admin")

    def manage_policies(self):
        print(f"{self.get_username()} is managing policies.")

    def __str__(self):
        return f"User ID: {self.get_user_id()}, Username: {self.get_username()}, Role: {self.get_role()}"

        
class AgentUser(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, role="agent")

    def assist_clients(self):
        print(f"{self.get_username()} is assisting clients.")

    def __str__(self):
        return f"User ID: {self.get_user_id()}, Username: {self.get_username()}, Role: {self.get_role()}"



admin = AdminUser(1, "Kamal", "kamal123")
agent = AgentUser(2, "Lakshmi", "Luck345")

print(admin) 
admin.manage_policies()

print(agent) 
agent.assist_clients()



  
