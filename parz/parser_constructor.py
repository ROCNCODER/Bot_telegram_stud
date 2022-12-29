import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


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

            print(spisok_link)


hh = GetPage("https://hh.ru/search/vacancy?experience=noExperience&text=", "Экономист")
hh = NumberOfPages("https://hh.ru/search/vacancy?experience=noExperience&text=",'Экономист',hh.list_link_vacansia().find("div", attrs={"class": "pager"}).find_all("span")[-3].text, f"serp-item__title")
print(hh.Namber())

class Filters():
    def filtre_hh(self):
        base_link = []
        spisok_ok_silok = []
        marker_marker = []
        for n in list:
            date = requests.get(
                url=f"{n}",
                headers={"user-agent": ua.random}
            )

            soup = BeautifulSoup(date.content, "lxml")

            # Забираем проверяемые элементы сайта
            name_vacansian = ""
            try:
                name_vacansian = soup.find("div", attrs={"class": "vacancy-title"}).find("h1").text
            except Exception as ex:
                print(ex)
            name_vacansian = re.split(" ", name_vacansian)
            osnovnoy_content = ""
            try:
                osnovnoy_content = soup.find("div", attrs={"class": "g-user-content"}).text
            except Exception as ex:
                print(ex)
            osnovnoy_content = re.split(" ", osnovnoy_content)
            marker_marker = [n]
            for i in spisok_filters.spisok_student:
                if i in osnovnoy_content or i in name_vacansian:
                    marker_marker.append("студент+")

                    break

            for i in spisok_filters.spisok_probationer:
                if i in osnovnoy_content or i in name_vacansian:
                    marker_marker.append("стажер+")

            if len(marker_marker) != 3:
                if len(marker_marker) != 2:
                    marker_marker.append("студент-")
                    marker_marker.append("стажер-")
                else:
                    if marker_marker[1] == "студент+":
                        marker_marker.append("стажер-")
                    else:
                        marker_marker.append("студент-")
            base_link.append(marker_marker)

        return (base_link)