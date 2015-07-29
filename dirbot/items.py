from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class Website(Item):
    name = Field()
    description = Field()
    url = Field()


class WebsiteLoader(ItemLoader):
    default_item_class = Website
    default_output_processor = TakeFirst()
