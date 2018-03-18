# Mouse-autoconfiguration-linux
A simple python script for auto configuring extra mouse button on linux.

This python script utilizes xbindkeys, xautomation, and xdotool to configure mouse's extra button on linux.
The current version for button setting is for Logitech M705.
You can find the button numbers for the buttons on your mouse by the following steps.

## Find mouse button numbers
### Step 1
Install ```xev```
```
sudo apt-get install xev
```            
### Step 2
Run ```xev```. You will see a small white window. Move the mouse to the block and press the button which you want to check.
You will see the results like the following:
```
ButtonRelease event, serial 37, synthetic NO, window 0x4200001,
    root 0x100, subw 0x4200002, time 25443907, (24,48), root:(1407,100),
    state 0x100, button 1, same_screen YES
```   
The mouse button is 1.
