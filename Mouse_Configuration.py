#! /usr/bin/python3
import os


# install xbindkeys, xautomation, xdotool 
os.system("sudo apt-get install xbindkeys xautomation xdotool")

# Create xbindkeys config file
os.system("xbindkeys --defaults > $HOME/.xbindkeysrc")

# Read in Mouse Setting
fo = open('Mouse_Setting','r')
command = fo.read()

fi = open('$Home/.xbindkeysrc','w+')
fi.write(command)

os.system("/usr/bin/xbindkeys_autostart autostart")
