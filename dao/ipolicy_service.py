from abc import ABC, abstractmethod

class IPolicyService(ABC):
    @abstractmethod
    def create_policy(self, policy): 
        pass

    @abstractmethod
    def get_policy(self, policy_id):
        pass

    @abstractmethod
    def get_all_policies(self): 
        pass

    @abstractmethod
    def update_policy(self, policy): 
        pass

    @abstractmethod
    def delete_policy(self, policy_id): 
        pass
