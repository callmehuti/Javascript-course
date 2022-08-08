countNum = 0 #count how many times user input a number
calTotal = 0 #sum of all numbers user entered

while True:
    userInput = input("Enter a number: ")
    if userInput == "":
        break
    convertInputType = float(userInput) #convert String to Float
    countNum += 1 
    calTotal = calTotal + convertInputType 

average = calTotal / countNum #solution 
    
# Display output
print(average)


# count = 5
# while count > 0:
#     print(count) #initialize
#     count = count - 1 #count will eventually descent to 0
# print("Thunderbirds are Go")