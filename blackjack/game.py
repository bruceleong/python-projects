import random

# Hearts, Diamonds,Clubs,Spades
suits = ('H','D','C','S')

# Possible card ranks
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Point values dict (Note: Aces can also be 11, check self.ace for details)
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

playing = True

class Card():
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return self.rank+ " of " +self.suit
