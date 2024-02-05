class ATMCard:
    def __init__(self, defaultPIN, defaultBalance):
        self.defaultPIN = defaultPIN
        self.defaultBalance = defaultBalance
        pass
    def CekPinAwal(self):
        return self.defaultPIN
    def CekSaldoAwal(self):
        return self.defaultBalance
        