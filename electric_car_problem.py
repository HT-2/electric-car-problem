maxCharge = int(input("Maximum car mileage in one charge: ")) # max mileage that car gives per charge
cityList = input("Enter the list of all the cities(enter with space in between): ").split(" ") # list of cities/nodes
# list of vertice costs
vertexCostList = input("Enter the list of costs from left to right respectively(enter with space in between): ").split(" ")

# validating vertexCostList and converting its elements from string to integer 
if len(vertexCostList) != len(cityList) - 1:
    print("Error: The number of vertices/costs should be equal to number of nodes - 1")
else:
    vertexCostList = [int(cost) for cost in vertexCostList]

currentCarCharge = maxCharge # variable to keep track of current car charge as it travels
stopsList = [] # output list with suggested stops
stopsList.append(cityList[0]) # appending start node/city to stop list

# for loop to iterate/travel until we reach the final node/city: Time Complexity O(number of vertices)
for i in range(len(vertexCostList)):
    if currentCarCharge >= vertexCostList[i] * 2: # travel ahead if enough fuel to backtrack to same city.
        currentCarCharge -= vertexCostList[i]
    else: # take a stop and charge if not enough fuel to backtrack to same city.
        currentCarCharge = maxCharge
        currentCarCharge -= vertexCostList[i]
        stopsList.append(cityList[i])

stopsList.append(cityList[-1]) # adding our destination/final stop into the stop list
print("Output-> Here are the suggested stops: " + str(stopsList)) # our final desired output i.e. list of stops

# Time Complexity = O(n) wherein n = Number of vertices/costs i.e. Number of cities/nodes - 1
# Optimal Space Complexity Achieved


