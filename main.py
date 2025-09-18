print("Welcome to the shoe shop chatbot")
name = input("what is your name? ")
age = input("Hello" + name + ", how old are you? ")

print()
print("Choose from the shoe selection below: " + name)
print("1. placeholder option 1")
print("2. placeholder option 2")
print("3. placeholder option 3")
print("4. placeholder option 4")
print("5. Exit the shoe shop chatbot")

user_choice = int(input("option: "))
if user_choice ==5:
    print("Thanks for visiting the shoe store!" + name)