# from enum import Enum
# value = [" A", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", " J", " Q", " K"]
# suit = ["♠", "♣", "♥", "♦"]
# Value = Enum("Value", ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"))
# Suit = Enum("Suit", ("♠", "♣", "♥", "♦"))

def fixed_length(s, length=10):
    if len(s) <= length:
        return s + " " * (length - len(s))
    return s[:length - 3] + "..."

class Card:
    def __init__(self, value="", suit=""):
        self.value = value
        self.suit = suit
        self.colored()

    def colored(self):
        if self.suit in ["♥", "♦"]:
            color = "\033[31m"  # red
        else:
            color = "\033[0m"   # default
        self.value = "{}{}\033[0m".format(color, fixed_length(self.value, 2))
        self.suit = "{}{}\033[0m".format(color, fixed_length(self.suit, 2))

class Player:
    def __init__(self, name="", chips=0):
        self.name = name
        self.chips = chips
        self.bet = 0
        self.stat = ""
        self.hand = []

    def set_name(self, name):
        self.name = name

    def set_chips(self, chips):
        self.chips = chips

    def set_hand(self, card1, card2):
        self.hand = [card1, card2]

class Render:
    def __init__(self):
        self.player = [Player() for i in range(9)]
        self.public = [Card() for i in range(5)]
    
    def draw(self):
        def card_box(pos, i):
            if i >= 0 and len(self.player[i].hand) == 2:
                if pos == 0:
                    print(" ┌──╥──┐       ", end="")
                elif pos == 1:
                    print(" │{}║{}│       ".format(self.player[i].hand[0].value, self.player[i].hand[1].value), end="")
                elif pos == 2:
                    print(" │{}║{}│${:<5} ".format(self.player[i].hand[0].suit, self.player[i].hand[1].suit, self.player[i].bet), end="")
                elif pos == 3:
                    print(" └──╨──┘       ", end="")
            else:
                print("               ", end="")

        def user_box(pos, i):
            # if i >= 0 and len(self.player[i].name) > 0:
            if i >= 0:
                if pos == 0:
                    print("┌─────────────┐", end="")
                elif pos == 1:
                    print("│{:<10}   │".format(fixed_length(self.player[i].name, 10)), end="")
                elif pos == 2:
                    print("│{:<4}  ${:>6}│".format(self.player[i].stat, self.player[i].chips, ), end="")
                elif pos == 3:
                    print("└─────────────┘", end="")
            else:
                print("               ", end="")

        for pos in [0, 1, 2, 3]:
            for i in [1, 2, 3, 4, 5]:
                user_box(pos, i)
            print()
        for pos in [0, 1, 2, 3]:
            for i in [1, 2, 3, 4, 5]:
                card_box(pos, i)
            print()
        print("╭─────────────────────────────────────────────────────────────────────────╮")
        print("│                            ┌──╥──╥──╥──╥──┐                             │")
        print("│                            │{}║{}║{}║{}║{}│                             │".format(self.public[0].value, self.public[1].value, self.public[2].value, self.public[3].value, self.public[4].value))
        print("│                            │{}║{}║{}║{}║{}│                             │".format(self.public[0].suit, self.public[1].suit, self.public[2].suit, self.public[3].suit, self.public[4].suit))
        print("│                            └──╨──╨──╨──╨──┘                             │")
        print("╰─────────────────────────────────────────────────────────────────────────╯")
        for pos in [0, 1, 2, 3]:
            for i in [0, -1, 8, 7, 6]:
                card_box(pos, i)
            print()
        for pos in [0, 1, 2, 3]:
            for i in [0, -1, 8, 7, 6]:
                user_box(pos, i)
            print()

if __name__ == "__main__":
    render = Render()
    render.player[0].set_name("ShaoShuai")
    render.player[1].set_name("hyuxusnia")
    render.player[2].set_name("nhaxyuuis")
    render.player[3].set_name("xsuhyinau")
    render.player[6].set_name("xuiyausnh")
    render.player[7].set_name("uxyunihas")
    render.player[8].set_name("auxsuhnyi")
    render.player[0].set_chips(1)
    render.player[1].set_chips(12)
    render.player[2].set_chips(123)
    render.player[3].set_chips(1234)
    render.player[6].set_chips(100)
    render.player[7].set_chips(1000)
    render.player[8].set_chips(10000)
    render.player[1].stat = "[BB]"
    render.player[2].stat = "[SB]"
    render.player[3].stat = "[D]"
    render.player[1].hand = [Card("A", "♠"), Card("10", "♦")]
    render.player[2].hand = [Card("", ""), Card("", "")]
    render.player[3].hand = [Card("", ""), Card("", "")]
    render.player[0].hand = [Card("K", "♠"), Card("K", "♦")]
    render.player[7].hand = [Card("", ""), Card("", "")]
    render.player[3].bet = 125
    render.public = [Card("A", "♠"), Card("9", "♥"), Card("10", "♦"), Card(), Card()]
    render.draw()