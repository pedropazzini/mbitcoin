#!/usr/bin/python

import pycurl
from bitcoin_ticker import bitcoin_ticker
from trade import trade
from orderbook import orderbook
import pdb
import io

#h = httplib2.Http(".cache")

#link_thicker = "https://www.mercadobitcoin.com.br/api/ticker/"
#t = json.loads(content.decode("utf-8"))
#t = bitcoin_ticker(content.decode("utf-8"))
#t.update();


# TO DEBUG
#pdb.set_trace()

link_thicker = "https://www.mercadobitcoin.com.br/api/trades/"
c = pycurl.Curl()
c.setopt(c.URL,link_thicker)
storage = io.BytesIO()
c.setopt(c.WRITEFUNCTION,storage.write)
c.perform()
c.close()
content = storage.getvalue().decode("utf-8") 
tr = trade(content)

link_thicker = "https://www.mercadobitcoin.com.br/api/orderbook/"
c = pycurl.Curl()
c.setopt(c.URL,link_thicker)
storage = io.BytesIO()
c.setopt(c.WRITEFUNCTION,storage.write)
c.perform()
c.close()
content = storage.getvalue().decode("utf-8") 
order = orderbook(content)

link_thicker = "https://www.mercadobitcoin.com.br/api/trades_litecoin/"
c = pycurl.Curl()
c.setopt(c.URL,link_thicker)
storage = io.BytesIO()
c.setopt(c.WRITEFUNCTION,storage.write)
c.perform()
c.close()
content = storage.getvalue().decode("utf-8") 
tr = trade(content,"l")

link_thicker = "https://www.mercadobitcoin.com.br/api/orderbook_litecoin/"
c = pycurl.Curl()
c.setopt(c.URL,link_thicker)
storage = io.BytesIO()
c.setopt(c.WRITEFUNCTION,storage.write)
c.perform()
c.close()
content = storage.getvalue().decode("utf-8") 
order = orderbook(content,"l")
