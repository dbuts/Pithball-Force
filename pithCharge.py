import math
import sys
if __name__ == "__main__":
    inp = 0
    m = 4.e-5
    g = 3.924e-4 
    k = 9.e-9 
    theta = 0
    while inp>= 0:
        inp = float(input("What is the distance of the pithball from the center?(cm): "))
        inp = inp/100
        theta = math.asin(inp/.198)
        ret = math.sqrt((math.degrees(math.sin(theta))*m*g*inp*inp)/k)
        print(ret)


