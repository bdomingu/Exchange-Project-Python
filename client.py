from cmcApi import cmc

from pprint import pprint as pp

ethPrice = cmc.getPrice('ETH')
ethereumPrice = (ethPrice["ETH"]["quote"]["USD"]["price"])

btcPrice = cmc.getPrice("BTC")
bitcoinPrice = (btcPrice["BTC"]["quote"]["USD"]["price"])

bnbPrice = cmc.getPrice("BNB")
BNBPrice = (bnbPrice["BNB"]["quote"]["USD"]["price"])

usdWallet = 2000


class Client:
    def updateBTCBalance(x, bool):
        purchase = bool 

        if purchase:
            btcBalance = x/bitcoinPrice
            return btcBalance

        else: 
            BTCSellPrice = x * bitcoinPrice
            return BTCSellPrice
    
    def updateETHBalance(x, bool):
        purchase = bool
        if purchase:
            ETHBalance = x/ethereumPrice
            return ETHBalance

        else: 
            ETHSellPrice = x * ethereumPrice
            return ETHSellPrice

    def updateBNBBalance(x, bool):
        purchase = bool
        if purchase:
            BNBBalance = x/BNBPrice
            return BNBBalance

        else: 
            BNBSellPrice = x * BNBPrice
            return BNBSellPrice


    def updateUSDBalance(y, input):
            transaction = input

            if transaction == 'buy':
                USDBal1 = usdWallet - y
                return USDBal1
            
            elif transaction == "sellBTC":
                USDBal2 = usdWallet + (y * bitcoinPrice)
                return USDBal2

            elif transaction == "sellETH":
                USDBal3 = usdWallet + (y * ethereumPrice)
                return USDBal3

            elif transaction == "sellBNB":
                USDBal4 = usdWallet + (y * BNBPrice)
                return USDBal4
            return y



    



         



         


   

