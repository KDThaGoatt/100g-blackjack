#!python3

"""
Create a list of cards
the cards should be denoted with a number or A, J, Q, K, T (for ace, jack, queen, king or ten)
as well as a suit
"""

import random

def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  deck = []
  
  for suit in suits:
    for rank in ranks:
      deck.append(rank + suit)

  random.shuffle(deck)

  return deck
  
  '''
  use the two lists to create a new list "deck" 
  return the deck list to your calling function
  '''

def main():
  deck = createDeck()
  assert "JH" in deck 
  assert "AC" in deck 
  assert "TD" in deck 
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()
