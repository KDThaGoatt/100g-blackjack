from x01_deck import createDeck
from x02_value import value
from x03_bust import busts
from x04_dealer import dealer
import random

# make a deck of cards
deck = createDeck()

# deal the dealers hand
dealerhand = dealer(deck)

# check if the dealer busted
if busts(dealerhand[1]) == True:
    print("Dealer busted! You win!")

# remove cards from the deck based off the dealers hand 
for card in dealerhand:
    if card in deck:
        deck.remove(card)

# deal the players hand
playerhand = dealer(deck)

# check if the player has busted
if busts(playerhand[1]) == True:
    print("Busted, you lose.")
else:
    print (playerhand)