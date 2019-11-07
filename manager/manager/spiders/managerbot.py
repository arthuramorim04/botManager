# -*- coding: utf-8 -*-
import scrapy


class ManagerbotSpider(scrapy.Spider):
    name = 'managerbot'
    allowed_domains = ['manager.com.br']
    start_urls = ['http://manager.com.br/empregos-desenvolvedor-javascript/']

    def parse(self, response):

        items = response.xpath('//div[@class="lista-resultado-busca"]/article[@class="vaga hlisting"]/header[@class="titulo"]')
        for item in items:
            #fazer a xpath mais completa pra tentar otimizar o tempo de processamento
            url = items.xpath('./h2[@class="cargo item offer announce fn"]/a[@class="permalink"]/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detalhes)

            next_page = items.xpath('//div[contains(@class, "pagination pagination-centered hidden-print")]//a[@rel="next nofollow"]/@href').extract_first()
            if next_page:
                #self.log('Next Page: {0}'.format(next_page))
                yield scrapy.Request(url=next_page, callback=self.parse)

            

    def parse_detalhes(self, response):

        titulo = response.xpath('//body//div[@class="container"]//article[@class="vaga hlisting"]//header[@class="page-header"]/h1[@class="pull-left item offer announce fn"]/span/text()').extract_first()
        cidade = response.xpath('//body//div[@class="container"]//article[@class="vaga hlisting"]//dl[@class="location adr"]/dd[@class="clear-none"]/span/text()').extract_first()
        salario = response.xpath('//body//div[@class="container"]//article[@class="vaga hlisting"]//div[@class="sub-item"]/dl/dd/text()').extract_first()
        desc = response.xpath('//body//div[@class="container"]//article[@class="vaga hlisting"]//div[@class="description"]/p/text()').extract_first()
        
        yield{
            'titulo' : titulo,
            'Cidade' : cidade,
            'salario' : salario,
            'descricao' : desc
        }