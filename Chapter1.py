# import collections

# Card = collections.namedtuple('Card',['rank','suit'])

# class FrenchDeck:
#     ranks = [str(n) for n in range(2,11)] + list('JQKA')
#     suits = ['spades','hearts','clubs','diamonds']

#     def __init__(self):
#         self._cards = [Card(rank,suits) for rank in self.ranks for suits in self.suits]
    
#     def __len__(self):
#         return (len(self._cards))
    
#     def __getitem__(self,position):
#         return self._cards[position]

# suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)

# def spades_high(card):
#     print(FrenchDeck.ranks)  ## this is the ranks list defined
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]
    
# FD = FrenchDeck()
# # print(f'Length {len(FD)}')
# # print(FD[3])

# from random import choice  ### works on a sequence, any one

# #print(choice(FD))

# # for cards in FD: ### becomes iterable because of getitem
# #     print(cards)

# #print(len(suit_values))

# for card in sorted(FD,key=spades_high): ## key is another function
#     print(card)

import math
class Vector:
    def __init__(self,x=0,y=0):
        self.xcoord = x
        self.ycoord = y

    def __add__(self,vec2):
        return Vector(self.xcoord+vec2.xcoord , self.ycoord+vec2.ycoord)
    
    def __repr__(self):
        return (f'Vector({self.xcoord!r},{self.ycoord!r})')  
        ## !r standard representation of attributes
    
    def abs(self):
        return math.hypot(self.x,self.y)
    
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)
    
vec1 = Vector(3,4)
vec2 = Vector(4,5)

def main():
    print(vec1 + vec2)

if __name__ == '__main__':
    main()  ## without doing this vector(7,9) was printed