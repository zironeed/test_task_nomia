from copy import deepcopy


def validate(banknotes=None, amount=None):
    maximum = 10 ** 9

    if banknotes:

        if len(banknotes) != 5:
            raise Exception('Error: banknotesCount length must be 5')

        for banknote in banknotes:
            if banknote < 0 or banknote > maximum:
                raise Exception('Error: Banknote value must be between 0 and 10^9')

        return banknotes

    if amount < 1 or (amount >= maximum):
        raise Exception('Error: Amount must be at least 1')

    return amount


class ATM(object):

    def __init__(self):
        self.cash = {10: 0, 50: 0, 100: 0, 200: 0, 500: 0}

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        banknotesCount = validate(banknotes=banknotesCount)

        for i, banknote in enumerate(self.cash):
            self.cash[banknote] += banknotesCount[i]

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        res, cash = [], deepcopy(self.cash)
        amount = validate(amount=amount)

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


if __name__ == '__main__':
    atm = ATM()
    atm.deposit([0, 0, 1, 2, 1])
    print(atm.withdraw(600))
    atm.deposit([0, 1, 0, 1, 1])
    print(atm.withdraw(600))
    print(atm.withdraw(550))
