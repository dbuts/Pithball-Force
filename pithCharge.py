import math
if __name__ == "__main__":
    inp = 0;
    while inp>= 0:
        inp = input("What is the distance of the pithball from the center?: "
        theta = math.asin(inp/.0198)
        ret = math.sqrt((math.degrees(math.sin(theta))*m*g*inp)/k)
        print(ret)


