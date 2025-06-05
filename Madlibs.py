print("Let's play Mad Libs!\n")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a type of food: ")
madlib = f"""
One {adjective} day, I went to the {place} to see a {animal}.
It was {verb}ing around like crazy! I laughed so hard, I dropped my {food}.
Then the {noun} ran by and scared everyone away!
What a day to remember!
"""
print(madlib)
