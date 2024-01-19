invitees = ["Albert Einstein", "Lionel Messi", "Kanye West"]

for person in invitees:
    print(f"Dear {person},\nI would like to invite you to dinner. It would be an honor to have your company.\nSincerely, Ziyan")

guest_cant_make_it = "Lionel Messi"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

new_invitee = "Drake"
invitees[invitees.index(guest_cant_make_it)] = new_invitee

print("Updated Invitations:")
for person in invitees:
    print(f"Dear {person},\nI would like to invite you to dinner. It would be an honor to have your company.\nSincerely, Ziyan")
