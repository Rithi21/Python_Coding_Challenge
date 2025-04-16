class Payment:
    def __init__(self, payment_id=None, payment_date=None, payment_amount=None, client=None):
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__payment_amount = payment_amount
        self.__client = client

    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_payment_date(self):
        return self.__payment_date

    def set_payment_date(self, payment_date):
        self.__payment_date = payment_date

    def get_payment_amount(self):
        return self.__payment_amount

    def set_payment_amount(self, payment_amount):
        self.__payment_amount = payment_amount

    def get_client(self):
        return self.__client

    def set_client(self, client):
        self.__client = client

    def __str__(self):
        return (f"Payment [ID: {self.__payment_id}, Date: {self.__payment_date}, "
                f"Amount: {self.__payment_amount}, Client: {self.__client}]")
