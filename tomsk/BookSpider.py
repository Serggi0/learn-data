from urllib import response
import scrapy
import time


class BookSpider(scrapy.Spider):
    name = "BookSpider"
    start_urls = ["http://knigi.tomsk.ru/products/new"]

    def parse(self, response):
        links = response.css("div.name a::attr(href)")
        for link in links:
            time.sleep()
            yield response.follow(link, self.parse_book)

        link = response.css("div.pagination a::attr(href)")[-1].get()
        yield response.follow(link, self.parse)

    def parse_book(self, response):
        yield {
            "name": response.css("div.page h1::text").get(),
            "price": response.css('div.price-helper div.price::text').get().split(" ")[0],
            "genere": response.css('div.breadcrumbs ul li a::text')[-1].get()
        }