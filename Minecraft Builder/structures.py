import pyautogui
import time
import random

class Mining:
    def __init__(self, startPoint : str):
        self.x, self.y, self.z = startPoint.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 1, int(self.z)

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(ms)

    def buildFissure(self, width : int = 4, length : int = None, digging_height : int = 16):
        self.width = width
        self.w1 = int(self.width // 2)
        self.w2 = int(self.width - self.w1)

        if length == None:
            self.length = (self.y - 10) * 2
        else:
            self.length = length

        for x in range(5):
            print(f"Mine creating is starting in {5 - x} sec...")
            time.sleep(1)

        if self.y <= 30:
            print("I can't mine that!")
        else:
            for i in range(0, self.y - digging_height):
                self.write(f"/fill {self.x - (self.w1 - 1)} {self.y - i} {self.z - (int(self.length / 2) - 1)} {self.x + self.w2} {self.y + 2 - i} {self.z + int(round(self.length / 2))} air")
            
            for i in range(digging_height, 9, -1):
                self.write(f"/fill {self.x - (self.w1 - 1)} {i} {self.z - (int(self.length / 2) - 1)} {self.x + self.w2} {i} {self.z + int(round(self.length / 2))} air 0 destroy", ms=0.3)
            print("Done!")

    def build(self):
        for x in range(5):
            print(f"Mine creating is starting in {5 - x} sec...")
            time.sleep(1)

        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + 1} {self.y} {self.z + 3} cobblestone")
        self.write(f"/fill {self.x} {self.y + 1} {self.z} {self.x + 1} {self.y + 1} {self.z + 2} cobblestone")
        self.write(f"/fill {self.x} {self.y + 2} {self.z} {self.x + 1} {self.y + 2} {self.z + 1} cobblestone")
        self.write(f"/fill {self.x} {self.y + 3} {self.z} {self.x + 1} {self.y + 3} {self.z} cobblestone")

        self.write(f"/fill {self.x - 1} {self.y} {self.z} {self.x - 1} {self.y} {self.z + 1} cobblestone")
        self.write(f"/fill {self.x + 2} {self.y} {self.z} {self.x + 2} {self.y} {self.z + 1} cobblestone")
        

        self.write(f"/setblock {self.x - 1} {self.y + 1} {self.z} cobblestone")
        self.write(f"/setblock {self.x - 1} {self.y + 2} {self.z} cobblestone")
        self.write(f"/setblock {self.x + 2} {self.y + 1} {self.z} cobblestone")
        self.write(f"/setblock {self.x + 2} {self.y + 2} {self.z} cobblestone")

        self.write(f"/setblock {self.x - 1} {self.y + 1} {self.z + 1} cobblestone")
        self.write(f"/setblock {self.x + 2} {self.y + 1} {self.z + 1} cobblestone")

        self.write(f"/setblock {self.x - 1} {self.y} {self.z + 2} cobblestone")
        self.write(f"/setblock {self.x + 2} {self.y} {self.z + 2} cobblestone")

        self.write(f"/setblock {self.x} {self.y - 1} {self.z} cobblestone")
        self.write(f"/setblock {self.x + 1} {self.y - 1} {self.z} cobblestone")

        self.write(f"/setblock {self.x - 1} {self.y + 1} {self.z - 1} torch 4")
        self.write(f"/setblock {self.x + 2} {self.y + 1} {self.z - 1} torch 4")

        if self.y <= 20:
            print("I can't mine that!")
        else:
            for i in range(0, self.y - 9):
                self.write(f"/fill {self.x} {self.y - i} {self.z + i} {self.x + 1} {self.y + 2 - i} {self.z + i} air 0 destroy")
                if i % 8 == 0 and i != 0:
                    self.write(f"/setblock {self.x} {self.y - i} {self.z + i} torch")
                    self.write(f"/setblock {self.x + 1} {self.y - i} {self.z + i} torch")

            self.write(f"/setblock {self.x} {self.y + 2} {self.z} cobblestone")
            self.write(f"/setblock {self.x + 1} {self.y + 2} {self.z} cobblestone")
        
            # Door

            pyautogui.press("t")
            pyautogui.write(f"/setblock {self.x} {self.y} {self.z} wooden_door 4")
            pyautogui.press("enter")
            time.sleep(0.1)

            pyautogui.press("t")
            pyautogui.write(f"/setblock {self.x} {self.y + 1} {self.z} wooden_door 8")
            pyautogui.press("enter")
            time.sleep(0.1)

            pyautogui.press("t")
            pyautogui.write(f"/setblock {self.x + 1} {self.y} {self.z} wooden_door 6")
            pyautogui.press("enter")
            time.sleep(0.1)

            pyautogui.press("t")
            pyautogui.write(f"/setblock {self.x + 1} {self.y + 1} {self.z} wooden_door 9")
            pyautogui.press("enter")
            time.sleep(0.1)

