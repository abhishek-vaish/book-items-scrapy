from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import BookItem


class BookSpider(CrawlSpider):
    name = "bookscraper"
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(
            LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_items"
        ),
    )

    def parse_items(self, response):
        book_item = BookItem()

        book_item['title'] = response.css(".product_main > h1::text").get()
        book_item['price'] = response.css(".product_main > .price_color::text").get()
        book_item['upc'] = response.css(
            ".table.table-striped > tr:nth-child(1) > td::text"
        ).get()
        book_item['category'] = response.css(
            ".breadcrumb > li:nth-child(3) > a::text"
        ).get()
        book_item['image_url'] = response.urljoin(
            response.css(".item.active > img::attr(src)").get()
        )
        book_item['url'] = response.url
        book_item['available'] = response.css(
            ".table.table-striped > tr:nth-child(6) > td::text"
        ).get()

        return book_item
