import scrapy
import logging

class BooksBasicSpider(scrapy.Spider):
    name = 'books_basic'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    def parse(self, response):
        books = response.xpath('//h3')
        # books = response.css('h3')

        for book in books:
            # yield {
            #     'title': book.xpath('.//a/@title').get(),
            #     # 'title': book.css('a::attr(title)')
            #     'URL': book.xpath('.//a/@href').get()
            # }
            yield response.follow(url=book.xpath('.//a/@href').get(), callback=self.parse_item)

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)

    def parse_item(self, response):
        main_book_info = response.xpath('//div[@class="col-sm-6 product_main"]')
        # main_book_info = response.css('div.col-sm-6.product_main')
        yield {
            'title': main_book_info.xpath('.//h1/text()').get(),
            'price': main_book_info.xpath('.//p[@class="price_color"]/text()').get(),
            'stock': main_book_info.xpath('.//p[@class="instock availability"]/text()').get(),
            'rating': main_book_info.xpath('p[3]/@class').get(),
            'UPC': response.xpath('//th[contains(text(), "UPC")]/following-sibling::td[1]/text()').get(),
            'review': response.xpath('//th[contains(text(), "Number of reviews")]/following-sibling::td[1]/text()').get()
        }