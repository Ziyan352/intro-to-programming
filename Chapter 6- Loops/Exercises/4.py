sandwich_orders = ["Tuna", "Chicken Club", "Veggie Delight", "Turkey & Swiss", "BLT"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
