import shutil
import os
  
# use the audio file as the audio source 

shutil.copy2('/home/skysarthak/Documents/Project (copy)/temp.wav', '/home/skysarthak/Documents/Project (copy)/cheetah-master/demo/python/temp.wav')

os.chdir("/home/skysarthak/Documents/Project (copy)/cheetah-master/demo/python")

os.system('ffmpeg -i temp.wav -acodec pcm_s16le -ac 1 -ar 16000 test.wav')

os.system('python cheetah_demo.py --audio_paths test.wav')
