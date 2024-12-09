import random
SquareList = []
for i in range(10):
    sq = random.randint(1,50)
    SquareList.append(sq)
print(SquareList)
for i in SquareList:
    print("The square of all the numbers in the list is : " , i**2)

    
