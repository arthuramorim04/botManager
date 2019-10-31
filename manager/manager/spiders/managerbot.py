# -*- coding: utf-8 -*-
import scrapy


class ManagerbotSpider(scrapy.Spider):
    name = 'managerbot'
    allowed_domains = ['manager.com.br']
    start_urls = ['http://manager.com.br/empregos-desenvolvedor-javascript/']            

    def parse(self, response):

        items = response.xpath('//*[@id="resultado-busca-vagas"]')
        #items = response.xpath('.//div[contains(@class, "lista-resultado-busca)]//article]contains(@class, "vaga_hlisting")')
        for item in items:

            titulo = item.xpath('.//header[contains(@class, "titulo")]//h2//a[contains(@class, "permalink")]//mark/text()').extract()
            descricao = item.xpath('.//p[contains(@class, "descricao description")]/text()').extract()
            salario = item.xpath('.//header[contains(@class, "titulo")]//small[contains(@class, "pull-right")]//span/text()').extract() #pega faixa salarial
            cidade = item.xpath('.//footer[contains(@class, "rodape")]//span[contains(@class, "localidade linha-rodape-vaga location adr")]//a[contains(@class, "cidade locality")]//span/text()').extract() #pega cidade
            estado = item.xpath('.//footer[contains(@class, "rodape")]//span[contains(@class, "localidade linha-rodape-vaga location adr")]//a[contains(@class, "uf region")]//span/text()').extract() #pega cidade
        
        #next_page = items.xpath('/footer/div[contains(@class, "pagination pagination-centered hidden-print")]/ul/li[contains(@title, "Vagas de Emprego de Desenvolvedor Javascript - Última Página")]/a').extract()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
            
        self.log(titulo)
        self.log(descricao)
        self.log(salario)
        self.log(cidade)
        self.log(estado)
        self.log(next_page)


