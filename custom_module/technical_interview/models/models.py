# -*- coding: utf-8 -*-

from odoo import models, fields, api
from urllib.parse import urlparse, urlunparse

import requests
from bs4 import BeautifulSoup


class Publication(models.Model):
    _name = 'publications.postes'
    _description = 'technical_interview.publications.postes'

    name = fields.Char()
    link = fields.Char()
    publisher = fields.Char()
    date = fields.Char()
    asign_to = fields.Many2one('res.users')
    description = fields.Text()

    @api.model
    def scrape_add_pubs(self):
        postes_visee = self.env['postes.vises'].search([])
        for poste in postes_visee:
            url = poste.website
            poste_visee = poste.name
            response = requests.get(url)
            if response.status_code == 200:
                # Analyse the HTML contain of page
                soup = BeautifulSoup(response.content, "html.parser")
                # find all of pub on  page
                annonces = soup.find_all("article")
                for annonce in annonces:
                    title = annonce.find("h2").text
                    if poste_visee in str(title) :
                        parsed = urlparse(url)
                        # netloc attribute of parse result //www.tayara.tn
                        base = parsed.netloc
                        link = "http://" +base + annonce.find("a")['href']
                        res = requests.get(link)
                        soup_details = BeautifulSoup(res.content, "html.parser")
                        # find details pub
                        pub = soup_details.find_all("main")
                        publisher = pub[0].find("span").text
                        description = pub[0].find("p").text
                        vals = {'name': title,
                                'link': link,
                                'publisher': publisher,
                                'description' : description
                                }
                        self.create(vals)
            else:
                print("Échec de la requête")


