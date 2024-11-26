
gameRunning = True
playerName = "player"


print("\nWelcome To RPG Game")
print("This will be a rework of my C Sharp version of RPG game")

while (gameRunning):
    print(f"\nMain Menu: (Welcome, {playerName})")
    print("1. Start Game")
    print("2. About Game")
    print("s. Settings")
    print("3. Quit")
    print("Choose an option: ")
    choice = input()

    match choice:
        case "1":
            print("Get Ready!")#Adventure(playerName)
        case "2":
            print("\nThis game is created in python with the mentor of AI")
        case "s":
            print("\nPlease enter your character name: ")
            playerName = input()
        case "3":
            print("\nGood-Bye")
            gameRunning = False
        case _:
            print("\nInvaild choice, please try again")


    #Method to handle the game adventure
    def Adventure(str, playerName):
        print(f"\nWelcome to your adventure, {playerName}!")
        print("You come across a goblin patrol while going to the village")
        print("What will you do?")

        print("1. Attack")
        print("2. Run")
        
        action = input()

        if action == "1":
            print("You charge the goblin and attack the goblin and successfully defeated them.")
            print("You search the body and find 16 silver, and a worn club.")
        elif action == "2":
            print("You tuck tale and run in the direction")
        else:
            print("You stand in shock of actually seeing a goblin, the goblin captures you!")
