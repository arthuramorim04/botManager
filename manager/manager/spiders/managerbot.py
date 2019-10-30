# -*- coding: utf-8 -*-
import scrapy
from manager.items import ManagerItem


class ManagerbotSpider(scrapy.Spider):
    name = 'managerbot'
    allowed_domains = ['manager.com.br']
    start_urls = ['http://manager.com.br/empregos-desenvolvedor-javascript/']            

    def parse(self, response):

        items = response.xpath('//*[@id="resultado-busca-vagas"]')
        #items = response.xpath('.//div[contains(@class, "lista-resultado-busca)]//article]contains(@class, "vaga_hlisting")')
        for item in items:

            titulo = item.xpath('.//header[contains(@class, "titulo")]//h2[contains(@class, "permalink")]//mark/text()')
            descricao = item.xpath('.//p[contains(@class, "descricao description")]/text()').extract()
            salario = item.xpath('/html/body/div[4]/div/form/div[2]/section/div[2]/article[1]/header/small/span[1)').extract() #pega faixa salarial
            cidade = item.xpath('.//footer[contains(@class, "rodape")]//span[contains(@class, "localidade linha-rodape-vaga location adr")]//a[contains(@class, "cidade locality")]//span/text()').extract() #pega cidade
            estado = item.xpath('.//footer[contains(@class, "rodape")]//span[contains(@class, "localidade linha-rodape-vaga location adr")]//a[contains(@class, "uf region")]//span/text()').extract() #pega cidade

        self.log(titulo)
        self.log(descricao)
        self.log(salario)
        self.log(cidade)
        self.log(estado)


