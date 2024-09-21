import scrapy
from scrapy_selenium import SeleniumRequest
from time import sleep
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector

class GooglePythonSpider(scrapy.Spider):
    name = 'google_python'

    def start_requests(self):
        yield SeleniumRequest(
            url='http://www.google.com/?hl=ja',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        driver = response.meta['driver']
        driver.save_screenshot('01_open_google.png')

        # search_bar = driver.find_element_by_xpath('//input[@name="q"]')
        search_bar = driver.find_element_by_xpath('//textarea[@name="q"]')
        search_bar.send_keys('python')
        sleep(1)
        driver.save_screenshot('02_after_input.png')

        search_bar.send_keys(Keys.ENTER)
        sleep(3)
        w = driver.execute_script('return document.body.scrollWidth')
        h = driver.execute_script('return document.body.scrollHeight')
        driver.set_window_size(w, h)
        driver.save_screenshot('03_after_enter.png')    

        # html = driver.page_source
        # sel = Selector(text=html)

        # for elem in sel.xpath('//div[@class="g"]'):
        #     yield{
        #         'title': elem.xpath('.//h3/text()').get(),
        #         'URL': elem.xpath('.//h3/parent::a/@href').get()
        #     }

        yield SeleniumRequest(
            url=driver.current_url,
            wait_time=3,
            callback=self.parse_next
        )

    def parse_next(self, response):
        driver = response.meta['driver']
        # html = driver.page_source
        # sel = Selector(text=html)

        # Googleのページ変更に伴う修正
        # for elem in response.xpath('//div[@class="g"]'):
        #     yield{
        #         'title': elem.xpath('.//h3/text()').get(),
        #         'URL': elem.xpath('.//h3/parent::a/@href').get()
        #     }
        for elem in response.xpath('//h3/parent::a'):
            yield{
                'title': elem.xpath('.//child::h3/text()').get(),
                'URL': elem.xpath('.//@href').get()
            }


        next_page = response.xpath('//a[@id="pnnext"]/@href').get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield SeleniumRequest(
                url=next_url,
                wait_time=1,
                callback=self.parse_next
            )