import requests
from bs4 import BeautifulSoup
import fake_useragent
import time


ua = fake_useragent.UserAgent()


def list_link_vacansia():
    date = requests.get(
        url=f"https://hh.ru/search/vacancy?text=физикучитель",
        headers={"user-agent":ua.random}
    )
    if date.status_code!=200:
        return
    
    soup=BeautifulSoup(date.content,"lxml")
    
    try:
        
        col_stranitch=int(soup.find("div",attrs={"class":"pager"}).find_all("span")[-3].text)
        print(col_stranitch)
    except:
        сol_stranitch=int(soup.find("div",attrs={"class":"pager"}).find_all("a",attrs={"class":"block-button"})[-2].text)
        print(col_stranitch)
    for i in range(col_stranitch):
        date = requests.get(
            url=f"https://hh.ru/search/vacancy?text=физика&page={i}",
            headers={"user-agent":ua.random}
        )
        
        
        soup=BeautifulSoup(date.content,"lxml")
        spisok_link=[]
        for a in soup.find_all("a", attrs={"class":"serp-item__title"}):
            print(a.get("href"))
            spisok_link.append(a.get("href"))
            


            
        
    
            

        
           
            
        
        
        
         
        
    

def content_rezume():
    pass








def main():
    list_link_vacansia()

if __name__ == '__main__':
    main()