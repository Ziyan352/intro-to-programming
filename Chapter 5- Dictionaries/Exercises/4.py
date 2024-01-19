rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nNames of each river:")
for river in rivers.keys():
    print(river)

print("\nNames of each country:")
for country in rivers.values():
    print(country)
