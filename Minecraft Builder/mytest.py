import pyautogui
import time
import random
from structures import Tree, Market, Well

class RandomBlocks:

    def __init__(self, startPoint : str, endPoint : str, randomness : float = 0.5):
        
        # Create random blocks
        self.start = startPoint.split(" ")
        self.end = endPoint.split(" ")

        self.x = abs(int(self.start[0]) - int(self.end[0]))
        self.y = abs(int(self.start[1]) - int(self.end[1]))
        if self.y < 1:
            self.y = 1
        self.z = abs(int(self.start[2]) - int(self.end[2]))
        self.randomness = randomness
        self.amount = self.x * self.y * self.z * self.randomness * 0.5
        if int(self.amount) < 1: self.amount = 1

    def build(self, block : str = "cobblestone"):

        for i in range(int(round(self.amount))):
            pyautogui.press("t")
            pyautogui.write(f"/setblock {int(self.start[0]) + random.randint(0,self.x)} {int(self.start[1]) + random.randint(0,self.y)} {int(self.start[2]) + random.randint(0,self.z)} {block}")
            pyautogui.press("enter")
            time.sleep(0.1)

    def buildClass(self, classToBuild : type):
        if classToBuild == Tree:
            for i in range(int(round(self.amount))):
                tree = classToBuild(location=f"{random.randint(min(int(self.start[0]),int(self.end[0])), max(int(self.start[0]),int(self.end[0])))} {self.start[1]} {random.randint(min(int(self.start[2]),int(self.end[2])), max(int(self.start[2]),int(self.end[2])))}")
                tree.build(wait=0)

    def buildNormalled(self, block : str = "cobblestone"):
        height = random.randint(0,self.y)
        self.amount *= 2
        for x in range(height):
            self.amount = int(round(self.amount / 2))
            for i in range(int(round(self.amount))):
                pyautogui.press("t")
                pyautogui.write(f"/setblock {int(self.start[0]) + random.randint(0,self.x)} {int(self.start[1]) + int(x)} {int(self.start[2]) + random.randint(0,self.z)} {block}")
                pyautogui.press("enter")
                time.sleep(0.1)

def randomizePoint(point : str, randomness : float = 0.25, randomY : bool = False):
    value = int(round(randomness * 100))
    x, y, z = point.split(" ")
    if not randomY:
        x, y, z = int(x) + random.randint(-value, value), int(y), int(z) + random.randint(-value, value)
    else:
        x, y, z = int(x) + random.randint(-value, value), int(y) + random.randint(int(round(value/5)), int(round(2 * value / 5))), int(z) + random.randint(-value, value)
    
    return f"{x} {y} {z}"

class Islands:
    def __init__(self, startPoint : str, size : int = 15) -> None:
        self.x, self.y, self.z = startPoint.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 5 if int(self.y) >= 5 else int(self.y), int(self.z)
        self.size = size

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        pyautogui.press("enter")
        time.sleep(ms)

    def buildClassic(self, wait : int = 5) -> None:
        for x in range(wait):
            print(f"Island creating is starting in {wait - x} sec...")
            time.sleep(1)

        self.island = list()
        self.level1 = ["dirt", "gravel", "stone 1", "stone 3", "stone 5"]
        self.level2 = ["iron_ore", "coal_ore", "gold_ore"]
        self.level3 = ["redstone_ore", "lapis_ore"]
        self.level4 = ["emerald_ore"]
        self.level5 = ["diamond_ore"]

        self.write(f"/fill {self.x} {self.y + self.size - 1} {self.z} {self.x + self.size - 1} {self.y + self.size - 1} {self.z + self.size - 1} grass")
        self.write(f"/fill {self.x} {self.y + self.size - 2} {self.z} {self.x + self.size - 1} {self.y + self.size - 2} {self.z + self.size - 1} dirt")
        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + self.size - 1} {self.y + self.size - 3} {self.z + self.size - 1} stone")

        for a in range(self.size):
            for b in range(self.size):
                if b <= 1: 
                    continue

                for c in range(self.size):
                    if random.randint(0, 10000) not in range(4500, 6000):
                        continue

                    listChoice = random.randint(0, 1000)
                    if listChoice in range(0, 700):
                        self.block = random.choice(self.level1)
                    elif listChoice in range(600, 800):
                        self.block = random.choice(self.level2)
                    elif listChoice in range(800, 970):
                        self.block = random.choice(self.level3)
                    elif listChoice in range(970, 990):
                        self.block = random.choice(self.level4)
                    else:
                        self.block = random.choice(self.level5)

                    self.write(f"/setblock {self.x + (self.size - (c + 1))} {self.y + (self.size - (b + 1))} {self.z + (self.size - (a + 1))} {self.block}", ms=0.05)
        
        if random.randint(0, 100) in range(20, 80):
            r = RandomBlocks(startPoint=f"{self.x} {self.y + self.size - 1} {self.z}", endPoint=f"{self.x + self.size - 1} {self.y + self.size - 1} {self.z + self.size - 1}", randomness=random.uniform(0.01 * self.size, 0.03 * self.size))
            r.buildClass(Tree)
        else:
            newRandom = random.randint(1000, 10000)
            if newRandom in range(3460, 4525):
                m = Market(location=f"{self.x + int(round(((self.size - 1) / 2)))} {self.y + self.size - 1} {self.z + int(round(((self.size - 1) / 2)))}")
                m.build(wait=0)
            else: #newRandom in range(4600, 4700):
                w = Well(startPoint=f"{self.x + int(round(((self.size - 1) / 2)))} {self.y + self.size - 1} {self.z + int(round(((self.size - 1) / 2)))}")
                w.build(wait=0)