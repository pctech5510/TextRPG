gameRunning = True
playerName = "Player"

def Adventure(playerName):
    print(f"\nWelcome to your adventure, {playerName}!")
    print("You come across a goblin patrol while going to the village.")
    print("What will you do?")
    print("1. Attack")
    print("2. Run")
    
    action = input("Choose an action: ")

    if action == "1":
        print("You charge the goblin and successfully defeat it!")
        print("You search the body and find 16 silver and a worn club.")
    elif action == "2":
        print("You tuck tail and run back to safety.")
    else:
        print("You stand in shock! The goblin captures you!")

print("\nWelcome To RPG Game")
print("This will be a rework of my C# version of RPG game")

while gameRunning:
    print(f"\nMain Menu: (Welcome, {playerName})")
    print("1. Start Game")
    print("2. About Game")
    print("s. Settings")
    print("3. Quit")
    
    choice = input("Choose an option: ")

    match choice:
        case "1":
            print("Get Ready!")
            Adventure(playerName)
        case "2":
            print("\nThis game is created in Python with the mentorship of AI!")
        case "s":
            playerName = input("\nPlease enter your character name: ")
        case "3":
            print("\nGoodbye!")
            gameRunning = False
        case _:
            print("\nInvalid choice, please try again.")
