#Enter the address in command line and run the script
#eg: python mapIt.py 'enter the address you want to find in Google maps'

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
webbrowser.open("https://www.google.com/maps/place/" + address)