class Aquarium:
    def __init__(self, startPoint : str, side_length : int = 10, summonCount : int = None):
        self.x, self.y, self.z = startPoint.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y), int(self.z)
        self.side_length = side_length
        if summonCount == None:
            self.summonCount = int(round(side_length / 2))
        else:
            self.summonCount = summonCount

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(ms)

    def build(self):
        for x in range(5):
            print(f"Aquarium creating is starting in {5 - x} sec...")
            time.sleep(1)

        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + self.side_length - 1} {self.y + int(round(self.side_length / 2))} {self.z + int(round(self.side_length / 2))} glass")
        self.write(f"/fill {self.x + 1} {self.y + 1} {self.z + 1} {self.x + self.side_length - 2} {self.y + int(round(self.side_length / 2)) + 1} {self.z + int(round(self.side_length / 2)) - 1} air")
        self.write(f"/fill {self.x + 1} {self.y + 1} {self.z + 1} {self.x + self.side_length - 2} {self.y + int(round(self.side_length / 2))} {self.z + int(round(self.side_length / 2)) - 1} water")
        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + self.side_length - 1} {self.y} {self.z + int(round(self.side_length / 2))} cobblestone")
        self.write(f"/fill {self.x + 1} {self.y} {self.z + 1} {self.x + self.side_length - 2} {self.y} {self.z + int(round(self.side_length / 2)) - 1} glowstone")
        self.write(f"/fill {self.x} {self.y + int(round(self.side_length / 2)) + 1} {self.z} {self.x + self.side_length - 1} {self.y + int(round(self.side_length / 2)) + 1} {self.z + int(round(self.side_length / 2))} cobblestone")
        self.write(f"/fill {self.x + 1} {self.y + int(round(self.side_length / 2)) + 1} {self.z + 1} {self.x + self.side_length - 2} {self.y + int(round(self.side_length / 2)) + 1} {self.z + int(round(self.side_length / 2)) - 1} glowstone")
        
        for i in range (self.summonCount):
            self.write(f"/summon squid {self.x + int(round(self.side_length / 2))} {self.y + int(round(self.side_length / 4))} {self.z + int(round(self.side_length / 4))}")

class Farm:
    def __init__(self, startPoint : str, double : bool = False):
        self.x, self.y, self.z = startPoint.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 1, int(self.z)
        self.double = double

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(ms)

    def build(self):
        for x in range(5):
            print(f"Farm creating is starting in {5 - x} sec...")
            time.sleep(1)

        if not self.double:
            self.write(f"/fill {self.x} {self.y} {self.z} {self.x + 6} {self.y} {self.z + 8} cobblestone")
            self.write(f"/fill {self.x + 1} {self.y} {self.z + 1} {self.x + 5} {self.y} {self.z + 7} farmland")
            self.write(f"/fill {self.x + 3} {self.y} {self.z + 1} {self.x + 3} {self.y} {self.z + 7} water")
        else:
            self.write(f"/fill {self.x} {self.y} {self.z} {self.x + 12} {self.y} {self.z + 8} cobblestone")
            self.write(f"/fill {self.x + 1} {self.y} {self.z + 1} {self.x + 11} {self.y} {self.z + 7} water")
            self.write(f"/fill {self.x + 1} {self.y} {self.z + 1} {self.x + 2} {self.y} {self.z + 7} farmland")
            self.write(f"/fill {self.x + 4} {self.y} {self.z + 1} {self.x + 5} {self.y} {self.z + 7} farmland")
            self.write(f"/fill {self.x + 7} {self.y} {self.z + 1} {self.x + 8} {self.y} {self.z + 7} farmland")
            self.write(f"/fill {self.x + 10} {self.y} {self.z + 1} {self.x + 11} {self.y} {self.z + 7} farmland")
            self.write(f"/fill {self.x + 6} {self.y} {self.z + 1} {self.x + 6} {self.y} {self.z + 7} cobblestone")

