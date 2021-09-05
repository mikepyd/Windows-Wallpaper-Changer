import os
import sys
import ctypes
import random
import time

   


def wpc():

    while True:

        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        for root, directories, files in os.walk(os.path.join(path, 'wallpapers')):
           wallpapers = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]

        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(path, 'wallpapers', random.choice(wallpapers)) , 0)

        time.sleep(1800)

wpc()

