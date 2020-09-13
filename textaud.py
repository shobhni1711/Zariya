from gtts import gTTS
import os

def audio_feature(word):
	language = 'en'
	output = gTTS(text=word, lang=language, slow=False)
	output.save("output.mp3")
	os.system("start output.mp3")
   
    
    

    