toppings = []

while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ").lower()

    if topping == 'quit':
        break

    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)

print("Your pizza with the following toppings is ready:")
for topping in toppings:
    print(f"- {topping}")
