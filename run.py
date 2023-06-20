# Shopping cart exercise

sushi = ["1.  Dragon Roll", "2.  Rainbow Roll", "3.  Salmon Roll", "4.  Crispy Roll", "5.  Tempura Roll"]
MISO = 0.5
prices = [1.7, 1.2, 1, 1.5, 1.6]
choises = []
choise_costs = []
total = 0

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
    # Credit to scb at stack overflow
    print("\n".join("{} {}".format(x, y) for x, y in zip(sushi, prices)))

    pick_item(sushi)

def pick_item(sushi):

    choise = int(input("Please enter the number of the roll that you want to order, or press '0' if you have changed your mind: "))

    while choise != 0:
        if choise == 1 or choise == 2 or choise == 3 or choise == 4 or choise == 5:
            print(f"\nYou have selected {sushi[choise -1]} which costs {prices[choise -1]} euros.\n")
            amount = int(input("How many pieces would you like? \n"))
            if amount > 0 and amount < 50:
                price = prices[choise -1]
                choise_costs.append(price * amount)
            else:
                print("\nYou have entered invalid data, please try again.\n")
                break
            choises.append(sushi[choise -1])
            print(choises)
            print(choise_costs)
        else:
            print("\nYou have entered a number that does not exist on our menue, please choose number 1-5 \n")
            pick_item(sushi)
            break
    # while True:
    #     choise = input("Please enter the number of the roll that you want to order, or press 'q' if you have changed your mind: ")
    #     if choise.lower() == "q":
    #         break
    #     else:
    #         price = float(input(f"Enter the price of a {food}: $"))
    #         choises.append(choise)
    #         prices.append(price)

main()

# print("----- YOUR CART -----")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print()
# print(f"Your total is: ${total}")

