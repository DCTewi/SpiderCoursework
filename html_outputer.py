#coding=utf-8

import os

from news import News

def output_to_html(news: News) -> None:
    if not os.path.exists("output"):
        os.makedirs("output")

    body = """<html>
<head><head>
<body>

<h1>标题:{}</h1>
<div>{}</div>
<div>浏览量:{}</div>
<div>原文链接:{}</div>
</body>
</html>
""".format(news.title, news.publish_time, news.views, news.url)
    
    with open("output/{}.html".format(news.title), mode="w+", encoding="utf-8") as f:
        f.write(body)
