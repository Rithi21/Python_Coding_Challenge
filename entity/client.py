class Client:
    def __init__(self, client_id, client_name, contact_info, policy):
        self.__client_id = client_id
        self.__client_name = client_name
        self.__contact_info = contact_info
        self.__policy = policy

    def get_client_id(self):
        return self.__client_id
    
    def set_client_id(self, client_id):
        self.__client_id = client_id

    def get_client_name(self):
        return self.__client_name
    
    def set_client_name(self, client_name):
        self.__client_name = client_name

    def get_contact_info(self):
        return self.__contact_info
    
    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def get_policy(self):
        return self.__policy
    
    def set_poilcy(self, policy):
        self.__policy = policy

    

    def __str__(self):
        return f"Client [ID: {self.client_id}, Name: {self.client_name}, Contact: {self.contact_info}]"
