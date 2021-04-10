from grpc_lib import texas_pb2

PRETTY_VALUE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
PRETTY_SUITS = {
    1: "♠",  # spades
    2: "♥",  # hearts
    4: "♦",  # diamonds
    8: "♣",  # clubs
}


def fixed_length(s, length=10):
    if len(s) <= length:
        return s + " " * (length - len(s))
    return s[: length - 3] + "..."


class Card:
    def __init__(self, card: texas_pb2.Poker = None):
        self.value = "  "
        self.suit = "  "
        if card is not None:
            self.parse(card)

    def parse(self, card: texas_pb2.Poker):
        self.value = PRETTY_VALUE[card.suit]
        self.suit = PRETTY_SUITS[card.value]
        self.colored()

    def colored(self):
        if self.suit in ["♥", "♦"]:
            color = "\033[31m"  # red
        else:
            color = "\033[0m"  # default
        self.value = "{}{}\033[0m".format(color, fixed_length(self.value, 2))
        self.suit = "{}{}\033[0m".format(color, fixed_length(self.suit, 2))


class Player:
    def __init__(self, player_status: texas_pb2.PlayerStatus = None):
        self.player_name = ""
        self.player_id = -1
        self.counter = 0
        self.buyin_time = 0
        self.active = False
        self.ready = False
        self.pool = 0
        self.hands = []
        if player_status is not None:
            self.parse(player_status)

    def parse(self, player_status: texas_pb2.PlayerStatus):
        self.player_name = player_status.player_name
        self.player_id = player_status.player_id
        self.counter = player_status.counter
        self.buyin_time = player_status.buyin_time
        self.active = player_status.active
        self.ready = player_status.ready
        self.pool = player_status.pool
        if player_status.active:
            self.hands = [Card(), Card()]
        if len(player_status.hands) == 2:
            self.hands[0].parse(player_status.hands[0])
            self.hands[1].parse(player_status.hands[1])


class Render:
    def __init__(self):
        self.player = [Player() for i in range(9)]
        self.public = [Card() for i in range(5)]
        self.myid = 0

    def parse(self, status: texas_pb2.RoomStatus, myid):
        self.__init__()
        self.myid = myid
        for player in status.players:
            self.player[player.player_id - self.myid].parse(player)
        for i in range(len(status.public)):
            self.public[i].parse(status.public[i])

    def draw(self):
        def card_box(pos, i):
            if i >= 0 and len(self.player[i].hands) == 2:
                if pos == 0:
                    print(" ┌──╥──┐       ", end="")
                elif pos == 1:
                    print(
                        " │{}║{}│       ".format(
                            self.player[i].hands[0].value, self.player[i].hands[1].value
                        ),
                        end="",
                    )
                elif pos == 2:
                    print(
                        " │{}║{}│${:<5} ".format(
                            self.player[i].hands[0].suit,
                            self.player[i].hands[1].suit,
                            self.player[i].pool,
                        ),
                        end="",
                    )
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
                    print(
                        "│{:<10}   │".format(
                            fixed_length(self.player[i].player_name, 10)
                        ),
                        end="",
                    )
                elif pos == 2:
                    print(
                        "│{:<4}  ${:>6}│".format(
                            "",
                            self.player[i].counter,
                        ),
                        end="",
                    )
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
        print(
            "╭─────────────────────────────────────────────────────────────────────────╮"
        )
        print(
            "│                            ┌──╥──╥──╥──╥──┐                             │"
        )
        print(
            "│                            │{}║{}║{}║{}║{}│                             │".format(
                self.public[0].value,
                self.public[1].value,
                self.public[2].value,
                self.public[3].value,
                self.public[4].value,
            )
        )
        print(
            "│                            │{}║{}║{}║{}║{}│                             │".format(
                self.public[0].suit,
                self.public[1].suit,
                self.public[2].suit,
                self.public[3].suit,
                self.public[4].suit,
            )
        )
        print(
            "│                            └──╨──╨──╨──╨──┘                             │"
        )
        print(
            "╰─────────────────────────────────────────────────────────────────────────╯"
        )
        for pos in [0, 1, 2, 3]:
            for i in [0, -1, 8, 7, 6]:
                card_box(pos, i)
            print()
        for pos in [0, 1, 2, 3]:
            for i in [0, -1, 8, 7, 6]:
                user_box(pos, i)
            print()
