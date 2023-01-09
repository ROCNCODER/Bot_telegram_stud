import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

import  spisok_filters
class GetPage():
    def __init__(self,link,keyword):
        self._link=link
        self._keyword=keyword

    def list_link_vacansia(self):
        ua = UserAgent()
        date = requests.get(
            url=f"{self._link+self._keyword}",
            headers={"user-agent": ua.random}
        )

        if date.status_code != 200:
            return

        soup = BeautifulSoup(date.content, "lxml")

        return soup


class NumberOfPages(GetPage):
    def __init__(self, link, keyword,col_stranitch,place_link):
        GetPage.__init__(self, link, keyword)
        self._col_stranitch=col_stranitch
        self._place_link=place_link

    def Namber(self):
        ua = UserAgent()
        try:
            col_stranitch = int(self._col_stranitch)
            print(col_stranitch)
        except:
            сol_stranitch = 0

        for i in range(col_stranitch):
            date = requests.get(
                url=f"{self._link+self._keyword}&page={i}",
                headers={"user-agent": ua.random}
            )

            soup = BeautifulSoup(date.content, "lxml")
            spisok_link = []
            for a in soup.find_all("a", attrs={"class": f"{self._place_link}"}):
                spisok_link.append(a.get("href"))

            return (spisok_link)



class Filters_link():

    def __init__(self,link_mass):
        self._link_mass=link_mass
        self._osnovnoy_content = ""
        self._name_vacansia = ""
        self._base_link=[]
        # self._collection_links=()


    def Sorting(self):
            self._base_link=[]
            for i in spisok_filters.spisok_student:
                if i in self._osnovnoy_content or i in self._name_vacansia:
                    self._base_link.append("студент+")

                    break

            for i in spisok_filters.spisok_probationer:
                if i in self._osnovnoy_content or i in self._name_vacansia:
                    self._base_link.append("стажер+")

            if len(self._link_mass) != 3:
                if len(self._link_mass) != 2:
                    self._base_link.append("студент-")
                    self._base_link.append("стажер-")
                else:
                    if self._base_link[1] == "студент+":
                        self._base_linkappend("стажер-")
                    else:
                        self._base_link.append("студент-")


                return (self._base_link)

    def filtre_hh(self):
        br=[]
        ua = UserAgent()
        for n in self._link_mass:
            date = requests.get(
                url=f"{n}",
                headers={"user-agent": ua.random}
            )

            soup = BeautifulSoup(date.content, "lxml")

            # Забираем проверяемые элементы сайта
            try:
                self._name_vacansia = soup.find("div", attrs={"class": "vacancy-title"}).find("h1").text
            except Exception as ex:
                print(ex)
            self._name_vacansia = re.split(" ", self._name_vacansia)
            self._osnovnoy_content = ""
            try:
                self._osnovnoy_content = soup.find("div", attrs={"class": "g-user-content"}).text
            except Exception as ex:
                print(ex)
            osnovnoy_content = re.split(" ", self._osnovnoy_content)
            br=[]
            br.append(n)
            d = self.Sorting()
            br.append(d[0])
            br.append(d[1])
            print(br)



class Resume(GetPage):
    def __init__(self,mass_top_link,name_sferi,vacant,link, keyword):
        GetPage.__init__(self, link, keyword)
        self._mass_top_link=mass_top_link
        self._name_sferi=name_sferi
        self._vacant=vacant

    def content_rezume(self):
            vansian=()
            links=()
            zpd=()
            graf=()
            sity=()
            mod_1=()
            mod_2=()
            ua = UserAgent()
            for i in self._mass_top_link:
                t = i[0]
                date = requests.get(
                    url=f"{t}",
                    headers={"user-agent": ua.random}
                )
                soup = BeautifulSoup(date.content, "lxml")
                print(t)
                name_vacansian = ""
                zp = ""
                grafik = ""
                gorod = ""
                try:
                    name_vacansian = soup.find("div", attrs={"class": "vacancy-title"}).find("h1").text
                except:
                    name_vacansian = "Не указана"
                try:
                    zp = soup.find("div", attrs={"data-qa": "vacancy-salary"}).text
                except:
                    zp = "не указан"
                try:
                    grafik = soup.find("p", attrs={"class": "vacancy-description-list-item"}).text
                except:
                    grafik = "не указан"
                try:
                    gorod = soup.find("p", attrs={"data-qa": "vacancy-view-location"}).text
                except:
                    try:
                        gorod = soup.find("span", attrs={"data-qa": "vacancy-view-raw-address"}).text
                    except:
                        gorod = "Не указано"

                # sql_db.update(self._name_sferi, self._vacant, name_vacansian, t, zp, grafik, gorod, i[1], i[2])
                vansian.append(name_vacansian)
                links.append(t)
                zpd.append(zp)
                graf.append(grafik)
                sity.append(gorod)
                mod_1.append(i[1])
                mod_2.append(i[2])


hh = GetPage("https://hh.ru/search/vacancy?experience=noExperience&text=", "Экономист")
hh = NumberOfPages("https://hh.ru/search/vacancy?experience=noExperience&text=",'Экономист',hh.list_link_vacansia().find("div", attrs={"class": "pager"}).find_all("span")[-3].text, f"serp-item__title")
hh = Filters_link(hh.Namber())
hh = Resume()
print(hh.filtre_hh())