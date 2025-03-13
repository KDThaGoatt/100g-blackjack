from x01_deck import createDeck
from x03_bust import busts
from x04_dealer import dealer
from playerdeck import player

contBool = True

while contBool == True:
    # make a deck of cards
    deck = createDeck()

    # deal the dealers hand
    dealerHand = dealer(deck)

    # check if the dealer busted
    if busts(dealerHand[1]) == True:
        print("\033[0;32mDealer busted! You win!\033[0m")
        cont = input("Keep playing? Y/N: ")
        if cont == "Y" or cont =="y":
            contBool = True
        else:
            contBool = False
    
    if busts(dealerHand[1]) == False:
        # remove cards from the deck based off the dealers hand 
        deck = dealerHand[2]
        print(f"The dealer has {dealerHand[1]}")

        # deal the players hand
        playerhand = player(deck)

        # check if the player has busted
        if busts(playerhand) == True:
            print(f"\033[0;31mBusted, you lose. Your score was {playerhand}\033[0m")
            cont = input("Keep playing? Y/N: ")
            if cont == "Y" or cont =="y":
                contBool = True
            else:
                contBool = False
        else:
            if playerhand > dealerHand[1] and playerhand != 21:
                print(f"\033[0;32mYou have {playerhand}, dealer has {dealerHand[1]}, you win!\033[0m")
                cont = input("Keep playing? Y/N: ")
                if cont == "Y" or cont =="y":
                    contBool = True
                else:
                    contBool = False
            elif playerhand > dealerHand[1] and playerhand == 21:
                print(f"\033[0;32mBlackjack!, you win!\033[0m")
                cont = input("Keep playing? Y/N: ")
                if cont == "Y" or cont =="y":
                    contBool = True
                else:
                    contBool = False
            elif playerhand < dealerHand[1] and dealerHand[1] == 21:
                print(f"\033[0;31mDealer got Blackjack, you lose.\033[0m")
                cont = input("Keep playing? Y/N: ")
                if cont == "Y" or cont =="y":
                    contBool = True
                else:
                    contBool = False
            elif playerhand < dealerHand[1]:
                print(f"\033[0;31mYou have {playerhand}, dealer has {dealerHand[1]}, you lose.\033[0m")
                cont = input("Keep playing? Y/N: ")
                if cont == "Y" or cont =="y":
                    contBool = True
                else:
                    contBool = False
            else:
                print(f"\033[1;33mYou have {playerhand}, dealer also has {dealerHand[1]}, push\033[0m")
                cont = input("Keep playing? Y/N: ")
                if cont == "Y" or cont =="y":
                    contBool = True
                else:
                    contBool = False
            