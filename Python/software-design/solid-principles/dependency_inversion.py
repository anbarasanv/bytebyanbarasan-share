from abc import ABC, abstractmethod


class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


""" 
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║ dependency inversion means not depending on the any of the               ║
  ║ subclass but depending on the abstraction which is common                ║
  ║ for all the subclasses.                                                  ║
  ╚══════════════════════════════════════════════════════════════════════════╝
"""


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class AuthorizerSMS(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class AuthorizerGoogle(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying Google auth code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class AuthorizerRobot(Authorizer):
    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


""" 
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║ in the below classes initializers depends on the autherizer              ║
  ║ abstract classs, rather than the individual authorizers.                 ║
  ╚══════════════════════════════════════════════════════════════════════════╝
"""


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = AuthorizerRobot()
authorizer.not_a_robot()
processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)
processor.pay(order)
