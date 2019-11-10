#! python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4

print('Searching...')                               
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))   # original request, not sure what the author is trying to do here
# res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))                               # makes more sense to me but gives somewhat different results
res.raise_for_status()

print(f'res.text = {res.text[5000:10000]}')         # help with debugging by printing out a chunk in the middle

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result. ------------------------------------------------------------------------------------------              
# NOTE: had to try a few different things and I'm not sure I got it right

# Attempt #1:
#linkElems = soup.select('.package-snippet')        # original eample claims that search result links appear to have the following form, but doesn't work for me:
                                                    # <a class="package -snippet" href="HYPERLINK "view-source:https://pypi.org/project/xml-parser/"/project/xml-parser/">

# Attempt #2:
#linkElems = soup.select('div.r > a')               # inspect element -> copy css selector gives selectors of the following form, but doesn't work for me:
                                                    # #rso > div:nth-child(4) > div > div:nth-child(1) > div > div > div.r > a
                                                    # #rso > div:nth-child(2) > div > div > div > div.r > a
                                                    # etc.

# Attempt #3:
linkElems = soup.select('li > a')                   # checking res.text shows some links of the following form, and that seems to work:
                                                    # <li class="yNFsl">
                                                    #   <a href="/search?q=https://pypi.org/search/%3Fq%3Dboring+stuff&amp;ie=UTF-8&amp;source=lnt&amp;tbs=qdr:d&amp;sa=X&amp;ved=0ahUKEwisgLn-sN_lAhVQIjQIHa9oBdMQpwUIEg"> 
                                                    #       Últimas 24 horas
                                                    #   </a>
                                                    # </li>

# ------------------------------------------------------------------------------------------------------------------------------

print(f'linkElems = {linkElems}')       # for debugging         

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)