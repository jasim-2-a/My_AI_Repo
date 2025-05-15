def intro():
    print("Welcome to the Soul Society!")
    print("You find yourself standing at the entrance of a Serite.")
    print("There are two paths in front of you:")
    print("1. First Path to become a Subsitite Soul Reaper.")
    print("2. A dark path to work with Aizen sama.")
    
    choice = input("Which path will you choose? (1 or 2): ")
    
    if choice == '1':
        bright_path()
    elif choice == '2':
        dark_path()
    else:
        print("Invalid choice, please select 1 or 2.")
        intro()

def bright_path():
    print("\nYou walk down in the serite. The sunlight filters through the trees.")
    print("After a short walk, you come to see a hollow.")
    print("You can either:")
    print("1. Fight the hollow.")
    print("2. Run like a coward.")
    
    choice = input("What will you do? Become the man of your words or runaway and abadon your friends (1 or 2): ")
    
    if choice == '1':
        Fight_hollow()
    elif choice == '2':
        intro()
    else:
        print("Invalid choice, please select 1 or 2.")
        bright_path()

def Fight_hollow():
    print("\nYou defeated the hollow and find yourself in a serite street.")
    print("In the distance, you spot a 13 court office!")
    print("You can either:")
    print("1. Walk towards the 13 court office.")
    print("2. Move around in serite streets")
    
    choice = input("What will you do? (1 or 2): ")
    
    if choice == '1':
        court_office()
    elif choice == '2':
        print("\nYou move around in serite streets and did not come up with your words and stay like a coward. This is the end of your Journey.")
    else:
        print("Invalid choice, please select 1 or 2.")
        Fight_hollow()

def court_office():
    print("\nYou arrive at the 13 court office gates. The doors are slightly open.")
    print("You can either:")
    print("1. Enter the office.")
    print("2. Turn back and leave the forest.")
    
    choice = input("What will you do? (1 or 2): ")
    
    if choice == '1':
        print("\nYou enter the office and discover hidden treasures Soul Key inside! Congratulations, you win!")
    elif choice == '2':
        intro()
    else:
        print("Invalid choice, please select 1 or 2.")
        court_office()

def dark_path():
    print("\nYou decide to take the dark path. That Aizen will decide for youc.")
    print("After a few minutes of walking, you hear something rustling in the bushes.")
    print("You can either:")
    print("1. Investigate the noise.")
    print("2. Keep walking.")
    
    choice = input("What will you do? (1 or 2): ")
    
    if choice == '1':
        investigate_noise()
    elif choice == '2':
        print("\nYou keep walking, but the path leads you to a dead end. This is the part of Aizen plain .This is end  of your journey.")
    else:
        print("Invalid choice, please select 1 or 2.")
        dark_path()

def investigate_noise():
    print("\nYou approach the bushes and find a hollow hiding there!")
    print("The hollow offers you a choice:")
    print("1. be  the Arrancer.Like the hollow")
    print("2. Kill the hollow.")
    
    choice = input("What will you do? (1 or 2): ")
    
    if choice == '1':
        print("\nThe creature rewards you with a Arrancar Powers that grants you Power and unlock your Bankai. Congratulations, you win Aizen Trust!")
    elif choice == '2':
        print("\nYou kill the hollow into the forest. You walk back to the start of the dark path.But it is Aizen plain but you did not go as plain so  This is the end of your adventure.")
    else:
        print("Invalid choice, please select 1 or 2.")
        investigate_noise()

if __name__ == "__main__":
    intro()
