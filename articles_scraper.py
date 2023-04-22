import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import os
import multiprocessing


class ArticleSpider(scrapy.Spider):
    name = 'article_spider'

    def __init__(self, urls=[], **kwargs):
        super().__init__(**kwargs)
        self.start_urls = urls

    def parse(self, response):
        article_links = response.css('div.latest_article_text > h2 > a::attr(href)').getall()
        
        # Write the extracted links to a CSV file
        with open('article_links.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for link in article_links:
                writer.writerow([link])


def scrape_article_links(urls):
    process = CrawlerProcess()
    process.crawl(ArticleSpider, urls=urls)
    process.start()  # Script will block here until the crawling is finished.


def worker(url_list):
    scrape_article_links(url_list)


if __name__ == "__main__":
    # Set URLs list
    urls = [f'https://www.vgchartz.com/articles/?start={x}&category_story=Article&btn_submit=Search&q=' for x in range(0,1500,20)]
    
    # Initialize an empty CSV file
    with open('article_links.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Article Links'])

    # Run the code on the provided URLs with multiprocessing
    num_processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_processes) as pool:
        pool.map(worker, [urls[i::num_processes] for i in range(num_processes)])
