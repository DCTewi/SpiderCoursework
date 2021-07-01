#coding=utf-8

import re
import urllib.parse
import urllib.request

from spider_config import index_url

def download_index() -> list:
    index_page = urllib.request.urlopen(index_url).read()
    index_page = index_page.decode('utf-8', 'ignore')

    raw_list = re.findall(r'(/\d{4}/\d{4}/[0-9a-zA-Z]+/page.htm)', index_page)
    return [index_url + i for i in raw_list]

def download_single_page(url: str) -> str:
    return urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
