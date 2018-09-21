def weight_on_planets():
    weight = float( input() )
    marsWeight = weight * .38
    jupiterWeight = weight * 2.34
    print("What do you weigh on earth? \nOn Mars you would weigh " + str(marsWeight) + " pounds.\nOn Jupiter you would weigh " + str(jupiterWeight) + " pounds.")
    # print( "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds.")
if __name__ == "__main__":
    weight_on_planets()