def add_expense(expenses, amount, category): 
    expenses.append({'amount': amount, 'category': category}) #Add expenses to the list
    
def print_expenses(expenses):
    for expense in expenses: #For each expense on the list...
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}') #...print its amount and category
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses)) #returns the sum of the expense amounts on the list
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses) #returns each expense thats corresponds to the searched category on the list

def main():
    expenses = [] #This list represents the database
    while True: #This loop keeps the menu always accessible after each task performed
        print('\n\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break #This option ends the program

if __name__ == '__main__': #this block ensures that the call to the main function is directly executed if this is the main script and not a module of another script
    main()