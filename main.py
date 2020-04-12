from chapter01.data_model import Card, FrenchDeck

from random import choice

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    deck = FrenchDeck()
    # print(len(deck))
    # random_deck = choice(deck)
    # print('random choose card:', random_deck.rank, random_deck.suit)
    #
    # print('reverse iterator：')
    for card in sorted(deck, key=spades_high):
        print(card)

