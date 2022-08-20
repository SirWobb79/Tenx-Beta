player = "$"
areabeen = "#"

#Map
gameworld = [["." for a in range(20)] for b in range(20)]

#All controls
keys = ["w", "a", "s", "d", "k", "quit"]

x = 0
y = 0

gameworld[y][x] = player

print("Welcome to Tenx! A text game made with Python that has an\nopen-world feel! Tenx relies heavily on imagination and memory to\nnavigate your personal world. WASD to move, K is the action key.\nType 'quit' to stop the game.")

game = True

while game == True:
    
    print("\n------------------Map------------------")
    
    for i in gameworld:
        print(" ".join(i))
    
    print("|--Tenx--|World limit is 20|Use WASD to move|Find and solve riddle|")
    
    #Ralf the helper
    if x == 15:
        
        if y == 15:
            
            if move == "k":
            
                print("\nHello, I am Ralf. I am here to simply give you, the player, info\nabout Tenx.\n\nIt is a game where you move around a world, but only with a map\nshowing where you have been, nothing else. Memory is very important\nwhen traversing through Tenx. There is not too much else to say.\nHappy Travels!")
    
    #Moving around Tenx
    move = input(">")
    
    if move == "w":
        
        if y < 20:
            gameworld[y][x] = areabeen
            y -= 1
            gameworld[y][x] = player
            print("")
            
        else:
            pass
            print("You cannot move through the border")
    
    if move == "a":
        
        if x > -20:
            gameworld[y][x] = areabeen
            x -= 1
            gameworld[y][x] = player
            print("")
            
        else:
            pass
            print("You cannot move through the border")
            
    if move == "s":
        
        if y > -20:
            gameworld[y][x] = areabeen
            y += 1
            gameworld[y][x] = player
            print("")
            
        else:
            pass
            print("You cannot move through the border")
            
    if move == "d":
        
        if x < 20:
            gameworld[y][x] = areabeen
            x += 1
            gameworld[y][x] = player
            print("")
            
        else:
            pass
            print("You cannot move through the border")
            
    if move == "quit":
        
        print("\nYou ended the game manually.")
        game = False
        
    if move not in keys:
        print(move + " is not a valid command.")