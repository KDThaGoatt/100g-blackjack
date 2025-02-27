#!python3

def value(hand):
  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''
  endVal = []

  for i in range(11):
    
    if hand [i][0] == '2':
      cardVal = 2
    elif hand [i][0] == '3':
      cardVal = 3
    elif hand [i][0] == '4':
      cardVal = 4
    elif hand [i][0] == '5':
      cardVal = 5
    elif hand [i][0] == '6':
      cardVal = 6
    elif hand [i][0] == '7':
      cardVal = 7
    elif hand [i][0] == '8':
      cardVal = 8
    elif hand [i][0] == '9':
      cardVal = 9
    elif hand [i][0] == 'T':
      cardVal = 10
    elif hand [i][0] == 'J':
      cardVal = 10
    elif hand [i][0] == 'Q':
      cardVal = 10
    elif hand [i][0] == 'K':
      cardVal = 10
    elif hand[i][0] == 'A':
      if endVal >= 11:
        cardVal = 1
      else:
        cardVal = 11

    endVal = endVal + cardVal

  return endVal


def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()
