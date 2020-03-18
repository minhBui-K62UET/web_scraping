import requests
from bs4 import BeautifulSoup


def get_article(des):
    result = []
    url = "https://vnexpress.net/giao-duc-p"

    for page_number in range(1, 1265):
        print(page_number)
        next_page = url + str(page_number)
        req = requests.get(str(next_page))
        soup = BeautifulSoup(req.content, "lxml")

        if des == 'list_news':
            for article in soup.find_all('article', {"class": des}):
                article_dict = {'title': '', 'description': '', 'url': ''}
                article_title = article.select_one('article.list_news > h4.title_news > a')['title']
                article_description = article.select_one('article.list_news > p.description > a').text.strip()
                article_url = article.select_one('article.list_news > h4.title_news > a')['href']
                article_dict['title'] = article_title
                article_dict['description'] = article_description
                article_dict['url'] = article_url
                result.append(article_dict)

    return result


