import scrapy
from scrapy_selenium import SeleniumRequest
from time import sleep
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector

class LuxuryWatchSpider(scrapy.Spider):
    name = 'luxury_watch'

    def start_requests(self):
        yield SeleniumRequest(
            url='http://antenna.jp/',
            wait_time=3,
            screenshot=False,
            callback=self.parse
        )

    def parse(self, response):
        driver = response.meta['driver']

        search_text = driver.find_element_by_xpath('//input[@id="search-input"]')
        # search_text = driver.find_element_by_css_selector('input#search-input')
        search_text.send_keys('高級時計')
        search_button = driver.find_element_by_xpath('//input[@id="search-button"]')
        search_button.submit()
        sleep(3)

        scroll_count = 20
        for i in range(scroll_count):
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            sleep(1)

        w = driver.execute_script('return document.body.scrollWidth')
        h = driver.execute_script('return document.body.scrollHeight')
        driver.set_window_size(w, h)
        driver.save_screenshot('antenna.png')

        html = driver.page_source
        selector = Selector(text=html)

        watches = selector.xpath('//div[@class="article-view feed-article-view album-article"]')

        for watch in watches:
            yield{
                'title': watch.xpath('.//div[@class="title"]/text()').get(),
                'URL': watch.xpath('.//a[@class="thumbnail-content"]/@href').get()
            }