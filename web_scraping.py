import requests
from bs4 import BeautifulSoup
import pymysql.cursors
from peewee import *
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    # database = "web_scarping"
)

mydbcursor = mydb.cursor()

mydbcursor.execute("CREATE DATABASE IF NOT EXISTS web_scraping")
mydbcursor.execute("USE web_scraping")
mydb.commit()

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "web_scraping"
)

mycursor = con.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS vnexpress_giao_duc (title VARCHAR(255) PRIMARY KEY, des TEXT, url VARCHAR(255))")
con.commit()
sql = "INSERT INTO vnexpress_giao_duc (title, des, url) VALUES (%s, %s, %s)"


# connection = pymysql.connect(host='192.168.1.1', user='root', password='', db='scrape_web', charset='utf8mb4')
# print("Connect Successful!")


# def getConnection():
#     connection = pymysql.connect(host='192.168.1.1', user='root', password='', db='scrape_web', charset='utf8mb4',
#                                  cursorclass='pymysql.cursors.DictCursor')
#     return connection

urls = []
res = requests.get("https://vnexpress.net/giao-duc")
src = res.content
soup = BeautifulSoup(src, 'html.parser')


# def tag(article, h, des):
#     # h_tag = article.find(h, {"class": des})
#     # if h_tag == 'None':
#     #     return None
#     # # h_tag = article.find()
#     # else:
#     #     a_tag = h_tag.find('a')
#     #         # urls.append(a_tag['title'])
#     return ''


def article(des):

    # dict = {'title': '', 'description': ''}
    res = []
    if des == '':
        dict = {'title': '', 'description': ''}
        for article in soup.find_all('article'):
            articleTag = article.select_one('article > h1.title_news > a')
            # article = BeautifulSoup(article, 'html.parser')
            # res.append(article)
            # dict['title'] = tag(article, 'h1', 'title_news')
            # dict['description'] = tag(article, 'p', 'description')


            # res.append(articleTag)
    elif des == 'list_news':

        for article in soup.find_all('article', {"class": des}):
            dict = {'title': '', 'description': '', 'url': ''}
            articleTitle = article.select_one('article.list_news > h4.title_news > a')['title']
            articleDescription = article.select_one('article.list_news > p.description > a').text.strip()
            articleUrl = article.select_one('article.list_news > h4.title_news > a')['href']
            # article = BeautifulSoup(article, 'html.parser')
            # res.append(article)
            dict['title'] = articleTitle
            dict['description'] = articleDescription
            dict['url'] = articleUrl

            res.append(dict)

            # print(type(article))
    return res

# article()
# article('list_news')
# a = []
a = article('list_news')

for x in a:
    val = (x['title'], x['description'], x['url'])
    mycursor.execute(sql, val)


# con.commit()
mycursor.execute("SELECT * FROM vnexpress_giao_duc")

myres = mycursor.fetchall()

for x in myres:
    print(x)

con.commit()





# def get_data(h, des):
#     news = {'title':'','des':''}






# soup = BeautifulSoup(src, 'html.parser')
# tag('h1', 'title_news')
# tag('p', 'description')
# tag('h4', 'title_news')


# for h4_tag in soup.find_all("h4"):
#     a_tag = h4_tag.find('a')
#     # title = a_tag.find('title')
#     urls.append(a_tag.attrs['href'])
#     # print(type(a_tag))

# print(urls)

# try:
#     with connection.cursor() as cursor:
#         q1 = "CREAT DATABASE scrape_web"
#         print(cursor.execute(q1))
#         q2 = "CREATE TABLE 'data'('id' varchar(255) NOT NULL, PRIMARY KEY('id')"
#         print(cursor.execute(q2))
#         q3 = "INSERT INTO 'scrape_web' VALUES (%s)"
#         print(cursor.execute(q3, urls))
#
#
#         connection.commit()
# finally:
#     connection.close()