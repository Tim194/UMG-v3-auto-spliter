# UMG-v3-auto-spliter
an auto splitter for Untitled Magnet Game v3
Only works on windows at the moment

## How to install
To install the auto splitter you will need to install a mod for UMG and also run a "translation layer" between UMG and live split.
Video tutorial: https://youtu.be/dstxDy5KQAA 
### Install UMG mod
1. Open your UMG v3 install folder
2. Go to /Untitled Magnet Game_Data/Managed/
3. Replace the "Assembly-CSharp.dll" with the modified "Assembly-CSharp.dll" found in this repository
4. Run the game and complete at least one level. The first one is fine.

### Configure the "translation layer"
1. Press win + r and type %appdata%
2. Go back one folder. You should see a LocalLow folder
3. Go to /LocalLow/GMTK/Untitled Magnet Game/ there should be a level.txt file there. If not make sure you installed the mod correctly and completed at least one level with the mod installed. Your path should look something like C:/Users<userName>/AppData/LocalLow/GMTK/Untitled Magnet Game
4. copy the path for the level.txt file
5. Go to the files you downloaded from this repository and open the config.json
6. Past the path to the level.txt file in the "Game_Output_path" filed and add /level.txt at the end. It should look somthing like this C:/Users<userName>/AppData/LocalLow/GMTK/Untitled Magnet Game/level.txt !!!INPORTANT!!! You NEED to change all the \ to / othervise it wont work
7. Change the split_key to the key you configured live split to use. See below which keys you can use.

### Accepted split_key
* All singel leter keys such like "a", "b", "c"
* "f1" to "f12" and "f24"
