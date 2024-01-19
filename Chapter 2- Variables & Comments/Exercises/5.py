usb_stick_price = 6
budget = 50

num_usb_sticks = budget // usb_stick_price

money_left = budget % usb_stick_price

print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{money_left} left.")