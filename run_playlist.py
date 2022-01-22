import os
import random
import time

MUSIC_DIR = "playlist/"

run_forever = True
while run_forever == True:
    musicList = os.listdir(MUSIC_DIR)
    fileCount = len(musicList)
    random.shuffle(musicList)

    i = 0
    while i < fileCount:
        if musicList[i].find('.mp3') < 0:
            continue

        cmd = "sox \"" + MUSIC_DIR + musicList[i] + "\" -r 22050 -c 1 -b 16 -t wav current_music.wav"
        print(cmd)
        os.system(cmd)

        cmd = "sudo ./fm_transmitter/fm_transmitter -f 101.0 current_music.wav"
        print(cmd)
        os.system(cmd)
        time.sleep(1)
        i += 1

