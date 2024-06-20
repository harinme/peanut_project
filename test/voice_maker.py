from gtts import gTTS 

def speak(text): 
   tts = gTTS(text=text, lang='ko') 
   tts.save('voice3.mp3') 

speak("3개 불량")