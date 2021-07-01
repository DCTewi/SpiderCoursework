#coding=utf-8

import os
import json

from news import News, from_News_2_json, from_json_2_News

def load_url_form_json() -> list:
    if os.path.exists("result.json"):
        with open("result.json", mode="r", encoding="utf-8") as f:
            return json.load(f, object_hook=from_json_2_News)
    else:
        return []

def check_url_exist(url: str) -> bool:
    newss = load_url_form_json()
    for news in newss:
        if news.url == url:
            return True
    return False

def save_news(news: News) -> None:
    newss = load_url_form_json()
    newss.append(news)
    with open("result.json", mode="w+", encoding="utf-8") as f:
            json.dump(newss, f, default=from_News_2_json, sort_keys=True, indent=4, ensure_ascii=False)
