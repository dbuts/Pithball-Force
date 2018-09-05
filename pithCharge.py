import math
import sys
if __name__ == "__main__":
    inp = 0
    m = 4.e-5 #mass of pith ball
    g = 9.81 #gravational constant
    k = 9.e-9 #Coulomb's constant
    len =.198 #length of connecting rope
    theta = 0 #angle between rope and y-axis
    forc = 0
    while inp>= 0:
        inp = float(input("What is the distance of the pithball from the center?(cm): "))
        inp = inp/100
        theta = math.asin(inp/len)
        forcg = math.sin(theta)*m*g
        char = math.sqrt((forcg/k)*((2*inp)*(2*inp)))
        forc = ((char*char)*k)/((2*len)*(2*len)) 
        print("Charge per pith ball: " + str(char))
        print("Electric Force: " + str(forc))
        print("Electric Force calc by gravity: " + str(forcg))
