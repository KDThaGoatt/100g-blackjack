from x01_deck import createDeck
from x02_value import value
from x03_bust import busts
from x04_dealer import dealer
import random

deck = createDeck()

dealerhand = dealer(deck)

if busts(dealerhand[1]) == True:
    print("Dealer busted! You win!")


deck = deck.remove(dealerhand)

playerhand = dealer(deck)

if busts(playerhand[1]) == True:
    print("Busted, you lose.")
else:
    