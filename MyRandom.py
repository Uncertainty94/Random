import matplotlib.pyplot as plt
import math

M=5
maxLen=10000

def frac(num):
    return math.modf(num)[0]

def randomNew(previous):
    return frac(previous*M)

def getNewArr(num):
    result=[]
    while num not in result and len(result) < maxLen:

        result.append(num)
        num = randomNew(num)
    return result

def makeArrToDraw(fullArr):
    result = [0,0,0,0,0,0,0,0,0,0]
    for num in fullArr:
        i =math.trunc(num*10)
        result[i]+=1
    print(result)
    return result

def drawHist(arr):
    osx=makeArrToDraw(arr)
    osy=[0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250]
    width = 200
    plt.bar(osy, osx, width)
    plt.show()

R0=0.12341512312451
randArr = getNewArr(R0)
drawHist(randArr)

