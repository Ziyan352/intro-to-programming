pets = [
    {'kind': 'Dog', 'owner': 'Mark'},
    {'kind': 'Cat', 'owner': 'Harry'},
    {'kind': 'Parrot', 'owner': 'David'},
    {'kind': 'Fish', 'owner': 'Bob'},
    {'kind': 'Rabbit', 'owner': 'Eve'}
]

for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"{owner}'s pet is a {kind}.")
