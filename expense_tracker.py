expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"Amount": amount, "Category": category})
    print("Expense added!\n")

def view_expenses():
    total = 0
    for exp in expenses:
        print("Amount:", exp["Amount"], "Category:", exp["Category"])
        total += exp["Amount"]
    print("Total Expense:", total)
    print()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")