# benodigde librarys
import random
import pygame.mixer as mix
import time

# klaarzettem mp3 bestand
def blastthem():
    mix.init()
    sfx = "vine-boom.mp3"
    mix.music.load(sfx)
    mix.music.play()
    print("let it rip")

    while mix.music.get_busy():
        time.sleep(1)


for i in range(10):
    interval = random.randrange(60, 600)
    blastthem()
    time.sleep(interval)


