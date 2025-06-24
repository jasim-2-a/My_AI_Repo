from datetime import datetime


DIARY_FILE = "diary_entries.txt"

def write_entry():
    print("\n🖊️ Write your diary entry:")
    entry = input("Enter your thoughts (press Enter when done): ").strip()
    if not entry:
        print("❗ Empty entry. Entry not saved.")
        return
 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    formatted_entry = f"{timestamp}\n{entry}\n{'-'*50}\n"
    
 
    with open(DIARY_FILE, "a") as file:
        file.write(formatted_entry)
    
    print("\n✅ Diary entry saved successfully!")

def view_entries():
    try:
        with open(DIARY_FILE, "r") as file:
            entries = file.read().strip()
        
        if not entries:
            print("❗ No diary entries found.")
        else:
            print("\n📖 Your Diary Entries:")
            print(entries)
    
    except FileNotFoundError:
        print("❗ No diary entries found. Start by writing your first entry.")

def main():
    while True:
        print("\nDiary Application")
        print("1. Write a new entry")
        print("2. View all entries")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("\nGoodbye! Come back soon to record more memories!")
            break
        else:
            print("❗ Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
