import datetime
import json
from connector import connector
import pdb

class trade:
    """Classe que encapsula uma transacao do Mercado bitcoin """
    price = -1
    amount = -1
    type_trade = ""
    date = -1
    trade_id = -1
    coin_type = ""

    # Constantes
    nome_tabela = "trade"

    def __init__(self, string,  coin_type = "b", to_update = True):

        #pdb.set_trace()
        
        d = json.loads(string);
        for j in d:
    
            self.price = j['price']
            self.amount= j['amount']
            self.type_trade = j['type']
            self.date = j['date']
            self.trade_id = j['tid']
            self.coin_type = coin_type
            
            

            if to_update == True and not self.exists():
                self.update()

    def update (self):
        
        myConn = connector()        
        query = "INSERT INTO " + self.nome_tabela + " (tid,price,amount,type,date,coin_type) values (" + repr(self.trade_id) + "," + repr(self.price) + "," + repr(self.amount) + "," + repr(self.type_trade) + ",TIMESTAMP '" + datetime.datetime.fromtimestamp(self.date).strftime('%Y-%m-%d %H:%M:%S') + "','" + self.coin_type  + "');"
        myConn.crud(query);
    
    def exists (self):
        
        query = "select * from " + self.nome_tabela + " where tid = '" + repr(self.trade_id) + "' and coin_type = '" + self.coin_type  + "';"
        myConn = connector()
        d = myConn.execute(query)
        return len(d) > 0
