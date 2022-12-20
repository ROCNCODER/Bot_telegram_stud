import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

from data_bs import sql_db
import filters
import spisok_zaprosov


ua = UserAgent()


def list_link_vacansia(zapros):
    date = requests.get(
        url=f"https://hh.ru/search/vacancy?experience=noExperience&text={zapros}",
        headers={"user-agent":ua.random}
    )
    if date.status_code!=200:
        return
    
    soup=BeautifulSoup(date.content,"lxml")
    
    try:
        
        col_stranitch=int(soup.find("div",attrs={"class":"pager"}).find_all("span")[-3].text)
    except:
        сol_stranitch=int(soup.find("div",attrs={"class":"pager"}).find_all("a",attrs={"class":"block-button"})[-2].text)
    for i in range(col_stranitch):
        date = requests.get(
            url=f"https://hh.ru/search/vacancy?experience=noExperience&text={zapros}&page={i}",
            headers={"user-agent":ua.random}
        )
        
        
        soup=BeautifulSoup(date.content,"lxml")
        spisok_link=[]
        for a in soup.find_all("a", attrs={"class":"serp-item__title"}):
            spisok_link.append(a.get("href"))
            
        return(filters.filtre_hh(spisok_link))


def content_rezume(mass_top_link,name_sferi,vacant):
    for i in mass_top_link:
        t=i[0]
        date=requests.get(
            url=f"{t}",
            headers={"user-agent":ua.random}
        )
        soup=BeautifulSoup(date.content,"lxml")
        print(t)
        name_vacansian=""
        zp=""
        grafik=""
        gorod=""
        try:
            name_vacansian=soup.find("div",attrs={"class":"vacancy-title"}).find("h1").text
        except:
            name_vacansian="Не указана"
        try:
            zp=soup.find("div",attrs={"data-qa":"vacancy-salary"}).text
        except:
            zp="не указан"
        try:
            grafik=soup.find("p", attrs={"class":"vacancy-description-list-item"}).text
        except:
            grafik="не указан"
        try:
            gorod=soup.find("p", attrs={"data-qa":"vacancy-view-location"}).text
        except:
            try:
                gorod=soup.find("span", attrs={"data-qa":"vacancy-view-raw-address"}).text
            except:
                gorod="Не указано"
        
           
        
        sql_db.update(name_sferi,vacant,name_vacansian,t,zp,grafik,gorod,i[1],i[2])










def main():
    for i in spisok_zaprosov.god_spisok:
        try:
            sql_db.Del_table(i)
            sql_db.sozidanie_table(i)
        except:
            print("OK")
        for n in spisok_zaprosov.god_spisok[i]:
            time.sleep(1)
            content_rezume(list_link_vacansia(n),i,n)

if __name__ == '__main__':
    main()