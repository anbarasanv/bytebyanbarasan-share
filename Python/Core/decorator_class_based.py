from random import randint
from typing import Callable

# API limits per day as per the account type
ACCOUNT_TYPE = {"Silver": 5, "Gold": 10, "Platinum": 15}

# Customer Database with id, name, account type and used count
# Let us assume this is the initial customer database
# Every day the used count will be reset to 0

CUSTOMERS = [
    {"id": 1, "name": "Anba", "account_type": "Silver", "used": 0},
    {"id": 2, "name": "Sunil", "account_type": "Gold", "used": 0},
    {"id": 3, "name": "Rohit", "account_type": "Platinum", "used": 0},
]


class CustomerValidator:
    # mimic the customer database
    def __init__(self, customer_id: int) -> None:
        self.customer_id = customer_id
        self.customer = CUSTOMERS[self.customer_id - 1]
        self.account_type = (
            self.customer["account_type"] if self.customer else None
        )  # type: account_type
        self.api_usage = self.customer["used"] if self.customer else None
        self.api_limit = ACCOUNT_TYPE.get(self.account_type)

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if self.api_limit is None:
                return "Invalid account type"
            if self.api_usage < self.api_limit:
                self.api_usage += 1
                CUSTOMERS[self.customer_id - 1]["used"] = self.api_usage
                return f"customer_name:{self.customer['name']} & Your Special Number is: {func(*args, **kwargs)}"
            else:
                return f"API Limit Exceeded. (Limit: {self.api_limit})"

        return wrapper


customer_id = 1


# function to get a special number
@CustomerValidator(customer_id)
def get_special_number():
    return randint(1, 100)


# now we are going to simulate 6 calls for the silver customer
for i in range(6):
    print(get_special_number())


# output
# customer_name:Anba & Your Special Number is: 48
# customer_name:Anba & Your Special Number is: 60
# customer_name:Anba & Your Special Number is: 4
# customer_name:Anba & Your Special Number is: 55
# customer_name:Anba & Your Special Number is: 64
# API Limit Exceeded. (Limit: 5)
