import os
import shutil
import time
from pygame import mixer


def Desktop():
    os.chdir(r"/home/wario/Escritorio")

mixer.init()
bark = mixer.Sound("/home/wario/Escritorio/warioo/proyectos/Bark/bark.mp3")

# Set up the name of the files that we want in our desktop
allow_files = ("warioo", "Mario", "Basura")

Desktop()

# Get the path of the desktop
path = os.getcwd()
new_path = "/home/wario/Escritorio/Basura"

while True:

    files = os.listdir()
    for file in files:
        if file not in allow_files:
            old_path_file = path + '/' + file
            new_path_file = new_path + '/' + file
            shutil.move(old_path_file, new_path_file)
            
            bark.play()
            time.sleep(2)
            
    # Do this every 30 minutes
    time.sleep(1800)
