import requests 
from requests import Session 
import secrets 
from pprint import pprint as pp
#https://coinmarketcap.com/api/documentation/v1/

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
  
}


r = requests.get(url, headers=headers)

class CMC:
  def __init__(self, token):
      self.apiurl = 'https://pro-api.coinmarketcap.com'
      self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': token,}
      self.session = Session()
      self.session.headers.update(self.headers)

  def getAllCoins(self):
      url = self.apiurl + '/v1/cryptocurrency/map'
      r = self.session.get(url)
      data = r.json()['data']
      return data

  def getPrice(self, symbol):
      url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
      parameters = {'symbol': symbol}
      r = self.session.get(url, params=parameters)
      data = r.json()['data']
      return data
      

cmc = CMC(secrets.API_KEY)

# pp(cmc.getPrice('ETH'))

# ethPrice = cmc.getPrice('ETH')
# pp(ethPrice["ETH"]["quote"]["USD"]["price"])

# btcPrice = cmc.getPrice("BTC")
# pp(btcPrice["BTC"]["quote"]["USD"]["price"])

# bnbPrice = cmc.getPrice("BNB")
# pp(bnbPrice["BNB"]["quote"]["USD"]["price"])


