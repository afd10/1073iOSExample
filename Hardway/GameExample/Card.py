class Card(object):
    def __init__(self, suit, pips, value):
        self.suit = suit
        self.pips = pips
        self.value = value

    def display(self):
        print self.suit, self.pips
