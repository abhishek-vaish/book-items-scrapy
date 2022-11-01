from scrapy import Item, Field


class BookItem(Item):
    title = Field()
    price = Field()
    upc = Field()
    category = Field()
    image_url = Field()
    url = Field()
    available = Field()

