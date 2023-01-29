print("""+============================+
+ Slightly shady riddle game +
+============================+""")


word = input("I am every Mexican child's nightmare. What am I?\n")

count = 1

hints = [
    "It's not real... Or is it?😵‍💫",
    "Grannies also fear it. 👵🏽",
    "It ends with an 'a'",
    "Goats are also not fond of it.🐐 But it's fond of them.",
    "You're so slow it would have gotten you by now.🐢",
]

while word != "chupacabra":
    if count == 1:
        print("Ha! Got you! It's a loop!")
    if count == 3:
        print("It's funny because you're stuck! 🤣")

    if count >= 10:
        print("Ok, ok, I'll tell you. It's a chupacabra.")
        break
    elif count % 2 == 0:
        print(f"Hint: {hints.pop(0)}")
    elif count % 5 == 0:
        print("Mwahaha! You'll never escape! 😈")
    else:
        print("Wrong!")
    count += 1
    word = input("Guess again.\n")

print(f"{'Correct! ' if word == 'chupacabra' else ''}You've successfully left the loop. 🎉")
