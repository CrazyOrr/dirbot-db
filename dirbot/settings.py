# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

ITEM_PIPELINES = {
    'dirbot.pipelines.RequiredFieldsPipeline': 1,
    'dirbot.pipelines.FilterWordsPipeline': 2,
    'dirbot.pipelines.DbPipeline': 3,
}

# Database settings
DB_API_NAME = 'MySQLdb'
DB_ARGS = {
    'host': 'localhost',
    'db': 'dirbot',
    'user': 'root',
    'passwd': '123',
    'charset': 'utf8',
    'use_unicode': True,
}
