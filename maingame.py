from x01_deck import createDeck
from x02_value import value
from x03_bust import busts
from x04_dealer import dealer
import random

#while cont == True:
if __name__ == "__main__":
    # make a deck of cards
    deck = createDeck()

    # deal the dealers hand
    dealerHand = dealer(deck)

    # check if the dealer busted
    if busts(dealerHand[1]) == True:
        print("\033[0;32mDealer busted! You win!\033[0m")
    
    if busts(dealerHand[1]) == False:
        # remove cards from the deck based off the dealers hand 
        deck = dealerHand[2]

        # deal the players hand
        playerhand = dealer(deck)

        # check if the player has busted
        if busts(playerhand[1]) == True:
            print(f"Busted, you lose. Your score was {playerhand[1]}")
        else:
            if playerhand[1] > dealerHand[1]:
                print(f"\033[0;32mYou have {playerhand[1]}, dealer has {dealerHand[1]}, you win!\033[0m")
            elif playerhand[1] < dealerHand[1]:
                print(f"You have {playerhand[1]}, dealer has {dealerHand[1]}, you lose.")
            else:
                print(f"You have {playerhand[1]}, dealer also has {dealerHand[1]}, push")
            