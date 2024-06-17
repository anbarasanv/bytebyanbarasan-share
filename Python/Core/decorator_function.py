from typing import Dict

STATE_TAX = 0.18
CENTRAL_TAX = 0.18
FRUITS_PRICE_PER_KG = {
    "apple": 200,
    "orange": 150,
    "banana": 40,
    "mango": 50,
    "grapes": 120,
    "pineapple": 120,
    "watermelon": 30,
    "kiwi": 80,
}


def bill_generator(func):
    def wrapper(fruits):
        total_cost = func(fruits)
        state_tax = STATE_TAX * total_cost
        central_tex = CENTRAL_TAX * total_cost
        print("*" * 75, end="\n")
        print("Sample Shop Name")
        print("*" * 75, end="\n")
        print("Item", "\t" * 4, "Weight", "\t" * 4, "Price")
        print("*" * 75, end="\n")
        for item, weight in fruits.items():
            print(item, "\t" * 4, weight, "\t" * 4, FRUITS_PRICE_PER_KG[item] * weight)
        print("*" * 75, end="\n")
        print("\t" * 10, f"Total:{total_cost}")
        print("\t" * 10, f"SGST:{state_tax}")
        print("\t" * 10, f"CSGT:{central_tex}")
        print("*" * 75, end="\n")
        print("\t" * 10, f"Grand Total:{round(total_cost+state_tax+central_tex,2)}")

    return wrapper


@bill_generator
def bill_calculator(fruits: Dict[str, float]) -> float:
    total_cost = 0
    for item, weight in fruits.items():
        total_cost += FRUITS_PRICE_PER_KG[item] * weight
    return total_cost


# Input
customer_purchase = {"apple": 0.5, "orange": 1.25, "grapes": 0.6}
bill_calculator(customer_purchase)

# Output
# ***************************************************************************
# Sample Shop Name
# ***************************************************************************
# Item 				 Weight 				 Price
# ***************************************************************************
# apple 				 0.5 				 100.0
# orange 				 1.25 				 187.5
# grapes 				 0.6 				 72.0
# ***************************************************************************
# 										 Total:359.5
# 										 SGST:64.71
# 										 CSGT:64.71
# ***************************************************************************
# 										 Grand Total:488.92
