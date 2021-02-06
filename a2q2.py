# NSID - bhs053
# Student Number - 11258695
# Course Number - CMPT145
# Lecture Section - 04(Arlin)

def findCoordinates(directions):
    '''
    Purpose - This function calculates the coordinates in a standard Cartesian grid and prints the calculated
               final coordinates (x,y) of Mechagodzilla after it finishes a series of movement
    Pre Conditions - always assume that the input string of directions will be E,W,N and S and starts at the base
                    coordinates of (0,0) (i.e. x=0 and y=0)
    Post Conditions - None
    Return - None
    '''
    # Starting the base coordinates x and y with 0
    x = 0
    y = 0
    isInputValid = True
    for d in directions:
        # If the d in the input string is E, increment the value of x with 1
       if d == 'E':
         x = x + 1
        # If the d in the input string is W, decrement the value of x with 1
       elif d == 'W':
         x = x - 1
        # If the d in the input string is N, increment the value of y with 1
       elif d == 'N':
         y = y + 1
        # If the d in the input string is S, decrement the value of y with 1
       elif d == 'S':
         y = y - 1
       else:
        isInputValid = False
        print("Invalid input")
        break
    if isInputValid:
      print("     ", "(", x, ',', y, ")")  # prints the x and y coordinates to the console

findCoordinates("EN")
findCoordinates("ETN")

