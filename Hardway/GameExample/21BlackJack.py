import Deck
import Hand

cards = Deck.Deck()

def showHands():
    print "Dealer's Hand:"
    dealer.showHand()
    print "\nPlayer's Hand:"
    player.showHand()

def findWinner(player, dealer):
    ptotal = player.total()
    dtotal = dealer.total()
    print "Player: ", ptotal
    print "Dealer: ", dtotal
    if ptotal > 21:
        print "Player busts.  House wins."
    elif dtotal >21:
        print "House busts.  Player wins."
    elif dtotal >= ptotal:
        print "House wins."
    else: 
        print "Player wins!"
    


#cards.display()
cards.shuffle()

dealer = Hand.Hand()
player = Hand.Hand()

dealer.addCard(cards.dealACard())
dealer.addCard(cards.dealACard())

player.addCard(cards.dealACard())
player.addCard(cards.dealACard())

showHands()
player.total()

playerOn = True
dealerOn = True


while playerOn or dealerOn:
    print "hit (h) or stay (s)"
    choice = raw_input("> ")
    if dealer.total() < 15 and dealerOn:
        dealer.addCard(cards.dealACard())
        if dealer.total() > 21:
            dealerOn = False
    else:
        dealerOn = False
    if choice =='h':
        player.addCard(cards.dealACard())
        if player.total() > 21:
            playerOn = False
    if choice =='s':
        print "Player stays."
        playerOn = False

    showHands()
findWinner(player, dealer)
