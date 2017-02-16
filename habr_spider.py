
import scrapy
import json


class HabrSpider(scrapy.Spider):
    name = 'habrspider'
    start_urls = ['https://habrahabr.ru', ]

    def parse(self, response):
        for item in response.css('div.post.post_teaser.shortcuts_item'):
            title = item.css('a.post__title_link::text').extract_first()
            hubs = item.css('a.hub::text').extract()
            link = item.css('a.post__title_link::attr("href")').extract_first()
            print(dict(title=title, hubs=hubs, link=link))

            my_file = open('parsed_habrahabr.txt', 'a')
            my_file.write(
                          json.dumps(dict(title=title, hubs=hubs, link=link),
                                     ensure_ascii=False)
                          )
            my_file.write('\n \n')
            my_file.close()
