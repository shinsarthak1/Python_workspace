friends = {
    'Shivam': 8156858763,
    'Aryan': 9156757609,
    'Shubham': 8156757302,
    'Ananya': 7178564021,
}

sorted_friends = dict(sorted(friends.items()))
print(sorted_friends)

name = input("Enter name: ")
if name in sorted_friends:
    print(f"{name} is there in the dictionary.")
else:
    phone_no = input(f"Enter {name}'s phone number")
    sorted_friends[name] = phone_no
    print(f"{name}'s details have been added to the dictionary.")


print("Updated friend's dictionary:")
for name , phone_no in sorted_friends.items():
    print(f"{name}:{phone_no}")