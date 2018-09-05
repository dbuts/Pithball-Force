import math
import os
clear = lambda: os.system('clear')

if __name__ == "__main__":
    inp = 0
    m = 4.e-5 #mass of pith ball
    g = 9.81 #gravational constant
    k = 9.e9 #Coulomb's constant
    len =.198 #length of connecting rope
    theta = 0 #angle between rope and y-axis
    forc = 0
    while inp>= 0:
        inp = float(input("What is the distance of the pithball from the center?(cm): "))
        inp = inp/100
        theta = math.asin(inp/len)
        forcg = math.sin(theta)*m*g #force due to gravity in x-direction
        char = math.sqrt((forcg/k)*((2*inp)*(2*inp))) #charge on a pith ball
        forc = ((char*char)*k)/((2*inp)*(2*inp)) #force calculated via charge
        print("Charge per pith ball: " + str(char))
        print("Electric Force: " + str(forc))
        #print("Electric Force calc by gravity: " + str(forcg))
        temp = input("Press enter to move on, or q to quit: ")
        if temp == 'q':
            exit()
        clear()
