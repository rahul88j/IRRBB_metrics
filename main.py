import portfolio

portfolio_list=[]
choice = 1
try:
    while (choice != 5):
        print('''
        ====================================
        RiskLab - Banking Risk Analyzer
        Version 1.0
        ====================================
        ''')

        print('''
        1. Add instrument
        2. View Portfolio
        3. Search Instrument
        4. Delete Instrument
        5. Exit
        ''')

        choice = int(input("enter choice:"))
        if (choice == 1):
            portfolio.instrument_add(portfolio_list)
            print("Instrument added")
        elif (choice == 2):
            portfolio.portfolio_view(portfolio_list)
        elif (choice == 3):
            portfolio.portfolio_search(portfolio_list)
        elif(choice == 4):
            portfolio.instrument_delete(portfolio_list)
        elif(choice == 5):
            exit()
        else:
            print("wrong choice ")
except ValueError:
    print(f"\nError: it is not a valid choice number. Please enter a number")

except Exception as e:
    print("\n An unexpected error occured")
    print(f"Error: {e}")

