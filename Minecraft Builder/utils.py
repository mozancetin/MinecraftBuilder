import pyautogui
import time
import pyperclip
from mytest import *

def write(text : str, ms : float = 0.1):
    pyautogui.press("t")
    pyautogui.write(text)
    pyautogui.press("enter")
    time.sleep(ms)

def writeSpecial(text : str, ms : float = 0.1):
    pyperclip.copy(text)
    pyautogui.press("t")
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    pyautogui.press("enter")
    time.sleep(ms)

def startingPack():
    writeSpecial("/tp @a 0 1 0")
    writeSpecial("/spawnpoint @a")
    write("/fill -5 0 -5 5 0 5 dirt")
    write("/gamerule keepInventory true")
    
    writeSpecial(text='/setblock 0 1 -3 chest 0 replace {Items:[{Slot:0,id:log,Count:20},{Slot:1,id:wooden_pickaxe,Count:1},{Slot:2,id:wooden_axe,Count:1},{Slot:3,id:wooden_shovel,Count:1},{Slot:4,id:cooked_beef,Count:20},{Slot:5,id:coal,Count:10},{Slot:6,id:bed,Count:2}]}')
    
    write("/setblock 1 1 -3 torch")
    write("/setblock -1 1 -3 torch")
    write("/setblock 0 1 -2 torch")
    write("/setblock 0 1 -4 torch")

    write("/setblock 3 1 0 crafting_table")
    write("/setblock 0 1 3 furnace")
    writeSpecial("/gamemode survival @a")


def buildIslandMap(wait : int = 5):
    for x in range(wait):
        print(f"Random Island Build is starting in {wait - x} secs...")
        time.sleep(1)

    startingPack()
    for x in range(random.randint(3, 7)):
        i = Islands(startPoint=randomizePoint("0 5 0", randomness=0.4), size=random.randint(5, 9))
        i.buildClassic(wait=0)

def buildRandomIslands(startPoint : str, wait : int = 5, countMin : int = 3, countMax : int = 5, sizeMin : int = 5, sizeMax : int = 12, randomizeY : bool = False):
    for x in range(wait):
        print(f"Random Island Build is starting in {wait - x} secs...")
        time.sleep(1)

    for x in range(random.randint(countMin, countMax)):
        i = Islands(startPoint=randomizePoint(startPoint, randomness=0.4, randomY=randomizeY), size=random.randint(sizeMin, sizeMax))
        i.buildClassic(wait=0)


# time.sleep(5)
# startingPack()

#buildIslandMap()
#buildRandomIslands(startPoint="40 24 -41", countMax=5, sizeMin=5, sizeMax=9, countMin=4)