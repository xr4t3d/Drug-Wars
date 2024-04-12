import random
import os

def main():
    print("Welcome to Drug Wars!")
    print("You borrowed $20,000 from a loanshark and have 30 days to pay it back.")

    wallet_balance = 20000
    debt = 20000
    day = 30
    cocaine_qty = 0
    heroin_qty = 0
    marijuana_qty = 0
    current_city = "New York"

    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

    # Initialize drug prices
    cocaine_price = random.randint(2000, 5000)
    heroin_price = random.randint(1000, 3000)
    marijuana_price = random.randint(500, 2000)

    while day > 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print("\nDay", day)
        print("Wallet Balance: ${:,.0f}".format(wallet_balance))
        print("Loan Balance: ${:,.0f}".format(debt))
        print("Current City:", current_city)
        print("\nYour current drug quantities:")
        print("Cocaine:", cocaine_qty, "kilograms")
        print("Heroin:", heroin_qty, "kilograms")
        print("Marijuana:", marijuana_qty, "kilograms")

        print("\nDrug Prices:")
        print("1. Cocaine: $", cocaine_price)
        print("2. Heroin: $", heroin_price)
        print("3. Marijuana: $", marijuana_price)
        print("4. Sell drugs")
        print("5. Loanshark")
        print("6. Travel")
        print("7. Quit")

        choice = input("\nWhat do you want to do? (1/2/3/4/5/6/7): ")
        if not choice or choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Please make a valid selection.")
            input("Press Enter to continue...")
            continue

        if choice == '7':
            print("Game Over. You quit.")
            break

        elif choice == '6':
            travel_cost = random.randint(50, 250)
            if wallet_balance < travel_cost:
                print("You don't have enough money to travel.")
                input("Press Enter to continue...")
                continue

            print("\nAvailable cities to travel to:")
            for index, city in enumerate(cities, start=1):
                print(index, ".", city)
            city_choice = input("\nWhich city do you want to travel to? (1-10): ")
            try:
                city_index = int(city_choice) - 1
                if 0 <= city_index < len(cities):
                    current_city = cities[city_index]
                    wallet_balance -= travel_cost

                    # Update drug prices when traveling
                    cocaine_price = random.randint(2000, 5000)
                    heroin_price = random.randint(1000, 3000)
                    marijuana_price = random.randint(500, 2000)
                    day -= 1  # Day progresses only when player travels

                    # Apply interest on the debt
                    interest = debt * 0.10
                    debt += interest
                    print("Interest accrued today: ${:,.0f}".format(interest))
                else:
                    print("Invalid city choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
            continue

        try:
            if choice == '1' or choice == '2' or choice == '3':
                drug = ""
                if choice == '1':
                    drug = "cocaine"
                elif choice == '2':
                    drug = "heroin"
                else:
                    drug = "marijuana"
                quantity = int(input("How many kilograms of {} do you want to buy? (You can buy {}) ".format(drug, wallet_balance // cocaine_price if choice == '1' else wallet_balance // heroin_price if choice == '2' else wallet_balance // marijuana_price)))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            cost = cocaine_price * quantity
            if wallet_balance >= cost:
                cocaine_qty += quantity
                wallet_balance -= cost
                print("You bought", quantity, "kilograms of cocaine.")
            else:
                print("Not enough money to purchase this amount. Returning to main menu...")
                input("Press Enter to continue...")
                continue

        elif choice == '2':
            cost = heroin_price * quantity
            if wallet_balance >= cost:
                heroin_qty += quantity
                wallet_balance -= cost
                print("You bought", quantity, "kilograms of heroin.")
            else:
                print("Not enough money to purchase this amount. Returning to main menu...")
                input("Press Enter to continue...")
                continue

        elif choice == '3':
            cost = marijuana_price * quantity
            if wallet_balance >= cost:
                marijuana_qty += quantity
                wallet_balance -= cost
                print("You bought", quantity, "kilograms of marijuana.")
            else:
                print("Not enough money to purchase this amount. Returning to main menu...")
                input("Press Enter to continue...")
                continue

        elif choice == '4':
            try:
                drug_to_sell = input("\nWhich drug do you want to sell? (1/2/3): ")
                if drug_to_sell == '1':
                    max_quantity = cocaine_qty
                    quantity_to_sell = int(input("How many kilograms of cocaine do you want to sell? (Max: {}) ".format(max_quantity)))
                    if quantity_to_sell > max_quantity:
                        print("You don't have enough cocaine to sell.")
                    else:
                        sell_price = cocaine_price * quantity_to_sell
                        wallet_balance += sell_price
                        cocaine_qty -= quantity_to_sell
                        print("You sold", quantity_to_sell, "kilograms of cocaine for $", sell_price)
                elif drug_to_sell == '2':
                    max_quantity = heroin_qty
                    quantity_to_sell = int(input("How many kilograms of heroin do you want to sell? (Max: {}) ".format(max_quantity)))
                    if quantity_to_sell > max_quantity:
                        print("You don't have enough heroin to sell.")
                    else:
                        sell_price = heroin_price * quantity_to_sell
                        wallet_balance += sell_price
                        heroin_qty -= quantity_to_sell
                        print("You sold", quantity_to_sell, "kilograms of heroin for $", sell_price)
                elif drug_to_sell == '3':
                    max_quantity = marijuana_qty
                    quantity_to_sell = int(input("How many kilograms of marijuana do you want to sell? (Max: {}) ".format(max_quantity)))
                    if quantity_to_sell > max_quantity:
                        print("You don't have enough marijuana to sell.")
                    else:
                        sell_price = marijuana_price * quantity_to_sell
                        wallet_balance += sell_price
                        marijuana_qty -= quantity_to_sell
                        print("You sold", quantity_to_sell, "kilograms of marijuana for $", sell_price)
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        elif choice == '5':
            print("\nLoanshark Options:")
            print("1. Pay the balance of the loan")
            print("2. Pay other amount")
            print("3. Take a Loan")
            repay_choice = input("Enter your choice (1/2/3): ")
            if repay_choice == '1':
                repay_amount = debt
            elif repay_choice == '2':
                try:
                    repay_amount = int(input("How much do you want to pay back to the loanshark? "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            elif repay_choice == '3':
                try:
                    loan_amount = int(input("How much do you want to borrow from the loanshark? "))
                    wallet_balance += loan_amount
                    debt += loan_amount
                    print("You borrowed $", loan_amount, "from the loanshark.")
                    input("Press Enter to continue...")
                    continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            else:
                print("Invalid choice. Returning to main menu...")
                input("Press Enter to continue...")
                continue

            if repay_amount <= wallet_balance:
                wallet_balance -= repay_amount
                debt -= repay_amount  # Deduct repayment from debt
                print("You paid back $", repay_amount, "to the loanshark.")
            else:
                print("You don't have enough money to pay back that amount.")
            input("Press Enter to continue...")  # Continue to the next day

        else:
            print("Invalid choice. Try again.")
            continue

        # Random event: Police raid
        if random.randint(1, 10) == 1:
            confiscated_money = random.randint(500, 1500)
            wallet_balance -= confiscated_money
            print("\nOh no! The police raided your stash and you lost $", confiscated_money)

        # Random event: Find drugs
        if random.randint(1, 20) == 1:
            found_drugs = random.choice(["cocaine", "heroin", "marijuana"])
            found_quantity = random.randint(1, 5)
            if found_drugs == "cocaine":
                cocaine_qty += found_quantity
                print("You found", found_quantity, "kilograms of cocaine!")
            elif found_drugs == "heroin":
                heroin_qty += found_quantity
                print("You found", found_quantity, "kilograms of heroin!")
            elif found_drugs == "marijuana":
                marijuana_qty += found_quantity
                print("You found", found_quantity, "kilograms of marijuana!")
            input("Press Enter to continue...")

        # Random event: Find drugs on street or in car trunk
        if random.randint(1, 20) == 1:
            event = random.choice(["street", "car"])
            found_drugs = random.choice(["cocaine", "heroin", "marijuana"])
            found_quantity = random.randint(1, 5)
            if event == "street":
                print("You found", found_quantity, "kilograms of", found_drugs, "on the street!")
            elif event == "car":
                print("You found", found_quantity, "kilograms of", found_drugs, "in the trunk of a car!")
            if found_drugs == "cocaine":
                cocaine_qty += found_quantity
            elif found_drugs == "heroin":
                heroin_qty += found_quantity
            elif found_drugs == "marijuana":
                marijuana_qty += found_quantity
            input("Press Enter to continue...")

        day -= 1

    if debt <= 0:
        print("\nCongratulations! You paid back your debt of $20,000 to the loanshark in", 30 - day, "days.")
    else:
        print("\nGame Over. You failed to pay back your debt of $20,000 to the loanshark in 30 days.")

    input("Press Enter to continue...")

if __name__ == "__main__":
    main()
