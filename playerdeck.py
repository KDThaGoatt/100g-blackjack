#!python3

from x02_value import value

def player(deck):
    score = 0
    hitBool = True
    aceCount = 0
    aceBust = False

    while score < 21:
        for i in range(10):
            while hitBool == True:
                card = deck[i]
                print(card)
                if card[0] == "A" and aceBust == False:
                    score += 11
                    aceCount += 1
                elif card[0] == "A" and aceBust == True:
                    score += 1
                else:
                    score += value(card)

                
                if score > 21 and aceCount > 0:
                    score -= (10*aceCount)
                    aceBust = True
                    aceCount = 0
                if score > 21:
                    return score
                if score == 21:
                    return score
                deck.pop(i)
                hit = input(f"Your score is now {score}, would you like to hit again? Y/N: ")
                if hit != "Y" and hit != "y":
                    hitBool = False
                    return score