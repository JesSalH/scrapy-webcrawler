from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader

#Vamos a extraer info de stackoverflow

class Pregunta(Item):
    pregunta = Field()
    id = Field()

class StackOverflowSpider(Spider):
    name = "Scrapy Spider Test"
    start_urls = ['http://stackoverflow.com/']
    def parse(self, response):
        sel = Selector(resoponse)
        preguntas = sel.xpath('//div[@id="question-mini-list"]/div')

        #Recorremos preguntas
        for i, elem in enumerate(preguntas):
            item = ItemLoader(Pregunta(), elem)
            item.add_xpath('pregunta','.//h3/a/text()')
            item.add_value('id', i)
            yield item.load_item()
