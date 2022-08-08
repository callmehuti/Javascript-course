# num = 0
# tot = 0.0
# while True:
#     number = input("Enter a number")
#     if number == 'done':
#         break
#     try :
#         num1 = float(number)
#     except:
#         print('Invailed Input')
#         continue
#     num = num+1
#     tot = tot + num1
# print ('all done')
# print (tot,num,tot/num)

num = 0
calTotal = 0
while True:
    userInput = input("Enter a number: ")
    if userInput == "":
        break
    try:
        getNum = float(userInput)
    except:
       continue
    num = num + 1
    calTotal = calTotal + getNum
    average = calTotal / num
# Display output
print(average)
# print("getNum is: ", getNum)
# print("num is: ", num)