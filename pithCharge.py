import math
import os
clear = lambda: os.system('clear')

if __name__ == "__main__":
    inp = 0
    m = 4.e-5 #mass of pith ball
    g = 9.81 #Earth's gravational constant
    G = 6.67408e-11 #Universal gravitational Constant
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
        print("Electric Force: " + str(forcg))
        print("Number of excess Protons/Electrons: " + str(format((char/1.60217662e-19),"e")))
        print("Gravitational Force Between two Balls: " + str((G*m*m)/(2*inp*2*inp)))
