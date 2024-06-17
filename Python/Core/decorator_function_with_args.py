from typing import Dict, Callable


def bill_generator(
    state_tax: float, central_tax: float, fruits_price_per_kg: Dict[str, float]
) -> Callable:
    def bill_inner(func: Callable):
        def wrapper(fruits: Dict[str, float]):
            total_cost = func(fruits)
            state_tax_amount = state_tax * total_cost
            central_tax_amount = central_tax * total_cost
            print("*" * 75, end="\n")
            print("Sample Shop Name")
            print("*" * 75, end="\n")
            print("Item", "\t" * 4, "Weight", "\t" * 4, "Price")
            print("*" * 75, end="\n")
            for item, weight in fruits.items():
                print(
                    item, "\t" * 4, weight, "\t" * 4, fruits_price_per_kg[item] * weight
                )
            print("*" * 75, end="\n")
            print("\t" * 10, f"Total:{total_cost}")
            print("\t" * 10, f"SGST:{state_tax_amount}")
            print("\t" * 10, f"CSGT:{central_tax_amount}")
            print("*" * 75, end="\n")
            print(
                "\t" * 10,
                f"Grand Total:{round(total_cost + state_tax_amount + central_tax_amount,2)}",
            )

        return wrapper

    return bill_inner

# Input
state_tax = 0.18
central_tax = 0.18
fruits_price_per_kg = {
    "apple": 200,
    "orange": 150,
    "banana": 40,
    "mango": 50,
    "grapes": 120,
    "pineapple": 120,
    "watermelon": 30,
    "kiwi": 80,
}


@bill_generator(state_tax, central_tax, fruits_price_per_kg)
def bill_calculator(fruits: Dict[str, float]) -> float:
    total_cost = 0
    for item, weight in fruits.items():
        total_cost += fruits_price_per_kg[item] * weight
    return total_cost


# Input
customer_purchase = {"apple": 0.5, "orange": 1.25, "grapes": 0.6}
bill_calculator(customer_purchase)

# Output
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
