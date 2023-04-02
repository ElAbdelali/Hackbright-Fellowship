inputNum = int(input("It's a simple game really, input 1 to win, input 2 to lose, input anything else to be stuck in limbo: "))

if inputNum == 1:
    print("You won the game!")
elif inputNum == 2:
    print("You lost the game!")
else:
    print("You are stuck in limbo!")