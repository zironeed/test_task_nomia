from copy import deepcopy


class ATM(object):

    def __init__(self):
        self.cash = {10: 0, 50: 0, 100: 0, 200: 0, 500: 0}

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i, banknote in enumerate(self.cash):
            self.cash[banknote] += banknotesCount[i]

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        res, cash = [], deepcopy(self.cash)

        for banknote in list(cash.keys())[::-1]:
            banknote_count = amount // banknote

            if amount == 0 or banknote_count == 0 or banknote_count > cash[banknote]:
                res.append(0)
                continue

            amount -= banknote_count * banknote
            cash[banknote] -= banknote_count
            res.append(banknote_count)

        if amount > 0:
            return [-1]

        self.cash = cash
        return res[::-1]


atm = ATM()
atm.deposit([0,0,1,2,1])
print(atm.withdraw(600)) # [0,0,1,0,1]
atm.deposit([0,1,0,1,1])
print(atm.withdraw(600)) # [-1]
print(atm.withdraw(550)) # [0,1,0,0,1]
