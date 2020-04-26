import requests
import sys
from bs4 import BeautifulSoup

def imgextract(search):
    try:
        params = {"q": search}
        r = requests.get("http://www.bing.com/images/search", params=params)

        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find("a", {"class": "thumb"})

        #print(links.attrs["href"])
        with open("P:\Pvz_Program_Files\Web_Development\COVID\Python Scripts\img.txt",'w') as f:
            f.write(links.attrs["href"])

        #return(links.attrs["href"])

    except Exception:
        return "https://miro.medium.com/max/5000/1*Q33vwKNBXPxeOpmg9WPsrw.jpeg"

if len(sys.argv)>1:
    imgextract(sys.argv[1])
  


