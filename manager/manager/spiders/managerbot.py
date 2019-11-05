# -*- coding: utf-8 -*-
import scrapy


class ManagerbotSpider(scrapy.Spider):
    name = 'managerbot'
    allowed_domains = ['manager.com.br']
    start_urls = ['http://manager.com.br/empregos-desenvolvedor-javascript/']

    def parse(self, response):

        items = response.xpath('//*[@id="resultado-busca-vagas"]')
        for item in items:

            url = item.xpath('.//header[contains(@class, "titulo")]//h2//a[contains(@class, "permalink")]/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detalhes)

            next_page = response.xpath('//div[contains(@class, "pagination pagination-centered hidden-print")]//ul//li[contains(@title, "Vagas de Emprego de Desenvolvedor Javascript - Página Seguinte")]//a[contains(@class, "next nofollow")]/@href').extract()
            
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)

            

    def parse_detalhes(self, response):


        items = response.xpath('//div[contains(@class, "conteudo-principal")]//div[contains(@class, "row")]//div[contains(@class, "span8")]//article[contains(@class, "vaga hlisting")]')
        titulo = items.xpath('//header[contains(@class, "page-header")]//h1[contains(@class, "pull-left item offer announce fn")]/text()').extract_first()
        desc = items.xpath('//div[contains(@class, "description")]/text()').extract_first()
        salario = items.xpath('//div[contains(@class, "sub-item")]/text()').extract_first()
        #local = items.xpath('//div[1]//dl[contains(@class, "location adr")]//dd[contains(@class, "clear-none")]//span[contains(@class, "locality")]//text()').extract_first()
        
        yield{
            titulo,
            desc,
            items,
            salario
        }