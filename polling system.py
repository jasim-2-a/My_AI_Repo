
def create_poll():
    print("🎯 Welcome to the Polling System!")
    topic = input("Enter the poll topic (e.g., Favorite programming language): ")

    num_options = int(input("How many options do you want to add? "))
    options = []
    votes = {}

    for i in range(num_options):
        option = input(f"Enter option {i + 1}: ")
        options.append(option)
        votes[option] = 0

    print("\nPoll created! 🎉")
    print(f"🗳 Topic: {topic}")
    for i, opt in enumerate(options):
        print(f"{i + 1}. {opt}")

    return topic, options, votes


def vote_poll(topic, options, votes):
    while True:
        print(f"\n🗳 {topic}")
        for i, opt in enumerate(options):
            print(f"{i + 1}. {opt}")

        choice = input("Enter option number to vote (or type 'done' to finish): ")

        if choice.lower() == "done":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            selected = options[int(choice) - 1]
            votes[selected] += 1
            print(f"✅ Vote cast for: {selected}")
        else:
            print("❌ Invalid choice. Try again.")

    return votes


def show_results(topic, votes):
    print("\n📊 Poll Results")
    print(f"Topic: {topic}")
    for option, count in votes.items():
        print(f"{option}: {count} votes")


def main():
    topic, options, votes = create_poll()
    votes = vote_poll(topic, options, votes)
    show_results(topic, votes)


if __name__ == "__main__":
    main()
