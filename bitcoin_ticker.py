import datetime
import json
from connector import connector

class bitcoin_ticker:
    """Classe que encapsula o thicker do Mercado bitcoin em determinado instante"""
    high = -1
    low = -1
    vol = -1
    last = -1
    buy = -1
    sell = -1
    date = -1
    dateCreation = datetime.datetime.now()

    # Constantes
    nome_tabela = "bitcoin_ticker"

    def __init__(self, string):
        d = json.loads(string);
        cte_ticker = 'ticker'
        self.high = d[cte_ticker]['high']
        self.low = d[cte_ticker]['low']
        self.vol = d[cte_ticker]['vol']
        self.last = d[cte_ticker]['last']
        self.buy = d[cte_ticker]['buy']
        self.sell = d[cte_ticker]['sell']
        self.date = d[cte_ticker]['date']

    def update (self):
        
        myConn = connector()        
        query = "INSERT INTO " + self.nome_tabela + " (high,low,vol,last,buy,sell,date) values (" + repr(self.high) + "," + repr(self.low) + "," + repr(self.vol) + "," + repr(self.last) + "," + repr(self.buy) + "," + repr(self.sell) + ",TIMESTAMP '" + datetime.datetime.fromtimestamp(self.date).strftime('%Y-%m-%d %H:%M:%S') + "');"
        myConn.crud(query);
    
    
