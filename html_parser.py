#coding=utf-8

from bs4 import BeautifulSoup

from news import News

from spider_config import title_selector, publish_selector, views_selector

def parse_page(page_str: str, url: str) -> News:
    try:
        soup = BeautifulSoup(page_str, 'lxml')

        title = soup.select(title_selector)[0]
        print("标题: {}".format(title))

        publish_time = soup.select(publish_selector)[0]
        print("时间: {}".format(publish_time))

        views = soup.select(views_selector)[0]
        print("浏览量: {}".format(views))

        return News(title.string, publish_time.string, views.string, url)

    except:
        print("选择器未选择到指定内容, 跳过")

        return None
