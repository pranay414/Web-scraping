# Visit any website by just running this script
import sys, webbrowser

while True:
    print "Enter the address you want to open or type quit to stop:"
    address = raw_input()
    if address == 'quit' or address == 'Quit' or address == 'QUIT':
        exit()
    else:
        webbrowser.open(address)
        print "Opened:",address
