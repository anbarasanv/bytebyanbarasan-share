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
    ╔═════════════════════════════════════════════════════════════════════════════════════╗
    ║     Order class has too munch responsible by handing the payment,                   ║
    ║     so it's not single responsible we will refactor this part to adhere             ║
    ║     the single responsible principle.                                               ║
    ╚═════════════════════════════════════════════════════════════════════════════════════╝
    """
    # def pay(self, payment_type, security_code):
    #     if payment_type == "debit":
    #         print("Processing debit payment type")
    #         print(f"Verifying security code: {security_code}")
    #         self.status = "paid"
    #     elif payment_type == "credit":
    #         print("Processing credit payment type")
    #         print(f"Verifying security code: {security_code}")
    #         self.status = "paid"
    #     else:
    #         raise Exception(f"Unknown payment type: {payment_type}")


class PaymentProcessor:
    def debit_payment(self, order, security_code):
        print("processing debit payment")
        print("verifying security code")
        order.status = "paid"

    def credit_payment(self, order, security_code):
        print("processing credit payment")
        print("verifying security code")
        order.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    pay_obj = PaymentProcessor()
    pay_obj.debit_payment(order, "122334")
