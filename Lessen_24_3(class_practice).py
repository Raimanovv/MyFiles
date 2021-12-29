class Family:
    Family_name = 'Common family'
    Family_funds = 100000
    Having_a_house = False

    def info(self):
        print('Family name: {}\nFamily funds: {}\nHaving a house: {}'.format(
            self.Family_name, self.Family_funds, self.Having_a_house)
        )

    def earn_funds(self, earn):
        self.Family_funds += earn
        print('Earned {} money! Current value: {}'.format(
            earn, self.Family_funds)
        )

    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        print('\nTry to buy a house')
        if self.Family_funds >= price:
            self.Family_funds -= price
            print('House purchased! Current money: {}\n'.format(
                self.Family_funds)
            )
            self.Having_a_house = True
        else:
            print('Not enough money!\n')

family1 = Family()
family1.info()
family1.buy_house(1000000)
family1.earn_funds(10 ** 7)
family1.buy_house(1000000, 59)
family1.info()