class MobFarm:
    def __init__(self,startPoint : str, mob : str, count : int = 5):
        self.x, self.y, self.z = startPoint.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 1, int(self.z)
        self.mob = mob
        self.count = count

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(ms)
    
    def build(self):
        for x in range(5):
            print(f"Mob Farm creating is starting in {5 - x} sec...")
            time.sleep(1)
        
        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + 3} {self.y + 4} {self.z + 3} glass")
        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + 3} {self.y} {self.z + 3} glowstone")
        self.write(f"/fill {self.x} {self.y + 4} {self.z} {self.x + 3} {self.y + 4} {self.z + 3} glowstone")
        self.write(f"/fill {self.x + 1} {self.y + 1} {self.z + 1} {self.x + 2} {self.y + 3} {self.z + 2} water")

        for i in range(self.count):
            self.write(f"/summon {self.mob} {self.x + 1.5} {self.y + 1.5} {self.z + 1.5}")

        pyautogui.press("t")
        pyautogui.write(f"/kill ")
        pyautogui.hotkey('altright','q')
        pyautogui.write(f"e[type={self.mob}]")
        pyautogui.press("enter")
        time.sleep(0.1)

        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + 3} {self.y + 4} {self.z + 3} air")

class Tree:
    def __init__(self, location : str):
        self.location = location
        self.x, self.y, self.z = self.location.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 1, int(self.z)

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        pyautogui.press("enter")
        time.sleep(ms)

    def build(self, wait : int = 5):
        for x in range(wait):
            print(f"Tree creating is starting in {wait - x} sec...")
            time.sleep(1)

        length = random.randint(4, 8) - 1
        self.write(f"/fill {self.x} {self.y} {self.z} {self.x} {self.y + length} {self.z} log")
        self.write(f"/setblock {self.x + 1} {self.y + length} {self.z} leaves 0 keep")
        self.write(f"/setblock {self.x - 1} {self.y + length} {self.z} leaves 0 keep")
        self.write(f"/setblock {self.x} {self.y + length} {self.z + 1} leaves 0 keep")
        self.write(f"/setblock {self.x} {self.y + length} {self.z - 1} leaves 0 keep")
        self.write(f"/fill {self.x - 2} {self.y + length + 1} {self.z - 2} {self.x + 2} {self.y + length + 2} {self.z + 2} leaves 0 keep")
        self.write(f"/fill {self.x - 1} {self.y + length + 3} {self.z - 1} {self.x + 1} {self.y + length + 3} {self.z + 1} leaves 0 keep")

class Writing:
    # Towards -Z
    def __init__(self, startPoint : str, sentence : str = "CODE BY OZYBO"):
        self.x, self.y, self.z = startPoint.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 4, int(self.z)
        self.sentence = sentence

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        pyautogui.press("enter")
        time.sleep(ms)

    def build(self):
        import letters
        for x in range(5):
            print(f"Writing creating is starting in {5 - x} sec...")
            time.sleep(1)

        self.height, self.width = 7, 7 * len(self.sentence)
        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + self.width} {self.y + self.height} {self.z + 1} wool")
        self.offset = 0
        for i in range(len(self.sentence)):
            self.write(f"/fill {self.x + 1 + self.offset} {self.y + 1} {self.z + 1} {self.x + 1 + self.offset + 5} {self.y + self.height - 1} {self.z + 1} air")
            self.offset += 7

        self.offset = 0
        self.stepX = 0
        self.stepY = 0
        for letter in self.sentence:
            for bitlist in letters.get(letter)[::-1]: # [[0,0,0], [1,1,1], [1,0,1]]
                for bit in bitlist: # [1,1,1]
                    if bit == 1:
                        self.write(f"/setblock {self.x + 1 + self.offset + self.stepX} {self.y + 1 + self.stepY} {self.z + 1} wool 15", ms=0.01)
                    self.stepX += 1
                self.stepY += 1
                self.stepX = 0
            self.offset += 7
            self.stepY = 0
            self.stepX = 0

