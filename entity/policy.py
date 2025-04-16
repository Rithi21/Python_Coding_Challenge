class Policy:
    def __init__(self, policy_id=None, policy_name=None, policy_type=None, policy_amount=None):
        self.__policy_id = policy_id
        self.__policy_name = policy_name
        self.__policy_type = policy_type
        self.__policy_amount = policy_amount

    def get_policy_id(self):
        return self.__policy_id

    def set_policy_id(self, policy_id):
        self.__policy_id = policy_id

    def get_policy_name(self):
        return self.__policy_name

    def set_policy_name(self, policy_name):
        self.__policy_name = policy_name

    def get_policy_type(self):
        return self.__policy_type

    def set_policy_type(self, policy_type):
        self.__policy_type = policy_type

    def get_policy_amount(self):
        return self.__policy_amount

    def set_policy_amount(self, policy_amount):
        self.__policy_amount = policy_amount

    def __str__(self):
        return (f"Policy [ID: {self.__policy_id}, Name: {self.__policy_name}, "f"Type: {self.__policy_type}, Coverage: {self.__policy_amount}]")
