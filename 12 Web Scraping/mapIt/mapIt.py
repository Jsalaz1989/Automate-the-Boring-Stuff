#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
# Usage: python mapIt.py [your_address_string] 
#    eg. python mapIt.py 870 Valencia St, San Francisco, CA 94110

import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line. 
    addressList = sys.argv[1:]          # sys.argv[0] is the program name, we don't want it
                                        # eg. addressList = ['mapIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco, ', 'CA', '94110'] 
    address = ' '.join(addressList)     # eg. address = '870 Valencia St, San Francisco, CA 94110' 

else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)