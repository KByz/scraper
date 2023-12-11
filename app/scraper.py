"""
Import requests and import BeautifulSoup from bs4

"""
import requests
from bs4 import BeautifulSoup

def scrapePage():
    """
    Create function to retreive url of web page to scrape
    """
    pageToScrape = requests.get("https://www.facebook.com/Blizzard.ANZ/posts/pfbid02Vojf98tp6cVuijKBrCCDc6FJKrWyT4a5MywXMMZ4Xr2yfKobsEPWDAYJbkSaiNsVl")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    authors = soup.findAll('span', attrs= {'class':'x3nfvp2'})
    
    for author in authors:
        print(author.text)

scrapePage()