class Market:
    def __init__(self, location : str) -> None:
        self.location = location
        self.x, self.y, self.z = self.location.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 1, int(self.z)

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        pyautogui.press("enter")
        time.sleep(ms)
    
    def build(self, wait: int = 5):
        for x in range(wait):
            print(f"Market creating is starting in {wait - x} sec...")
            time.sleep(1)

        self.write(f"/setblock {self.x - 1} {self.y} {self.z - 1} stone 6")
        self.write(f"/setblock {self.x + 1} {self.y} {self.z + 1} stone 6")
        self.write(f"/setblock {self.x + 1} {self.y} {self.z - 1} stone 6")
        self.write(f"/setblock {self.x - 1} {self.y} {self.z + 1} stone 6")

        self.write(f"/setblock {self.x - 2} {self.y} {self.z - 2} torch")
        self.write(f"/setblock {self.x + 2} {self.y} {self.z + 2} torch")
        self.write(f"/setblock {self.x + 2} {self.y} {self.z - 2} torch")
        self.write(f"/setblock {self.x - 2} {self.y} {self.z + 2} torch")

        self.write(f"/setblock {self.x - 1} {self.y} {self.z} stone_slab 13")
        self.write(f"/setblock {self.x + 1} {self.y} {self.z} stone_slab 13")
        self.write(f"/setblock {self.x} {self.y} {self.z + 1} stone_slab 13")
        self.write(f"/setblock {self.x} {self.y} {self.z - 1} stone_slab 13")

        self.write(f"/setblock {self.x - 1} {self.y + 1} {self.z - 1} fence")
        self.write(f"/setblock {self.x + 1} {self.y + 1} {self.z + 1} fence")
        self.write(f"/setblock {self.x + 1} {self.y + 1} {self.z - 1} fence")
        self.write(f"/setblock {self.x - 1} {self.y + 1} {self.z + 1} fence")

        self.write(f"/fill {self.x - 1} {self.y + 2} {self.z - 1} {self.x + 1} {self.y + 2} {self.z + 1} stone_slab 5")

        self.write(f"/summon villager {self.x} {self.y} {self.z}")
        
class Well:
    def __init__(self, startPoint : str):
        self.x, self.y, self.z = startPoint.split(" ")
        self.x, self.y, self.z = int(self.x), int(self.y) + 1, int(self.z)

    def write(self, text : str, ms : float = 0.1):
        pyautogui.press("t")
        pyautogui.write(text)
        pyautogui.press("enter")
        time.sleep(ms)

    def build(self, wait : int = 5):
        for x in range(wait):
            print(f"Well creating is starting in {wait - x} sec...")
            time.sleep(1)

        self.write(f"/fill {self.x} {self.y} {self.z} {self.x + 3} {self.y - 1} {self.z - 3} cobblestone")
        self.write(f"/fill {self.x + 1} {self.y} {self.z - 1} {self.x + 2} {self.y} {self.z - 2} {random.choice(['water', 'water', 'water', 'water', 'lava', 'water', 'water', 'water', 'water', 'water'])}")
        self.write(f"/fill {self.x} {self.y + 1} {self.z} {self.x} {self.y + 2} {self.z} fence")
        self.write(f"/fill {self.x + 3} {self.y + 1} {self.z} {self.x + 3} {self.y + 2} {self.z} fence")
        self.write(f"/fill {self.x} {self.y + 1} {self.z - 3} {self.x} {self.y + 2} {self.z - 3} fence")
        self.write(f"/fill {self.x + 3} {self.y + 1} {self.z - 3} {self.x + 3} {self.y + 2} {self.z - 3} fence")
        self.write(f"/fill {self.x} {self.y + 3} {self.z} {self.x + 3} {self.y + 3} {self.z - 3} cobblestone")
        self.write(f"/setblock {self.x - 1} {self.y} {self.z + 1} torch")
        self.write(f"/setblock {self.x + 4} {self.y} {self.z + 1} torch")
        self.write(f"/setblock {self.x - 1} {self.y} {self.z - 4} torch")
        self.write(f"/setblock {self.x + 4} {self.y} {self.z - 4} torch")
