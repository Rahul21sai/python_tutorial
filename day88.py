
#for mac
# from os import system
# names = ["rahul","rohan","javed"]
# for name in names:
#     system(f"say{name}")
    #for windows

import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

list = ["rahul","rohan","javed"]

for i in list:
    print("shoutout to "+i)

for name in list:
    names  = name.split()
    shoutout = f"shoutout to {names[0]}"
    speaker.Speak(shoutout)
print("shoout of all for guys")
