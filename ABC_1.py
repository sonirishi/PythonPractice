import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = ['spades','hearts','clubs','diamonds']

    def __init__(self):
        self._cards = [Card(rank,suits) for rank in self.ranks for suits in self.suits]
    
    def __len__(self):
        return (len(self._cards))
    
    def __getitem__(self,position):
        return self._cards[position]
    
    def __setitem__(self,position,value): ## required for shuffle
        self._cards[position] = value
    
deck1 = FrenchDeck()
print(deck1.suits)

from random import shuffle

shuffle(deck1)
print(deck1[:3])