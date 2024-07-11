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


# =================== Before Liskov substitutuion following ===================

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order, security_code):
#         pass


# class DebitPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("processing debit payment")
#         print("verifying security code")
#         order.status = "paid"


# class CreditPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("processing credit payment")
#         print("verifying security code")
#         order.status = "paid"

# """
#   ╔══════════════════════════════════════════════════════════════════════════╗
#   ║ if we see compared to other classes, the below class                     ║
#   ║ takes email instead security_code, according to liskov                   ║
#   ║ substitution principle we should be able to substitue                    ║
#   ║ super class with subclass are in the same level classes                  ║
#   ║ so the signatures suppose to match                                       ║
#   ╚══════════════════════════════════════════════════════════════════════════╝
# """

# class PaypalPaymentProcessor(PaymentProcessor):
#     def pay(self, order, email):
#         print("processing paypal payment")
#         print("verifying security code")
#         order.status = "paid"

# =================== After Liskov substitutuion following ===================


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing debit payment")
        print(f"verifying {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing credit payment")
        print(f"verifying {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def pay(self, order):
        print("processing paypal payment")
        print(f"verifying {self.email}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

pay_obj = PaypalPaymentProcessor("sample@email.com")
pay_obj.pay(order)
