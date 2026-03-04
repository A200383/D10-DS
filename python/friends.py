are_friends = input("Are they friends? (true/false): ")
account_privacy = input("Is receiver account public or private? ")

if are_friends == "true":
    print("Message can be sent ✔")
else:
    if account_privacy == "public":
        print("Message can be sent ✔")
    else:
        print("Message cannot be sent ❌")
