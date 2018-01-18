from __future__ import print_function
import time
import pychromecast
import sys
from gtts import gTTS
import os

cast = pychromecast.Chromecast('192.168.1.77')

#What to say?
text = str(sys.argv[1:])

# Wait for cast device to be ready
cast.wait()
print(cast.device)

#print(cast.status)


tts = gTTS(text=text, lang='en-us')

dirpath = os.getcwd()
print("asdasdasdas" + dirpath)
tts.save(dirpath + "/out.mp3")

mc = cast.media_controller
mc.play_media('http://192.168.1.216:8000/out.mp3', 'audio/mp3')
mc.block_until_active()
print(mc.status)

mc.pause()
time.sleep(5)
mc.play()
