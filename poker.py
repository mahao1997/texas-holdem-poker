import random
from deuces import Deck
class Deck:
    def __init__(self):
        self.pokers = []
    def get_pokers(self):
        res = []
        for poker in self.pokers:
            res.append((Card.get_rank_int(a), Card.get_suit_int(card_int)))
        return res
    def draw(self, engine):
        self.pokers.append(engine.draw())

class PokerEngine:
    def __init__(self):
        self.wash()
    def wash(self):
        self.deck = Deck()
        self.deck.shuffle()
    def draw(self):
        return self.deck.draw(1)

def CalWinners(players, public_deck):
    res = []
    for player in players:
        if not player.active:
            res.append((player, 10000))
        else:
            res.append((player, evaluator.evaluate(player.hands.pokers, public_deck.pokers)))
    res.sort(key=lambda x:x[1])
    return [x for x,y in res]
