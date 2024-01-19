sandwich_orders = ["Tuna", "Chicken Club", "Pastrami", "Veggie Delight", "Turkey & Swiss", "BLT", "Pastrami", "Pastrami"]

finished_sandwiches = []

if 'Pastrami' in sandwich_orders:
    print("Sorry, the deli has run out of pastrami.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
