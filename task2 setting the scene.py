place = input("Choose a place forest or cave? ")
action = input("light a torch or proceed in the dark?")

if place == "cave":
   if action == "light a torch":
        print("Go forth with caution!")
   if action == "proceed in the dark":
        print("You sure are brave!")
elif place == "forest":
    print("Watch out for jaguars!")