#coding=utf-8

class News():
    def __init__(self, title: str, publish_time: str, views: bool, url: str) -> None:
        self.title = title
        self.publish_time = publish_time
        self.views = views
        self.url = url
    def __str__(self) -> str:
        return "title:{}\npublish_time:{}\nviews:{}\nurl:{}\n".format(self.title, self.publish_time, self.views, self.url)
    def __eq__(self, o: object) -> bool:
        return self.url == o.url

def from_json_2_News(news: News) -> News:
    return News(news['title'], news['publish_time'], news['views'], news['url'])

def from_News_2_json(news: News) -> dict:
    return news.__dict__
