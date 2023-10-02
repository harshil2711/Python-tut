import pyttsx3
i = 0
li = ['tom' , 'cruise' , 'simaran']
engine = pyttsx3.init()
for i in range(len(li)):
    engine.say(f"shout out to {li[i]}")
engine.runAndWait()
