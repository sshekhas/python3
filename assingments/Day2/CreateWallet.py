def createWallet(balance, user):

    def deposite(amount):
        nonlocal balance
        balance = balance+amount
        print("--------------------")
        print(amount, " Amount deposited by " + user)
        print("Total balance " + str(balance))
        print("--------------------")

    def withdraw(amount):
        nonlocal balance
        balance = balance - amount
        print(amount, " Amount withdrawn by " + user)
        print("Total balance " + str(balance))
        print("--------------------")

    def showBalance():
        print("Total balance of " + user + str(balance))

    def fundsTransfer(amount, wallet, name):
        nonlocal balance
        balance = balance - amount
        print(amount, " is transferred to " + name)
        wallet[0](amount)
        print("--------------------")

    return [deposite, withdraw, showBalance, fundsTransfer]


paytm = createWallet(43000, " John ")
phonePe = createWallet(50000, " Brad ")

paytm[0](5000)
paytm[1](5000)
paytm[2]()
paytm[3](2500, phonePe, "phonePe")
phonePe[2]()
paytm[2]()