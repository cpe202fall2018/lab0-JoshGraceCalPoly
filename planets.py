
# converts a weight on earth to the weight on Mars/ Jupiter and prints that weight
def weight_on_planets():
    weight = float( input() ) # read the inputed weight and convert it to a float 
    marsWeight = weight * .38 # convert the earth weight to weight on Mars
    jupiterWeight = weight * 2.34 # convert the earth weight to the weight on Jupiter
    print("What do you weigh on earth? \nOn Mars you would weigh " + str(marsWeight) + " pounds.\nOn Jupiter you would weigh " + str(jupiterWeight) + " pounds.") # print the return message with the calculated weights
if __name__ == "__main__":
    weight_on_planets()