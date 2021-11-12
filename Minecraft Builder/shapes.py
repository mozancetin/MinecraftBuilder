import pyautogui
import time

class Cube:
    def __init__(self, material : str, side_length : int, startPoint : str):
        self.material = material
        self.side_length = side_length - 1
        self.startPoint = startPoint
        self.x, self.y, self.z = self.startPoint.split(" ")

    def build(self):
        self.startPoints = [f"{self.x} {self.y} {self.z}", f"{self.x} {self.y} {self.z}", f"{self.x} {self.y} {self.z}", f"{int(self.x) + self.side_length} {self.y} {int(self.z) + self.side_length}", f"{int(self.x) + self.side_length} {self.y} {int(self.z) + self.side_length}", f"{self.x} {int(self.y) + self.side_length} {self.z}"]
        self.endPoints = [f"{self.x} {int(self.y) + self.side_length} {int(self.z) + self.side_length}", f"{int(self.x) + self.side_length} {self.y} {int(self.z) + self.side_length}", f"{int(self.x) + self.side_length} {int(self.y) + self.side_length} {self.z}", f"{self.x} {int(self.y) + self.side_length} {int(self.z) + self.side_length}", f"{int(self.x) + self.side_length} {int(self.y) + self.side_length} {self.z}", f"{int(self.x) + self.side_length} {int(self.y) + self.side_length} {int(self.z) + self.side_length}"]

        for x in range(5):
            print(f"Cube creating is starting in {5 - x} sec...")
            time.sleep(1)

        for i, j in zip(self.startPoints, self.endPoints):
            pyautogui.press("t")
            pyautogui.write(f"/fill {i} {j} {self.material}")
            pyautogui.press("enter")
            time.sleep(0.5)

        self.x = str(int(self.x) + 1)
        self.y = str(int(self.y) + 1)
        self.z = str(int(self.z) + 1)
        self.startPoint = f"{self.x} {self.y} {self.z}"
        self.side_length -= 2
        self.clear(wait=0)

    def buildFilled(self, wait : int = 5):
        for x in range(wait):
            print(f"Filled cube creating is starting in {wait - x} sec...")
            time.sleep(1)

        pyautogui.press("t")
        pyautogui.write(f"/fill {self.startPoint} {int(self.x) + self.side_length} {int(self.y) + self.side_length} {int(self.z) + self.side_length} {self.material}")
        pyautogui.press("enter")
        time.sleep(0.5)

    def clear(self, wait : int = 5):
        self.temp = self.material
        self.material = "air"
        self.buildFilled(wait=wait)
        self.material = self.temp
        del self.temp

class Pyramid:
    def __init__(self, material : str, side_length : int, startPoint : str):
        self.material = material
        self.side_length = side_length - 1
        self.startPoint = startPoint
        self.x, self.y, self.z = self.startPoint.split(" ")

    def buildFilled(self):
        self.startPoints = []
        self.endPoints = []
        for i in range(0, int(self.side_length//2) + 1):
            self.startPoints.append(f"{int(self.x) + i} {int(self.y) + i} {int(self.z) + i}")
            self.endPoints.append(f"{int(self.x) + self.side_length - i} {int(self.y) + i} {int(self.z) + self.side_length - i}")

        for x in range(5):
            print(f"Pyramid creating is starting in {5 - x} sec...")
            time.sleep(1)

        for i, j in zip(self.startPoints, self.endPoints):
            pyautogui.press("t")
            pyautogui.write(f"/fill {i} {j} {self.material}")
            pyautogui.press("enter")
            time.sleep(0.5)

    def clear(self):
        self.temp = self.material
        self.material = "air"
        self.buildFilled()
        self.material = self.temp
        del self.temp

