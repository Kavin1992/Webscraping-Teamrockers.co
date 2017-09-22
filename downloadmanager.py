import requests
from bs4 import BeautifulSoup
import re,os

url='https://teamrockers.co/downloads/index.php?p=1&sort=1&dir=Tamil%20Dubbed%20Movies/Jackie%20Chan%20Adventures%20Season%201%20Tamil%20Dubbed'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
html=requests.get(url)
soup=BeautifulSoup(html.content,'html5lib')
for link in soup.find_all('a'):
    lnk=link.get('href')
    #print(lnk)
    if re.search('mp4',lnk,re.MULTILINE):
        html1=requests.get(lnk)
        soup1=BeautifulSoup(html1.content,'html5lib')
        for link1 in soup1.find_all('a'):
            #print(link1.get('href'))
            if(link1.get('href').endswith('mp4')):
                fl_nm=os.path.basename(link1.get('href'))
                print("Writing to File",fl_nm)
                with open(fl_nm,'wb') as f:
                    r=requests.get(link1.get('href'),stream=True)
                    for chunk in r.iter_content(chunk_size=100000):
                        f.write(chunk)
                    print("Writing to File",fl_nm,"Finished")
                    f.close()
                break
        #print(lnk)
    #print(link.get('href'))
