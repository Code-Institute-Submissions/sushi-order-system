# Shopping cart exercise

sushi = ["1.  Dragon Roll", "2.  Rainbow Roll", "3.  Salmon Roll", "4.  Crispy Roll", "5.  Tempura Roll"]
miso = 0.5
prices = [1.7, 1.2, 1, 1.5, 1.6]
choises = []
choise_costs = []
total = 0

print(sushi)

def main():
    startup_menue()
    

def startup_menue():
    print(
        """
        *************************************************
        * Welcome to sushi paradise ordering system!    *
        *                                               *
        * Please order from the menue below             *
        *************************************************
        """
    )





while True:
    sushi = input("Please enter the number of the roll that you want to order, or press 'q' if you have changed your mind: ")
    if sushi.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")

main()
