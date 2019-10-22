# MapIT - script for quick searching map locations

import webbrowser, sys, pyperclip

webbrowser.open('https://automatetheboringstuff.com') #opens default webbrowser

sys.argv #['mapit.py','870','Valencia','St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    #['mapit.py','870','Valencia','St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://google.com/maps/place<ADDRESS>
webbrowser.open('https://www.google.com/maps/place' + address)
