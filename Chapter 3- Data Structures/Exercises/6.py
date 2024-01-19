invitees = ["Albert Einstein", "Lionel Messi", "Drake", "Kanye West"]

for person in invitees:
    print(f"Dear {person},\nI would like to invite you to dinner. It would be an honor to have your company.\nSincerely, Ziyan")

print("\nUnfortunately, the new dinner table won't arrive in time, and we can only invite two people for dinner.\n")

while len(invitees) > 2:
    removed_guest = invitees.pop()
    print(f"Sorry, {removed_guest}, we can't invite you to dinner.")

for remaining_person in invitees:
    print(f"Dear {remaining_person},\nYou're still invited to dinner. We look forward to seeing you!\n")

del invitees[:]
print("Guest list after removing the last two names:", invitees)
