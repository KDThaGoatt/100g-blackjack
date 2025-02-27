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
  endVal = 0
  ace_count = 0

  for card in hand:
    if card[0] == '2':
      cardVal = 2
    elif card[0] == '3':
      cardVal = 3
    elif card[0] == '4':
        cardVal = 4
    elif card[0] == '5':
      cardVal = 5
    elif card[0] == '6':
      cardVal = 6
    elif card[0] == '7':
      cardVal = 7
    elif card[0] == '8':
      cardVal = 8
    elif card[0] == '9':
      cardVal = 9
    elif card[0] == 'T':
      cardVal = 10
    elif card[0] == 'J':
      cardVal = 10
    elif card[0] == 'Q':
      cardVal = 10
    elif card[0] == 'K':
      cardVal = 10
    elif card[0] == 'A':
      ace_count += 1
      cardVal = 11  # Initially consider Ace as 11
    else:
      print("Invalid card")
      continue

    endVal += cardVal

    # Adjust for Aces if total value exceeds 21
  while endVal > 21 and ace_count > 0:
    endVal -= 10
    ace_count -= 1

  # Return a list if there are Aces in the hand
  if ace_count > 0:
      return [endVal - (10 * ace_count), endVal]  # Return both possible values

  return endVal



def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__main__":
  main()
