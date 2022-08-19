x = 0
y = 0

print("Welcome to Tenx Beta! A text game made with Python that has an\nopen-world feel! Tenx relies heavily on imagination and memory to\nnavigate your personal world")

game = True

while game == True:
    
    print("\n|--Tenx--|x , y|World limit is 20|Use WASD to move|Info at 15, -15|")
    
    #Where you exist in Tenx
    print("Position:",x,",",y)
    
    #Ralf the helper
    if x == 15:
        
        if y== -15:
            
            print("\nHello, I am Ralf. I am here to simply give you, the player, info\nabout Tenx.\n\nIt is a game where you move around a world, but without any visual clues on where you are. Memory is very important when traversing\nthrough Tenx. There is not too much else to say. Happy Travels!")
    
    #Moving around Tenx
    move = input(">")
    
    if move == "w":
        
        if y < 20:
            y += 1
            print("")
            
        else:
            pass
            print("You cannot move through the border")
    
    if move == "a":
        
        if x > -20:
            x -= 1
            
        else:
            pass
            print("You cannot move through the border")
            
    if move == "s":
        
        if y > -20:
            y -= 1
            
        else:
            pass
            print("You cannot move through the border")
            
    if move == "d":
        
        if x < 20:
            x += 1
            
        else:
            pass
            print("You cannot move through the border")