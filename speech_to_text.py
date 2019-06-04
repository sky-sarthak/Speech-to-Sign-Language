import os
import speech_recognition as sr 

  

AUDIO_FILE = ("temp.wav") 

  
# use the audio file as the audio source 

  

r = sr.Recognizer() 

  
with sr.AudioFile(AUDIO_FILE) as source: 

    #reads the audio file. Here we use record instead of 

    #listen 

    audio = r.record(source)   

    

try:
    
    os.chdir("/home/skysarthak/Documents/Project (copy)/")
    spoken = r.recognize_google(audio)

    print("The audio file contains: " + spoken) 

    f = open( 'spoken.txt', 'w' )
    f.write( repr(spoken) + '\n' )
    f.close()

except sr.UnknownValueError: 

    print("Google Speech Recognition could not understand audio") 

  

except sr.RequestError as e: 

    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

