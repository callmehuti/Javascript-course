numOfInt = int(input("Please enter the number of integers: ")) 
total = 0
checkLoop = 1
while checkLoop <= numOfInt:
    enterNum = float(input("Enter a number: "))
    print("total is: ", total)
    print("checkLoop is: ", checkLoop)
    print("enterNum is: ", enterNum)
    if enterNum == "":
        break
    total += enterNum
    print("total after calculation is: ", total)
    checkLoop += 1
    print("check Loop after calculation is: ", checkLoop)
    print("-----------END OF ONE LOOP--------------------")
    
average = total / numOfInt # Last edit: average = total / 4 and it placed in while loop
# For tester
print(average)