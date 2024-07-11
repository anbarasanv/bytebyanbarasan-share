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


# =========== Before Interface Segregation substitutuion following ============

""" 
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║ now if we want to introduce a new method to the payment                  ║
  ║ processor but that is not required by all the subclasses                 ║
  ║ it's better to segregate the interfaces.                                 ║
  ╚══════════════════════════════════════════════════════════════════════════╝
 """

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass

# class DebitPaymentProcessor(PaymentProcessor):
#     def __init__(self, security_code):
#         self.security_code = security_code

#     def pay(self, order):
#         print("processing debit payment")
#         print(f"verifying {self.security_code}")
#         order.status = "paid"


# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self, security_code):
#         self.security_code = security_code

#     def pay(self, order):
#         print("processing credit payment")
#         print(f"verifying {self.security_code}")
#         order.status = "paid"


# class PaypalPaymentProcessor(PaymentProcessor):
#     def __init__(self, email):
#         self.email = email

#     def pay(self, order):
#         print("processing paypal payment")
#         print(f"verifying {self.email}")
#         order.status = "paid"

# =========== After Interface Segregation substitutuion following ============


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class OTPPaymentProcessor(PaymentProcessor):
    @abstractmethod
    def sms_auth(self, otp):
        pass


class DebitPaymentProcessor(OTPPaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.otp_verified = False

    def sms_auth(self, otp):
        self.otp_verified = True

    def pay(self, order):
        if not self.otp_verified:
            raise Exception("Invalid OTP")
        print(f"verifying {self.security_code}")
        print("processing debit payment")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print(f"verifying {self.security_code}")
        print("processing credit payment")
        order.status = "paid"


class PaypalPaymentProcessor(OTPPaymentProcessor):
    def __init__(self, email):
        self.email = email
        self.otp_verified = False

    def sms_auth(self, otp):
        self.otp_verified = True

    def pay(self, order):
        if not self.otp_verified:
            raise Exception("Invalid OTP")
        print(f"verifying {self.email}")
        print("processing paypal payment")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())

pay_obj = PaypalPaymentProcessor("sample@email.com")
pay_obj.sms_auth("1234")
pay_obj.pay(order)
