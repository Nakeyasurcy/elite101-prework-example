

import time

print("Welcome to the retail chatbot.")
print()
print('I am here to provide you with anything you need help with ')
time.sleep(1)

# Inventory dictionary: item name -> stock quantity
inventory = {
    "Black T shirt": 10,
    "Grey sweatpants": 8,
    "Blue baggy jeans": 9,
    "Grey sweatshirt": 5,
    "Jordan 1's": 3,
    "Jordan 4's": 12
}

# A list to simulate "purchased" items (you can pretend the user bought these)
purchased_items = ["These are the items you have purchased: grey sweatpants", "grey sweatshirt", "jordan 1's"]
print(purchased_items)
while True:
    print()
    print("Hello, welcome to the clothing retailer chatbot, how may I help you today: ")
    print("1. Return an item")
    print("2. Exchang an item")
    print("3. check the return policy")
    print("4. request a refund option")
    print("5. veiw the inventory")
    print("6. Exit the shoe shop chatbot")
    
    user_choice = input("\nEnter the number of your choice: ")

    # return an item option
    if user_choice == "1":
        print("\nReturn an item")
        name = input(" What is your name? ")
        email = input(" What is your email? ")
        item_name = input("which item would you like to return from your purchased list? ")

        if item_name in purchased_items:
            reason = input("Why are you returning it? (e.g., too big, you don't like it): ")
            print("\nProcessing your return request, this will be just a minute")
            time.sleep(2)
            purchased_items.remove(item_name) # remove the item from your purchased list
            inventory[item_name] = inventory.get(item_name, 0) + 1  # put it back in stock in the inentory
            print(f"\nThank you, {name}! Your return for '{item_name}' has been processed.")
            print(f"Your refund has been proccessed and was sent to your email: {email}. The item was adding back to the inventory.\n")
        else:
            print("Item was not found")

    # Exchanging th item
    elif user_choice == "2":
        print("\nExchange an item")
        name = input("Enter your name: ")
        email = input(" Email address: ")
        old_item = input("Which item would you like to exchange? ")

        if old_item in purchased_items:
            new_item = input(" What item would you like instead? ")

            if new_item in inventory and inventory[new_item] > 0:
                print("\nProcessing your exchange request...")
                time.sleep(2)
                purchased_items.remove(old_item)
                purchased_items.append(new_item)
                inventory[old_item] = inventory.get(old_item, 0) + 1  # returned item back to stock
                inventory[new_item] -= 1  # remove one from stock
                print(f"\n Exchange complete! You returned '{old_item}' and received '{new_item}'.")
                print(f"A confirmation email will be sent to {email} shortly.\n")
            else:
                print(f"\nSorry, '{new_item}' is currently out of stock.\n")
        else:
            print(f"\nYou haven’t purchased '{old_item}', so we can’t process an exchange.\n")

    # OPTION 3 - RETURN POLICY
    elif user_choice == "3":
        print("\nTRENDY THREADS RETURN POLICY")
        print("----------------------------------------")
        print("• Items can be returned within 30 days of delivery.")
        print("• Items must be unworn, unwashed, and in their original packaging.")
        print("• Refunds are processed within 3–5 business days after inspection.")
        print("• First exchanges are free — additional ones may include shipping costs.")
        print("•  Clearance or final sale items cannot be returned or exchanged.\n")
        input("Press Enter to go back to the main menu...")

    # OPTION 4 - REQUEST A REFUND
    elif user_choice == "4":
        print("\n💳 REQUEST A REFUND")
        name = input(" What’s your full name? ")
        email = input(" What’s your email address? ")
        item_name = input("Which item are you requesting a refund for? ")

        if item_name in purchased_items:
            refund_reason = input("❓ Please explain why you’d like a refund: ")
            print("\nSubmitting your refund request...")
            time.sleep(2)
            purchased_items.remove(item_name)
            inventory[item_name] = inventory.get(item_name, 0) + 1
            print(f"\n Refund approved for '{item_name}', {name}.")
            print(f"A confirmation has been sent to {email}. The item was added back to inventory.\n")
        else:
            print(f"\n'{item_name}' was not found in your purchase history, so a refund can’t be processed.\n")

    # OPTION 5 - VIEW INVENTORY
    elif user_choice == "5":
        print("\n CURRENT INVENTORY")
        print("----------------------------------------")
        for item, stock in inventory.items():
            status = " In Stock" if stock > 0 else "Out of Stock"
            print(f"{item} - {stock} left | {status}")
            time.sleep(0.3)
        print("----------------------------------------")
        print("✨ More styles arriving soon!\n")
        input("Press Enter to return to the menu...")

    # OPTION 6 - EXIT
    elif user_choice == "6":
        print("\n Thank you for visiting Trendy Threads!")
        print("We appreciate your business and hope to see you again soon. \n")
        break

    else:
        print("\n Invalid choice. Please enter a number between 1 and 6.\n")
        time.sleep(1)
