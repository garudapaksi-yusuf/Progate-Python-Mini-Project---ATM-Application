from atm_card import ATMCard

class Customer:
    def __init__(self, ID, custPIN = 1234, custBalance = 10000):
        self.ID = ID
        self.custPIN = custPIN
        self.custBalance = custBalance
        pass
    def CekIdCust(self):
        return self.ID
    def CekPinCust(self):
        return self.custPIN
    def CekSaldoCust(self):
        return self.custBalance
    def Debet(self, nominal):
        self.nominal -= nominal
    def Simpan(self, nominal):
        self.nominal += nominal

