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
    print("\n".join("{} {} {}".format(x, y, z) for x, y, z in zip(sushi, prices, euros)))

    pick_item(sushi)

def pick_item(sushi):

    choise = int(input("Please enter the number of the roll that you want to order, or press '0' if you have changed your mind: "))
    # Amount and cost function for sushi ordering system
    while choise != 0:
        if choise == 1 or choise == 2 or choise == 3 or choise == 4 or choise == 5:
            print(f"\nYou have selected {sushi[choise -1]} which costs {prices[choise -1]} euros.\n")
            amount = int(input("How many pieces would you like? \n"))
            # Datavalidation for correct input data
            if amount > 0 and amount < 50:
                price = prices[choise -1]
                choise_costs.append(str(round(price * amount, 2)) + " €")
                chosen_amount.append(str(amount) + " pcs")
                choises.append(sushi[choise -1])
                global total
                total += (price * amount)
                order_more = str(input("Would you like to order more from the menu? If you do, please press y. If not, press n. \n"))
                if order_more.lower() == "y":
                    startup_menu()
                elif order_more.lower() == "n":
                    order_summary()
                    break
                else:
                    print("\nYou have entered invalid data, please try again.\n")
                    pick_item(sushi)
                    break
            # Datavalidation for correct input data           
            else:
                print("\nYou have entered invalid data, please try again.\n")
                pick_item(sushi)
                break
            break
        # Datavalidation for correct input data 1-5             
        else:
            print("\nYou have entered a number that does not exist on our menu, please choose number 1-5 \n")
            pick_item(sushi)
            break


def order_summary():
# Total amount and cost from the order
    print("\n".join("{} {} {}".format(x, y, z) for x, y, z in zip(choises, chosen_amount, choise_costs)))
    print(str(round(total, 2)) + " €")
#Function for miso order 
    order_miso = str(input("Would you also want some miso for a cost of 0.5€ per serving? If you do, please press y. If not, press n. \n"))
    if order_miso.lower() == "y":
        pick_miso()
    elif order_miso.lower() == "n":
        finalize_order()
    else:
        print("\nYou have entered invalid data, please try again.\n")
        order_summary()

# Miso order amount function
def pick_miso():
    miso_amount = int(input("How many servings would you like? \n"))
    if miso_amount > 0 and miso_amount < 50:
        choise_costs.append(str(round(0.5 * miso_amount, 2)) + " €")
        chosen_amount.append(str(miso_amount) + " servings")
        choises.append("Miso soup")
        global total
        total += (0.5 * miso_amount)
        finalize_order()
    else:
        print("\nYou have entered invalid data, please try again.\n")
        pick_miso()
        
# Final order cost and choises function
def finalize_order():
    global choises
    global choise_costs
    global chosen_amount
    global total
    print("This is your final order summary: ")
    print("\n".join("{} {} {}".format(x, y, z) for x, y, z in zip(choises, chosen_amount, choise_costs)))
    print(f"Your total cost for this order is {str(round(total, 2))} €")
    checkout = str(input("Would you like to continue and finalize your order? To proceed to checkout press y, to cancel order press n \n"))
    if checkout.lower() == "y":
        final_order()
    elif checkout.lower() == "n":
        choises = []
        choise_costs = []
        chosen_amount = []
        total = 0
        main()
    else:
        print("\nYou have entered invalid data, please try again.\n")
        finalize_order()


def final_order():
    print("Thank you so much for ordering from Sushi Paradise! Come again! Hai! Kampai!")


main()
