# Global variables for summarizing order choises

sushi = ["1.Dragon Roll", "2.Rainbow Roll", "3.Salmon Roll", "4.Crispy Roll", "5.Tempura Roll"]
euros = ["€", "€", "€", "€", "€"]
prices = [1.7, 1.2, 1, 1.5, 1.6]
choises = []
choise_costs = []
chosen_amount = []
total = 0

# Main program
def main():
    welcome()
    startup_menu()
    
# Welcome text
def welcome():

    print(
        """
        *************************************************
        * Welcome to sushi Paradise Ordering System!    *
        *                                               *
        * Please order from the menu below              *
        *************************************************

        """
    )
    
# Menu function
def startup_menu():

    # Credit to scb at stack overflow
    print("*" * 20)
    print("\n".join("{} {} {}".format(x, y, z) for x, y, z in zip(sushi, prices, euros)))
    print("*" * 20)
    print("")
    pick_item(sushi)


def pick_item(sushi):

    try:
        choise = int(input("Please enter the number of the roll that you want to order, or press '0' if you have changed your mind:\n"))
        # Amount and cost function for sushi ordering system
        while choise != 0:
            if choise == 1 or choise == 2 or choise == 3 or choise == 4 or choise == 5:
                pick_amount(choise)
                break
            # Datavalidation for correct input data 1-5             
            else:
                print("\nYou have entered a number that is not provided in the menu, please choose number 1-5 \n")
                pick_item(sushi)
                break
    except:
        print("\nSorry! You have entered invalid data, please try again.\n")
        pick_item(sushi)


def pick_amount(choise):
    print(f"\nYou have selected {sushi[choise - 1]} which costs {prices[choise - 1]} euros.\n")
    try:
        amount = int(input("How many pieces would you like?\n"))
        # Datavalidation for correct input data
        if amount > 0 and amount < 50:
            price = prices[choise - 1]
            choise_costs.append(str(round(price * amount, 2)) + " €")
            chosen_amount.append(str(amount) + " pcs")
            choises.append(sushi[choise - 1])
            global total
            total += (price * amount)
            order_more()
        # Datavalidation for correct input data           
        else:
            print("\OOPS! You have entered a number that is not accepted, please choose a number between 1 and 50.\n")
            pick_amount(choise)
    except:
        print("\nWOOPS! You have entered invalid data, please try again.\n")
        pick_amount(choise)


def order_more():
    more_sushi = str(input("Would you like to order more from the menu? If you do, please press y. If not, press n.\n"))
    if more_sushi.lower() == "y":
        startup_menu()
    elif more_sushi.lower() == "n":
        order_summary()
    else:
        print("\nSorry! You have entered invalid data, please try again.\n")
        order_more()


def order_summary():
    # Total amount and cost from the order
    print("")
    print("*" * 30)
    print("\n".join("{} {} {}".format(x, y, z) for x, y, z in zip(choises, chosen_amount, choise_costs)))
    print("*" * 30)
    print(f"Total cost: {str(round(total, 2))} €")
    print("*" * 20)
    print("")
    #Function for miso order 
    order_miso = str(input("Would you also want some miso for a cost of 0.5€ per serving? If you do, please press y. If not, press n.\n"))
    if order_miso.lower() == "y":
        pick_miso()
    elif order_miso.lower() == "n":
        finalize_order()
    else:
        print("\nSorry! You have entered invalid data, please try again.\n")
        order_summary()

# Miso order amount function
def pick_miso():
    try:
        miso_amount = int(input("How many servings would you like?\n"))
        if miso_amount > 0 and miso_amount < 50:
            choise_costs.append(str(round(0.5 * miso_amount, 2)) + " €")
            chosen_amount.append(str(miso_amount) + " servings")
            choises.append("Miso soup")
            global total
            total += (0.5 * miso_amount)
            finalize_order()
        else:
            print("\nSorry! You have entered invalid data, please try again.\n")
            pick_miso()
    except:
        print("\OOPS! You have entered invalid data, please try again.\n")
        pick_miso()
        
# Final order cost and choises function
def finalize_order():
    global choises
    global choise_costs
    global chosen_amount
    global total
    print("")
    print("This is your final order summary: ")
    print("*" * 40)
    print("\n".join("{} {} {}".format(x, y, z) for x, y, z in zip(choises, chosen_amount, choise_costs)))
    print("*" * 40)
    print(f"Your total cost for this order is {str(round(total, 2))} €")
    print("*" * 40)
    print("")
    checkout = str(input("Would you like to continue and finalize your order? To proceed to checkout press y, to cancel order press n:\n"))
    if checkout.lower() == "y":
        final_order()
    elif checkout.lower() == "n":
        choises = []
        choise_costs = []
        chosen_amount = []
        total = 0
        main()
    else:
        print("\nSorry! You have entered invalid data, please try again.\n")
        finalize_order()


def final_order():
    print("")
    print("Thank you so much for ordering from Sushi Paradise! Come again! Hai! Kampai!")


main()
