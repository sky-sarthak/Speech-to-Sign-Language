import record
import voice2text
import requests
import moviepy.editor as mp
import shutil
import os
import time
import urllib2
import goslate
from flask import Flask
app = Flask(__name__)

@app.route("/salil")
def main():
    file_name = "temp.wav"
    shutil.rmtree("data/")
    os.mkdir("data")
    
    record.record(file_name)
    
    import speech_to_text as stt
    #stt.system("/home/skysarthak/Documents/Project/speech_to_text.py")

    os.chdir("/home/skysarthak/Documents/Project (copy)/")
    with open('spoken.txt', 'r') as myfile:
    	spoken_text = myfile.read()
        
    list_words = [a.lower().strip("!,.?") for a in spoken_text.split()]

    with open('all_words.txt', 'r') as myfile:
    	words = myfile.read()
        
    lib = [a.lower().strip("!,.?") for a in words.split()]

    # read from local dataset
    for i,word in enumerate(list_words):
        if word in lib :
            f=mp.VideoFileClip("letters/" + word + ".mp4")
            f.write_videofile("data/%d.mp4" % i)
        else:
            letters = list(list_words[i])
            c = []
            for l in letters:
                if l.isalpha():
                    c.append(mp.VideoFileClip("letters/%s.mp4" % l).resize(height=320, width=240).speedx(factor=2))
            f = mp.concatenate_videoclips(c, method="compose")
            f.write_videofile("data/%d.mp4" % i)
            f.close()

    clips = []
    for j in range(len(list_words)):
        clips.append(mp.VideoFileClip("data/%d.mp4" % j).resize(height=320, width=240))
                
    final_clip = mp.concatenate_videoclips(clips, method="compose")

    final_clip.write_videofile("final_clip.mp4")
    time.sleep(1)
    os.system("xdg-open final_clip.mp4")
    return "final_clip.mp4"

#main()

if __name__ == "__main__":
	app.run(host='127.0.0.1',port=6789)
