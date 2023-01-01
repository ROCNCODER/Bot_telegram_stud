import re

import fake_useragent
import requests
import spisok_filters
from bs4 import BeautifulSoup

ua = fake_useragent.UserAgent()

def filtre_hh(list):
    base_link=[]
    spisok_ok_silok=[]
    marker_marker=[]
    for n in list:
        date=requests.get(
            url=f"{n}",
            headers={"user-agent":ua.random}
        )
        

        soup=BeautifulSoup(date.content,"lxml")

    #Забираем проверяемые элементы сайта 
        name_vacansian=""
        try:
            name_vacansian=soup.find("div",attrs={"class":"vacancy-title"}).find("h1").text
        except Exception as ex:
            print(ex)
        name_vacansian=re.split(" ",name_vacansian)
        osnovnoy_content=""
        try:
            osnovnoy_content=soup.find("div",attrs={"class":"g-user-content"}).text
        except Exception as ex:
            print(ex)
        osnovnoy_content=re.split(" ",osnovnoy_content)
        marker_marker=[n]
        for i in spisok_filters.spisok_student:
                if i in osnovnoy_content or i in name_vacansian:
                    
                    marker_marker.append("студент+")
                
                    break



        for i in spisok_filters.spisok_probationer:
                if i in osnovnoy_content or i in name_vacansian:
                    marker_marker.append("стажер+")

                
       


        
        if len(marker_marker)!=3:
            if len(marker_marker)!=2:
                marker_marker.append("студент-")
                marker_marker.append("стажер-")
            else:
                if marker_marker[1]=="студент+":
                    marker_marker.append("стажер-")
                else:
                    marker_marker.append("студент-")
        base_link.append(marker_marker)

    return(base_link)

        
                
       

        




        



        

    

    
def filtre_sj():
    pass


def main():
    pass

if __name__ == '__main__':
    main()