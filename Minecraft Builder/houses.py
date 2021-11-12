import pyautogui
import time

class House1:
    def __init__(self, location : str):
        self.x, self.y, self.z = location.split(" ")
        self.stoneLocationsV = [
            [f"{self.x} {self.y} {self.z}", f"{self.x} {int(self.y) + 5} {self.z}"],
            [f"{int(self.x) + 9} {self.y} {self.z}", f"{int(self.x) + 9} {int(self.y) + 5} {self.z}"],
            [f"{self.x} {self.y} {int(self.z) - 9}", f"{self.x} {int(self.y) + 5} {int(self.z) - 9}"],
            [f"{int(self.x) + 9} {self.y} {int(self.z) - 9}", f"{int(self.x) + 9} {int(self.y) + 5} {int(self.z) - 9}"]
        ]

        self.stoneLocationsH = [
            [f"{self.x} {int(self.y) + 6} {self.z}", f"{int(self.x) + 9} {int(self.y) + 6} {self.z}"],
            [f"{int(self.x) + 9} {int(self.y) + 6} {self.z}", f"{int(self.x) + 9} {int(self.y) + 6} {int(self.z) - 9}"],
            [f"{int(self.x) + 9} {int(self.y) + 6} {int(self.z) - 9}", f"{self.x} {int(self.y) + 6} {int(self.z) - 9}"],
            [f"{self.x} {int(self.y) + 6} {int(self.z) - 9}", f"{self.x} {int(self.y) + 6} {self.z}"],
            [f"{self.x} {int(self.y)} {self.z}", f"{int(self.x) + 9} {int(self.y)} {self.z}"],
            [f"{int(self.x) + 9} {int(self.y)} {self.z}", f"{int(self.x) + 9} {int(self.y)} {int(self.z) - 9}"],
            [f"{int(self.x) + 9} {int(self.y)} {int(self.z) - 9}", f"{self.x} {int(self.y)} {int(self.z) - 9}"],
            [f"{self.x} {int(self.y)} {int(self.z) - 9}", f"{self.x} {int(self.y)} {self.z}"]
        ]

        self.fillArea = [
            [f"{int(self.x) + 1} {self.y} {int(self.z) - 1}", f"{int(self.x) + 8} {self.y} {int(self.z) - 8}"],
            [f"{int(self.x) + 1} {int(self.y) + 1} {self.z}", f"{int(self.x) + 8} {int(self.y) + 5} {self.z}"],
            [f"{int(self.x) + 9} {int(self.y) + 1} {int(self.z) - 1}", f"{int(self.x) + 9} {int(self.y) + 5} {int(self.z) - 8}"],
            [f"{int(self.x) + 1} {int(self.y) + 1} {int(self.z) - 9}", f"{int(self.x) + 8} {int(self.y) + 5} {int(self.z) - 9}"],
            [f"{int(self.x)} {int(self.y) + 1} {int(self.z) - 1}", f"{int(self.x)} {int(self.y) + 5} {int(self.z) - 8}"],
            [f"{int(self.x) + 1} {int(self.y) + 6} {int(self.z) - 1}", f"{int(self.x) + 8} {int(self.y) + 6} {int(self.z) - 8}"]
        ]

        self.glasses = [
            [f"{int(self.x) + 9} {int(self.y) + 2} {int(self.z) - 2}", f"{int(self.x) + 9} {int(self.y) + 4} {int(self.z) - 7}"],
            [f"{int(self.x)} {int(self.y) + 2} {int(self.z) - 2}", f"{int(self.x)} {int(self.y) + 4} {int(self.z) - 7}"],
            [f"{int(self.x) + 2} {int(self.y) + 2} {int(self.z) - 9}", f"{int(self.x) + 7} {int(self.y) + 4} {int(self.z) - 9}"]
        ]

    def create(self, wait : int = 5):
        for x in range(wait):
            print(f"House1 creating is starting in {wait - x} sec...")
            time.sleep(1)

        for i, j in self.stoneLocationsV:

            pyautogui.press("t")
            pyautogui.write(f"/fill {i} {j} cobblestone")
            pyautogui.press("enter")
            time.sleep(0.1)

        for i, j in self.stoneLocationsH:

            pyautogui.press("t")
            pyautogui.write(f"/fill {i} {j} cobblestone")
            pyautogui.press("enter")
            time.sleep(0.1)

        for i, j in self.fillArea:

            pyautogui.press("t")
            pyautogui.write(f"/fill {i} {j} planks")
            pyautogui.press("enter")
            time.sleep(0.1)

        for i, j in self.glasses:

            pyautogui.press("t")
            pyautogui.write(f"/fill {i} {j} glass")
            pyautogui.press("enter")
            time.sleep(0.1)

        # Door

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 4} {int(self.y) + 1} {self.z} wooden_door")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 4} {int(self.y) + 2} {self.z} wooden_door 8")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 5} {int(self.y) + 1} {self.z} wooden_door")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 5} {int(self.y) + 2} {self.z} wooden_door 9")
        pyautogui.press("enter")
        time.sleep(0.1)

        # Torch

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 1} {int(self.y) + 4} {int(self.z) - 1} torch 4")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 8} {int(self.y) + 4} {int(self.z) - 1} torch 4")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 1} {int(self.y) + 4} {int(self.z) - 8} torch 3")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 8} {int(self.y) + 4} {int(self.z) - 8} torch 3")
        pyautogui.press("enter")
        time.sleep(0.1)

        # Chest

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 4} {int(self.y) + 1} {int(self.z) - 8} chest 3")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 5} {int(self.y) + 1} {int(self.z) - 8} chest 3")
        pyautogui.press("enter")
        time.sleep(0.1)

        # Bed 1

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 1} {int(self.y) + 1} {int(self.z) - 8} bed 10")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 1} {int(self.y) + 1} {int(self.z) - 7} bed 2")
        pyautogui.press("enter")
        time.sleep(0.1)

        # Bed 2

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 8} {int(self.y) + 1} {int(self.z) - 8} bed 10")
        pyautogui.press("enter")
        time.sleep(0.1)

        pyautogui.press("t")
        pyautogui.write(f"/setblock {int(self.x) + 8} {int(self.y) + 1} {int(self.z) - 7} bed 2")
        pyautogui.press("enter")
        time.sleep(0.1)

