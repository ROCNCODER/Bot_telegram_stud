import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import schedule
import  spisok_filters

ua = UserAgent()
date = requests.get(
    url="https://hh.ru/search/vacancy?experience=noExperience&text=Экономист",
    headers={"user-agent": ua.random}
)

soup = BeautifulSoup(date.content, "lxml")


class Parcer_constrct():


        def __init__(self, link,name_sferi,vacant):
            self._link = link
            self._name_sferi = name_sferi
            self._vacant = vacant
            # Запрос на количество страниц

            try:
                self._col_stranitch=soup.find("div", attrs={"class": "pager"}).find_all("span")[-3].text
                # Запросов определяющий место ссылок


                self._name_vacansia=soup.find("div", attrs={"class": "vacancy-title"}).find("h1").text
                self._osnovnoy_content=soup.find("div", attrs={"class": "g-user-content"}).text


                self._zp = soup.find("div", attrs={"data-qa": "vacancy-salary"}).text

                self._grafik = soup.find("p", attrs={"class": "vacancy-description-list-item"}).text
                self._gorod = soup.find("p", attrs={"data-qa": "vacancy-view-location"}).text
            finally:
                l=0





        def list_link_vacansia(self):
            ua = UserAgent()
            date = requests.get(
                url=f"{self._link + self._vacant}",
                headers={"user-agent": ua.random}
            )

            if date.status_code != 200:
                return

            soup = BeautifulSoup(date.content, "lxml")

            try:
                col_stranitch = self._col_stranitch
            except:
                сol_stranitch =  0
            return col_stranitch

        def Namber(self):
            ua = UserAgent()
            try:
                col_stranitch = self.list_link_vacansia()
                print(col_stranitch)
            except:
                сol_stranitch = 0

            for i in range(self.list_link_vacansia()):
                date = requests.get(
                    url=f"{self._link + self._vacant}&page={i}",
                    headers={"user-agent": ua.random}
                )

                soup = BeautifulSoup(date.content, "lxml")
                spisok_link = []
                for a in soup.find_all("a", attrs={"class": "serp-item__title"}):
                    spisok_link.append(a.get("href"))
                return (spisok_link)

        def Sorting(self):
            base_link=[]
            link_mass = self.Namber()
            for i in spisok_filters.spisok_student:
                if i in self._osnovnoy_content or i in self._name_vacansia:
                    base_link.append("студент+")

                    break

            for i in spisok_filters.spisok_probationer:
                if i in self._osnovnoy_content or i in self._name_vacansia:
                    base_link.append("стажер+")

            if len(link_mass) != 3:
                if len(link_mass) != 2:
                    base_link.append("студент-")
                    base_link.append("стажер-")
                else:
                    if base_link[1] == "студент+":
                        base_link.append("стажер-")
                    else:
                        base_link.append("студент-")

                return base_link


        def filtre_hh(self):

            dr =[]
            ua = UserAgent()
            for n in self.Namber():
                date = requests.get(
                    url=f"{n}",
                    headers={"user-agent": ua.random}
                )

                soup = BeautifulSoup(date.content, "lxml")

                # Забираем проверяемые элементы сайта
                name_vacansia=""
                try:
                    name_vacansia = self._name_vacansia
                except Exception as ex:
                    print(ex)
                name_vacansia = re.split(" ", name_vacansia)
                osnovnoy_content=""
                try:
                    osnovnoy_content = self._osnovnoy_content
                except Exception as ex:
                    print(ex)
                osnovnoy_content = re.split(" ", osnovnoy_content)
                br=[]
                br.append(n)
                d = self.Sorting()
                br.append(d[0])
                br.append(d[1])
                dr.append(br)
                print(dr)
            return dr

        def content_rezume(self):
            vansian = ()
            links = ()
            zpd = ()
            graf = ()
            sity = ()
            mod_1 = ()
            mod_2 = ()
            ua = UserAgent()

            for i in self.filtre_hh():
                t = i[0]
                date = requests.get(
                    url=f"{t}",
                    headers={"user-agent": ua.random}
                )
                soup = BeautifulSoup(date.content, "lxml")
                name_vacansian = ""
                zp = ""
                grafik = ""
                gorod = ""
                try:
                    name_vacansian = self._name_vacansia
                except:
                    name_vacansian = "Не указана"
                try:
                    zp = self._zp
                except:
                    zp = "не указан"
                try:
                    grafik = self._grafik
                except:
                    grafik = "не указан"
                try:
                    gorod = self._gorod
                except:
                        gorod = "Не указано"

                # sql_db.update(self._name_sferi, self._vacant, name_vacansian, t, zp, grafik, gorod, i[1], i[2])
                # vansian.append(name_vacansian)
                # links.append(t)
                # zpd.append(zp)
                # graf.append(grafik)
                # sity.append(gorod)
                # mod_1.append(i[1])
                # mod_2.append(i[2])
                print(t)


# hh = Parcer_constrct("https://hh.ru/search/vacancy?experience=noExperience&text=", "гоД",'Экономист')
# hh.content_rezume()


class Parser_hh(Parcer_constrct):
    pass




hh=Parser_hh("https://hh.ru/search/vacancy?experience=noExperience&text=", "гоД",'Экономист')

hh.content_rezume()




def main():
    pass
