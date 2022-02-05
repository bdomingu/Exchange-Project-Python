from client import Client 

class Agent:
    def BuyBTC():
        print("This is the buy option:")
        print("Purchases $100 of BTC:", Client.updateBTCBalance(100, True))
        print("Purchases $55 of ETH:", Client.updateETHBalance(55, True))
        print("Purchases $55 of BNB:", Client.updateBNBBalance(55, True))
        print("Subtracts $150 from USD Wallet:", Client.updateUSDBalance(150, "buy"))


    def SellBTC():
        print("This is the sell option")
        print("Sells .6 BTC:", Client.updateBTCBalance(.6, False))
        print("Sells .2 ETH:", Client.updateETHBalance(.2, False))
        print("Sells .35 BNB:", Client.updateBNBBalance(.35, False))
        print("Sells .11 BTC and adds it to the USD Wallet:", Client.updateUSDBalance(.11, "sellBTC"))
        print("Sells .5 ETH and adds it to the USD Wallet:", Client.updateUSDBalance(.5, "sellETH"))
        print("Sells .02 BNB and adds it to the USD Wallet:", Client.updateUSDBalance(.02, "sellBNB"))
