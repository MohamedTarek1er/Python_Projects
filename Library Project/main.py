from Librarymanager import Library

Lib = Library(["COD Mobile", "PUBG Mobile", "Free Fire", "Hopeless"], {}, {})

while True:
    print("This is the Gamers library!")
    op = int(input("What would you like to do:\n1. See the game list\n2. Rent a game\n3. Donate a game\n4. Return a game\n(1/2/3/4): "))

    if op == 1:
        print("\nAvailable games:")
        print(Lib.games())

    elif op == 2:
        print("\nAvailable games:")
        print(Lib.games())
        name = input("Your name: ")
        gamename = input("Game name: ")
        Lib.lend(gamename, name)

    elif op == 3:
        name = input("Your name: ")
        gamename = input("Game name to donate: ")
        Lib.donate(name, gamename)

    elif op == 4:
        if len(Lib.lenders) > 0:
            print("\nCurrently lent games:")
            print(Lib.lenders)
            name = input("Your name: ")
            gamename = input("Game name you want to return: ")
            Lib.returnb(name, gamename)
        else:
            print("No game debtor currently in the system!")

    else:
        print("Invalid option. Please select 1, 2, 3, or 4.")
