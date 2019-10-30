# -*- coding: utf-8 -*-
import scrapy
from manager.items import ManagerItem


class ManagerbotSpider(scrapy.Spider):
    name = 'managerbot'
    allowed_domains = ['manager.com.br/empregos-desenvolvedor-javascript']
    start_urls = ['http://manager.com.br/empregos-desenvolvedor-javascript/']

    def parse(self, response):

        items = response.xpath('.//div[contains(@class, "lista-resultado-busca)]//article]contains(@class, "vaga hlisting")')
        for item in items:
            titulo_vaga = item.xpath('.//a[contains(@class, "permalink")]/text()').extract_first() #Pega titulo real da vaga
            descricao = item.xpath('.//p[contains(@class, "descricao description")]/text()').extract()
            salario = item.xpath('.//small[contains(@class, "faixa-salarial muted")]//title()').extract() #pega faixa salarial
            cidade = item.xpath('.//footer[contains(@class, "rodape")]//span[contains(@class, "localidade linha-rodape-vaga location adr")]//a[contains(@class, "cidade locality")]//span/text()').extract() #pega cidade
            estado = item.xpath('.//footer[contains(@class, "rodape")]//span[contains(@class, "localidade linha-rodape-vaga location adr")]//a[contains(@class, "uf region")]//span/text()').extract() #pega cidade

        next_page_url = response.xpath('//div[contains(@class, "pagination pagination-centered hidden-print")]//li[contains(@title, Vagas de Emprego de Desenvolvedor Javascript - Página Seguinte")]/@href').extract()
        if next_page_url:
            next_page = 'http://manager.com.br/empregos-desenvolvedor-javascript/' + next_page_url
            yield scrapy.Request(url = next_page, callback = self.parse)
