from bs4 import BeautifulSoup
import requests
import fake_useragent

ua = fake_useragent.UserAgent()

def filtre_hh(list):
    for i in list:
        date=requests.get(
            url="i",
            headers={"user-agent":ua.random}
        )

    soup=BeautifulSoup(date,"lxml")

    
def filtre_sj():
    pass