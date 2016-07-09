import datetime
import json
from connector import connector

class orderbook:
    """Classe que encapsula as orders book do Mercado bitcoin """
    oid = -1
    coin_type = "b"
    order_type = ""
    price = -1
    num_coins = -1
    date_creation = datetime.datetime.now()
    date_not_avaible = None

    # Constantes
    nome_tabela = "orderbook"

    def __init__(self, string, coin_type = "b", to_update = True):
        
        arrayList = []

        totalQuery = ""

        d = json.loads(string);
        for i in d['asks']:
            self.price= i[0]
            self.num_coins = i[1]
            self.order_type =  'a'
            self.coin_type = coin_type

            dic = self.get_open_order(self.coin_type,self.order_type,self.num_coins,self.price)
            boolExist = len(dic) != 0
            if to_update == True and not boolExist:
                totalQuery += self.update(True)
            elif boolExist:
                arrayList.append(dic[0][0])
        
            
        for i in d['bids']:
            self.price= i[0]
            self.num_coins = i[1]
            self.order_type =  'b'
            self.coin_type = coin_type

            dic = self.get_open_order(self.coin_type,self.order_type,self.num_coins,self.price)
            boolExist = len(dic) != 0
            if to_update == True and not boolExist:
                totalQuery += self.update(True)
            elif boolExist:
                arrayList.append(dic[0][0])
        
        self.close_old_orders(arrayList)

        if len(totalQuery) > 0:
            myConn = connector()
            myConn.crud(totalQuery)

    def update (self, retString = False):
        
        myConn = connector()        
        query = "INSERT INTO " + self.nome_tabela + " (order_type,price,num_coins,coin_type,date_creation) values (" + repr(self.order_type) + "," + repr(self.price) + "," + repr(self.num_coins) + "," + repr(self.coin_type) + ",TIMESTAMP '" + self.date_creation.strftime('%Y-%m-%d %H:%M:%S') + "');"

        if not retString:
            myConn.crud(query)
        else:
            return query
    

    def get_open_order(self, coin_type , order_type , num_coins, price ):
        query = "select * from " + self.nome_tabela + " where "
        query += "coin_type = '" + coin_type + "'"
        query += " and order_type = '" + order_type + "'"
        query += " and price = '" + repr(price) + "'"
        query += " and num_coins = '" + repr(num_coins) + "'"
        query += " and date_not_avaible is null "

        myConn = connector()
        return myConn.execute(query)

    def exists (self):
        d = self.get_open_order(self.coin_type,self.order_type,self.num_coins,self.price)
        return d == None 

    def close_old_orders(self, array_open_orders):


        if len(array_open_orders) == 0:
            return

        placeholder = "?"
        placeholders = ", ".join(placeholder for unsed in array_open_orders)
        
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        
        query = "UPDATE " + self.nome_tabela + " set date_not_avaible = "
        query += "TIMESTAMP '" + now
        query += "' where date_not_avaible is NULL and coin_type = '" + self.coin_type  + "' and oid not in (%s)"
        new_query = query % placeholders

        for i in array_open_orders:
            new_query = new_query.replace("?",repr(i),1)

        myConn = connector()
        myConn.crud(new_query)
