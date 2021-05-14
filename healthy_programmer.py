from pygame import mixer
from datetime import datetime
from time import time
mixer.init()
b=input("if you want to stop reminder press S, else if you want to continue hit enter")
def musiconloop(file,stopper):
    mixer.init()

    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg},{datetime.now()}\n")
if __name__=='__main__':
    # musiconloop('water.mp3',"stop")
    init_water= time()
    init_eyes= time()
    init_exercise= time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs =45*60


    while True:
        if time() -init_water > watersecs:
            mixer.music.load("water.mp3")
            mixer.music.play()
            print("water drinking time enter 'drank' to stop alarm")
            musiconloop('water.mp3','drank')
            init_water= time()
            log_now("drank water at")


        if time() -init_eyes > eyessecs:
            mixer.music.load("eyes.mp3")
            mixer.music.play()
            print("eyes relaxing time enter 'done' to stop alarm")
            musiconloop('eyes.mp3','done')
            init_eyes= time()
            log_now("eyes relaxed at")



        if time() -init_exercise > exsecs:
            mixer.music.load("physical.mp3")
            mixer.music.play()
            print("physical exercises time enter 'done' to stop alarm")
            musiconloop('exercises.mp3','done')
            init_exercise= time()
            log_now("physical exercises done at")
        if b=="s":
            break

