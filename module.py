import requests 
from bs4 import BeautifulSoup
__author__ = "Гурбатов Владислав"
def parser(page:int):
    # создаём запорос сайта
    res = requests.get('https://zabgu.ru/php/news.php?category=1&page=' + page.__str__())
    # вытаскиваем из запроса html код
    text = res.text
    # создаём BeautifulSoup который парсит html код
    soup = BeautifulSoup(text, "html.parser")
    # находим на сайте нужные теги
    date = soup.find_all("div", class_ = "dateOnImage")
    tag = soup.find_all("div", class_ = "markersContainer")
    title = soup.find_all("div", class_= "headline")
    # выводим новости в консоль
    strweb = "Страница №" + page.__str__() + "\n\n"
    for i in range(len(date)):
        strweb += "Новость №" + i.__str__() + "\n"
        strweb += "Дата: "
        datetext = date[i].text.split('\n')
        for j in range(len(datetext)):
            if(datetext[j] != ''):
                strweb += datetext[j] + " "
        strweb += "\nЗаголовок: " + title[i].text + "\n"
        strweb +="Тэг: " + tag[i].text + "\n"
    print(strweb)