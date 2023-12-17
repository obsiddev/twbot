# typewriter bot

# tutorial: zuerst ausführn, dann des fenster mit der typewriter übung (schon in der übung)
# des hast es muss so a fenster dastehen mit "press any key to start"
# öffnen, dann space druckn, dann müssts eig funktioniern
# wenn nit bin i dumm

import keyboard
import time
import os
import random

os.system("cls")
print("running")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i" ,"j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

lesson = "fortnite fortnite fortnite fornite fortnite fortnite fortnite" # test lesson

wpm = 3600# wörter pro minutn

error_prob = 1 # fehlerwahrscheinlichkeit in prozent, nur ganze zahlen -1 = keine fehler, 0 = was i nit

errorcnt = 0

keyboard.wait("space")

for i in range(100):
    for i in range(len(lesson)):
        if (random.randint(0,100) <= error_prob):
            keyboard.write(random.choice(letters))
            errorcnt = errorcnt + 1
        else:
            keyboard.write(lesson[i])
        time.sleep(60/wpm)
    
    keyboard.write("  /errors: " + str(errorcnt))
    errorcnt = 0
    keyboard.send("enter")
    keyboard.send("space")