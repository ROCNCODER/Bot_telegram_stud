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
import pymysql

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

try:
    connection = pymysql.connect(
        host="92.53.124.26",
        port=3306,
        user="gen_user",
        password="71alidi6z3",
        database="default_db"    
    )
    print('Заебись')

except Exception as ex:
    print(ex)


spiski_economist={
"финансист+студент",
"экономист+студент"
}

spiski_urist={
"Юрист+студент", 
}

spiski_perovod_ingl={
"переводчик+английский+студент",
"английский+студент",
"лингвисит+английский+студент"
}
spiski_perovod_nem={
"переводчик+немецкий+студент",
"немецкий+студент",
"лингвисит+немецкий+студент"
}
spiski_perovod_fr={
"переводчик+французский+студент",
"французский+студент",
"лингвисит+французкий+студент"
}
spiski_perovod_china={
"переводчик+китайский+студент",
"китайский+студент",
"лингвисит+китайский+студент"
}

spiski_economist_sb={
"экономисты%20студенты"
}



if __name__ == "__main__":
        for a in get_links("финансист+студент"):
            spisok=(get_resume(a),)
            print(spisok)
            time.sleep(1)
        for a in get_links("экономист+студент"):
            spisok=(get_resume(a),)
            print(spisok)
            time.sleep(1)
        try:
            for i in  spiski_economist:
           
                    for a in get_links(i):

                        spisok=(get_resume(a))
                        time.sleep(1)
                        snils=str(spisok["Вакансия"])
                        snils_one=str(spisok["Ссылка"])
                        snils_TRY=str(spisok["Дата публикации"]) 
                
                        with connection.cursor() as cursor:
                            inser_qveri=f"INSERT INTO `Vacansian_economics`(NAME,LINK,DATE,Сервис) VALUES ('{snils}','{snils_one}','{snils_TRY}','hh')"
                            cursor.execute(inser_qveri)
                            connection.commit()


            for i in  spiski_urist:
           
                    for a in get_links(i):

                        spisok=(get_resume(a))
                        time.sleep(1)
                        snils=str(spisok["Вакансия"])
                        snils_one=str(spisok["Ссылка"])
                        snils_TRY=str(spisok["Дата публикации"]) 
                
                        with connection.cursor() as cursor:
                            inser_qveri=f"INSERT INTO `Vacansian_urist`(NAME,LINK,DATE,Сервис) VALUES ('{snils}','{snils_one}','{snils_TRY}','hh')"
                            cursor.execute(inser_qveri)
                            connection.commit()

            for i in  spiski_perovod_ingl:
           
                    for a in get_links(i):

                        spisok=(get_resume(a))
                        time.sleep(1)
                        snils=str(spisok["Вакансия"])
                        snils_one=str(spisok["Ссылка"])
                        snils_TRY=str(spisok["Дата публикации"]) 
                
                        with connection.cursor() as cursor:
                            inser_qveri=f"INSERT INTO `Vacansian_lengvih`(NAME,LINK,DATE,Сервис,Язык) VALUES ('{snils}','{snils_one}','{snils_TRY}','hh','Анг')"
                            cursor.execute(inser_qveri)
                            connection.commit()
            for i in  spiski_perovod_nem:
           
                    for a in get_links(i):

                            spisok=(get_resume(a))
                            time.sleep(1)
                            snils=str(spisok["Вакансия"])
                            snils_one=str(spisok["Ссылка"])
                            snils_TRY=str(spisok["Дата публикации"]) 
                    
                            with connection.cursor() as cursor:
                                inser_qveri=f"INSERT INTO `Vacansian_lengvih`(NAME,LINK,DATE,Сервис,Язык) VALUES ('{snils}','{snils_one}','{snils_TRY}','hh','Нем')"
                                cursor.execute(inser_qveri)
                                connection.commit()

                    for i in  spiski_perovod_fr:
                    
                                for a in get_links(i):

                                    spisok=(get_resume(a))
                                    time.sleep(1)
                                    snils=str(spisok["Вакансия"])
                                    snils_one=str(spisok["Ссылка"])
                                    snils_TRY=str(spisok["Дата публикации"]) 
                            
                                    with connection.cursor() as cursor:
                                        inser_qveri=f"INSERT INTO `Vacansian_lengvih`(NAME,LINK,DATE,Сервис,Язык) VALUES ('{snils}','{snils_one}','{snils_TRY}','hh','Фр')"
                                        cursor.execute(inser_qveri)
                                        connection.commit()

                    for i in  spiski_perovod_china:
                    
                                for a in get_links(i):

                                    spisok=(get_resume(a))
                                    time.sleep(1)
                                    snils=str(spisok["Вакансия"])
                                    snils_one=str(spisok["Ссылка"])
                                    snils_TRY=str(spisok["Дата публикации"]) 
                            
                                    with connection.cursor() as cursor:
                                        inser_qveri=f"INSERT INTO `Vacansian_lengvih`(NAME,LINK,DATE,Сервис,Язык) VALUES ('{snils}','{snils_one}','{snils_TRY}','hh','Китай')"
                                        cursor.execute(inser_qveri)
                                        connection.commit()


          
                            
        finally:
                connection.close()    
                            






    
    


#link="https://hh.ru/search/vacancy?text=Python&from=suggest_post&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true"
#straniga_economics_one = requests.get(link).text
#print(straniga_economics_one) 