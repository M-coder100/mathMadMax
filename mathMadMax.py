from IPython.display import clear_output 
import random
import os
from time import sleep
numCount = 0
score = 0
level = "easy"
placeMaxNum = []
arithmeticSignRange = []
mistakes = 0
maxMistakes = 0
levels = {
    "easy": {
        "numCount": 2,
        "placeMaxNum": [1],
        "arithmeticSignRange": [0, 1],
        "maxMistakes": 6
    },
    "medium": {
        "numCount": 2,
        "placeMaxNum": [1, 2],
        "arithmeticSignRange": [0, 3],
        "maxMistakes": 4
    },
    "hard": {
        "numCount": 3,
        "placeMaxNum": [1, 2],
        "arithmeticSignRange": [0, 3],
        "maxMistakes": 2
    },
}

def setDifficulty(levelDict):
    global numCount, placeMaxNum, arithmeticSignRange, maxMistakes
    numCount = levelDict["numCount"]
    placeMaxNum = levelDict["placeMaxNum"]
    arithmeticSignRange = levelDict["arithmeticSignRange"]
    maxMistakes = levelDict["maxMistakes"]

def generateRandomNums():
    newNums = []
    for i in range(numCount):
        num = round((random.random()+(random.choice(placeMaxNum)-1))*10)
        newNums.append(str(7 if num == 0 else 2 if num == 1 else num))
    return newNums

def getRandomArithmeticSign(signRange):
    arithmeticSigns = ["+", "-", "*", "/"][signRange[0]:signRange[1]]
    return random.choice(arithmeticSigns)

def generateEquation(maxResult):
    nums = generateRandomNums()
    for i in range(len(nums)-1):
        nums.insert(i*2+1, getRandomArithmeticSign(arithmeticSignRange))        
    eq = " ".join(nums)
    print(".", end="")
    if (eval(eq) > maxResult or eval(eq) < 0): eq = generateEquation(maxResult)
    return eq

def clearScreen(): 
    os.system("cls")
    clear_output()

def init():
    global level
    clearScreen()
    level = input("Chose difficulty [easy, medium, hard]: ")
    setDifficulty(levels[level])
    loop()
    
def loop():
    clearScreen()
    global score, mistakes
    print("#"*score, end=" ") if score else False
    eq = generateEquation(100)
    print("\n"+eq)
    userGuess = input("=> ")
    clearScreen()

    if (userGuess and int(userGuess) == eval(eq)): 
        score += 1
        print("(*) Good job!", "Score:", score)
    else:
        mistakes += 1
        print("(!) That isn't quite right...", "Mistakes:", "/".join([str(mistakes), str(maxMistakes)]))
    print(eq, "=>", eval(eq))

    sleep(3)
    clearScreen()
    if (mistakes >= maxMistakes):
        print("Well played!")
        print("Score:", score)
        print("Difficulty:", level)
        return
    loop()
init()