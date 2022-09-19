from datetime import date
from functools import total_ordering
from posixpath import split
import requests
import re
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
from datetime import datetime

ua = fake_useragent.UserAgent()
now_date = datetime.now()

def get_links(text):
    date = requests.get(
        url=f"https://hh.ru/search/vacancy?text={text}&from=suggest_post&area=1&page=0",
        headers={"user-agent":ua.random}
    ) 
  
    if date.status_code !=200: 
        return

    soup = BeautifulSoup(date.content,"lxml")
    try:
        col_str = int(soup.find("div", attrs={"class":"pager"}).find_all("span", recursive=False)[-1].find("a").find("span").text)
    except:
        col_str = 1
    for page in range(col_str):
        try:
        
            date = requests.get(
            url=f"https://hh.ru/search/vacancy?text={text}&from=suggest_post&area=1&page={page}",
            headers={"user-agent":ua.random}
            )
            if date.status_code !=200:
                    continue
            soup = BeautifulSoup(date.content,"lxml")
            for a in soup.find_all("a", attrs={"class":"serp-item__title"}):
                    yield f"{a.attrs['href'].split('?')[0] }" 

        except Exception as e:
            print(f"{e}")
            time.sleep(1)
        
cur = date.today

def get_resume(link):
    date= requests.get(
    url=link,
    headers={"user-agent":ua.random}
    )
    if date.status_code !=200:
        return

    soup = BeautifulSoup(date.content,"lxml")
    try:
        name = (soup.find(attrs={"class":"bloko-header-section-1"}).text)
        dad = soup.find(attrs={"class":"vacancy-creation-time-redesigned"}).text
        Proverca_vremeni(dad)
    except:
        name = ""
    
    some_date = datetime(int(YTSUBA[2]), int(YTSUBA[1]) ,int(YTSUBA[0]))
    a = (now_date-some_date).days
    
    resume = {
            
            "Вакансия":name,
            "Ссылка":link,
            "Дата публикации": tims_red,
            
            
            }
    
    return resume
  

def Proverca_vremeni(tims):
    global tims_red
    global YTSUBA
    tims_red = re.sub("\xa0", "-", tims)
    total_ordering = {
        "января"  :1, 
        "февраля" :2,
        "марта"    :3,
        "апреля"  :4,
        "майя"     :5,
        "июня"    :6,
        "июля"    :7,
       "августа"   :8,
        "сентября":9,
        "октября" :10,
        "ноября"  :11,
        "декабря" :12
        
        }
    
    ITSUKI = re.split(" ",tims_red)
    NINO = re.split("-",ITSUKI[2])
    MIKY = str(total_ordering[NINO[1]])
    YTSUBA=(NINO[0],(MIKY),NINO[2])
    

    


    

   
    
        
    

# def get_time(link):
#     global dad
#     date= requests.get(
#     url=link,
#     headers={"user-agent":ua.random}
#     )
#     if date.status_code !=200:
#         return

#     soup = BeautifulSoup(date.content,"lxml")
#     try:
#         dad = soup.find(attrs={"class":"vacancy-creation-time-redesigned"}).text
#     except:
#        dad = ""
#     return dad

if __name__ == "__main__":
        for a in get_links("финансист+студент"):
            spisok=(get_resume(a),)
            print(spisok)
            time.sleep(1)
        for a in get_links("экономист+студент"):
            spisok=(get_resume(a),)
            print(spisok)
            time.sleep(1)

    
    


#link="https://hh.ru/search/vacancy?text=Python&from=suggest_post&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true"
#straniga_economics_one = requests.get(link).text
#print(straniga_economics_one) 