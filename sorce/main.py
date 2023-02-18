import json
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

#load config file
try:
    f = open('config.json')
    config = json.load(f)
    f.close() 
except:
    print("Error while loading config.json")
    i = input("Press enter to exit")
    quit()

#Load curent file
try:
    with open(config["Game_Output_path"], "r") as f:
        oldLevel = f.read()
except:
    print("Error while loading game output file. Have you filed in the 'Game_Output_path' corectly?")
    i = input("Press enter to exit")
    quit()


#I know this is ugly but it works
if(len(config["split_key"]) == 1):
    k = config["split_key"]
else:
    if(config["split_key"] == "f24"):
        k = Key.f24
    elif(config["split_key"] == "f12"):
        k = Key.f12
    elif(config["split_key"] == "f11"):
        k = Key.f11
    elif(config["split_key"] == "f10"):
        k = Key.f10
    elif(config["split_key"] == "f9"):
        k = Key.f9
    elif(config["split_key"] == "f8"):
        k = Key.f8
    elif(config["split_key"] == "f7"):
        k = Key.f7
    elif(config["split_key"] == "f6"):
        k = Key.f6
    elif(config["split_key"] == "f5"):
        k = Key.f5
    elif(config["split_key"] == "f4"):
        k = Key.f4
    elif(config["split_key"] == "f3"):
        k = Key.f3
    elif(config["split_key"] == "f2"):
        k = Key.f2
    elif(config["split_key"] == "f1"):
        k = Key.f1
    else:
        print("ERROR invalide keycode!!!")
        i = input("Press enter to exit")
        quit()


#Main loop
print("Running!")
while True:
    time.sleep(1/config["pull_Rate"]) #Sets the pull rate

    with open(config["Game_Output_path"], "r") as f:
        data = f.read()
        if(data != oldLevel):
            oldLevel = data
            print("Next level! " + oldLevel)


            #Press split key
            keyboard.press(k)
            time.sleep(0.1)
            keyboard.release(k)