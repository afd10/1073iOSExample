import random
import Card

class Deck(object):

    def __init__(self):
        suits = ["heart","club","diamond","spades"]
        pips = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        value = [2,3,4,5,6,7,8,9,10,10,10,10,"A"]
        self.deck = []
        
        for suit in suits:
	        i = 0
	        for pip in pips:
		        aCard = Card.Card(suit,pip,value[i])
		        i+=1
		        self.deck.append(aCard)
	        i=0

        print len(self.deck)


    def shuffle(self):
        random.shuffle(self.deck)

    def display(self):
        for card in self.deck:
            card.display()

    def dealACard(self):
        aCard = self.deck.pop()
        return aCard
