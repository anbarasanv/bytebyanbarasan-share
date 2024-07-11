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
  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ we can see that the order class has to be modified,                              ║
  ║ when every new payment system added, so according to                             ║
  ║ open-close principle we should only allow to extend                              ║
  ║ not to modify.                                                                   ║
  ╚══════════════════════════════════════════════════════════════════════════════════╝
"""

# class PaymentProcessor:
#     def debit_payment(self, order, security_code):
#         print("processing debit payment")
#         print("verifying security code")
#         order.status = "paid"

#     def credit_payment(self, order, security_code):
#         print("processing credit payment")
#         print("verifying security code")
#         order.status = "paid"


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing debit payment")
        print("verifying security code")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing credit payment")
        print("verifying security code")
        order.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    pay_obj = DebitPaymentProcessor()
    pay_obj.pay(order, "122334")
