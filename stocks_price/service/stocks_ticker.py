
import requests
from bs4 import BeautifulSoup
import pandas as pd

class StocksTicker(object):
    
    def __init__(self):
        self.base_url = "https://br.financas.yahoo.com/industries/"
        self.sectors = ["Energia-Petroleo-Gas", "Industria-Financeira","Saude-Farmaceutica","Telecomunicacoes-Tecnologia",
                  "Industria-Alimenticia","Industria-Manufatureira","Servicos-diversos", "Varejo","Construcao-Equipamentos",
                  "Bens-de-consumo","Industrias-em-geral"]
        
        
    def getAllTicker(self):
        list_of_ticker =  []
        for sector in self.sectors:
            url = self.base_url + sector
            html_text = requests.get(url).text
            html_page = BeautifulSoup(html_text, 'html.parser')
            tbody = html_page.find('tbody')
            rows = tbody.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                list_of_ticker.append({
                    "sector": sector,
                    "symbol": cells[0].text,
                    "name": cells[1].text,
                })
        return pd.DataFrame(list_of_ticker)