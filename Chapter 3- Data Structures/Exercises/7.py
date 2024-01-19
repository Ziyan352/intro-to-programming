places_to_visit = ["Tokyo", "Paris", "Islamabad", "New York", "London"]

print("Original Order:", places_to_visit)

print("Alphabetical Order:", sorted(places_to_visit))

print("Original Order (unchanged):", places_to_visit)

print("Reverse Alphabetical Order:", sorted(places_to_visit, reverse=True))

print("Original Order (unchanged):", places_to_visit)

places_to_visit.reverse()
print("Reversed Order:", places_to_visit)

places_to_visit.reverse()
print("Original Order (reversed again):", places_to_visit)

places_to_visit.sort()
print("Alphabetical Order:", places_to_visit)

places_to_visit.sort(reverse=True)
print("Reverse Alphabetical Order:", places_to_visit)
