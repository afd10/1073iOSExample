import Card

class Hand(object):
    def __init__(self):
        self.hand = []

    def addCard(self,aCard):
        self.hand.append(aCard)

    def showHand(self):
        for card in self.hand:
            card.display()

    def total(self):
        totalval = 0
        for card in self.hand:
            if card.value == 'A':
                if (totalval + 11) < 22:
                    totalval = totalval + 11
                else:
                    totalval = totalval + 1
            else:
                totalval += card.value
        return totalval

