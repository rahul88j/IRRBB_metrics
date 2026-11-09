print('''
====================================
RiskLab - Banking Risk Analyzer
Version 1.0
====================================
''')

print('''1. Add instrument
2. View Portfolio
3. Search Instrument
4. Delete Instrument
5. Exit
''')
choice = 1
try:
    while (choice != 5):
        choice = int(input("enter choice:"))
        if (choice == 1):
            print("Instrument added")
        elif (choice == 2):
            print("portfolio viewed")
        elif (choice == 3):
            print (" instrument searched")
        elif(choice == 4):
            print ("instrument deleted")
        elif(choice == 5):
            exit()
        else:
            print("wrong choice ")
except ValueError:
    print(f"\nError: it is not a valid choice number. Please enter a number")

except Exception as e:
    print("\n An unexpected error occured")



# choice = input(int())