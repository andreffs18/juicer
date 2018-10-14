import scrapy
from urllib.parse import urlparse
from juicer.services.get_html_content_service import GetContentFromHtmlService


class WebsiteDataSpider(scrapy.Spider):
    name = "spider"

    def __init__(self, start_url=None, *args, **kwargs):
        super(WebsiteDataSpider, self).__init__(*args, **kwargs)
        if not start_url:
            raise ValueError("'start_url' is required")

        self.start_urls = [start_url]
        self.allowed_domains = [urlparse(start_url).netloc.replace("www.", "")]

    def parse(self, response):
        yield {'body': GetContentFromHtmlService(response.body).call()}

        for href in response.css('a::attr(href)'):
            self.log(href)
            yield response.follow(href, callback=self.parse)
