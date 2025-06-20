import pandas as pd
from datetime import datetime

categories = ["Food", "Transportation", "Entertainment", "Utilities", "Health", "Other"]


def load_expenses(file="expenses.csv"):
    try:
        return pd.read_csv(file)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])


def save_expenses(expenses, file="expenses.csv"):
    expenses.to_csv(file, index=False)


def add_expense(expenses):
    print("\nAvailable categories:", ", ".join(categories))
    category = input("Enter category: ").capitalize().strip()

    if category not in categories:
        print("Invalid category. Please choose from the available categories.")
        return expenses

    amount = input("Enter amount: ").strip()
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return expenses

    description = input("Enter description (optional): ").strip()
    date = input(f"Enter date (leave empty for today, default: {datetime.today().strftime('%Y-%m-%d')}): ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    
    new_expense = pd.DataFrame([[date, category, amount, description]], columns=["Date", "Category", "Amount", "Description"])
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    print("\n✅ Expense added successfully!")

    return expenses


def view_summary(expenses):
    print("\nView summary by: ")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ").strip()
        daily_expenses = expenses[expenses["Date"] == date]
        print(f"\nDaily expenses for {date}:")
        print(daily_expenses)
        print("Total:", daily_expenses["Amount"].sum())
        
    elif choice == "2":
        week = input("Enter week (YYYY-Wxx format): ").strip()
        weekly_expenses = expenses[expenses["Date"].str.startswith(week)]
        print(f"\nWeekly expenses for {week}:")
        print(weekly_expenses)
        print("Total:", weekly_expenses["Amount"].sum())

    elif choice == "3":
        month = input("Enter month (YYYY-MM format): ").strip()
        monthly_expenses = expenses[expenses["Date"].str.startswith(month)]
        print(f"\nMonthly expenses for {month}:")
        print(monthly_expenses)
        print("Total:", monthly_expenses["Amount"].sum())

    else:
        print("Invalid option. Please choose a valid option.")


def view_category_summary(expenses):
    category_summary = expenses.groupby("Category")["Amount"].sum().reset_index()
    print("\nCategory-wise Summary:")
    print(category_summary)

def main():

    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expense Summary")
        print("3. View Category Summary")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            expenses = add_expense(expenses)
            save_expenses(expenses)

        elif choice == "2":
            view_summary(expenses)

        elif choice == "3":
            view_category_summary(expenses)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
