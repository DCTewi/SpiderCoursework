#coding=utf-8

import time

import urls_manager
import html_downloader
import html_parser

def main():
    print('启动成功, 准备抓取')

    while True:
        print('正在抓取主页\n')

        urls = html_downloader.download_index()
        print('获得了{}个新闻链接\n'.format(len(urls)))

        for url in urls:
            time.sleep(0.5)
            print("正在尝试抓取{}\n".format(url))

            if not urls_manager.check_url_exist(url):
                html = html_downloader.download_single_page(url)
                news = html_parser.parse_page(html, url)

                if news is None:
                    continue

                urls_manager.save_news(news)
                print()
            else:
                print("新闻已经抓取过, 跳过\n")
            
        print('抓取完成, 等待下一轮调度')
        time.sleep(5)

if __name__ == "__main__":
    main()
