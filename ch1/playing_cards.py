import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(r, s) for s in self.suits for r in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    from random import choice
    random_card = Card('7', 'diamonds')
    print(random_card)

    deck = FrenchDeck()
    print(len(deck))

    print(choice(deck))
    print(choice(deck))

    print(deck[:3])

    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)
    