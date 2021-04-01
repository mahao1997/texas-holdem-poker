from grpc_lib.texas_pb2 import Poker 
class Player():
    def __init__(self, player_name, counter, player_id):
        self.player_name = player_name
        self.player_id = player_id
        self.counter = counter
        self.buyin_time = 1
        self.active = False
        self.ready = False
        self.pool = 0
        self.hands=Deck()

    def GetStatus(self, hands):
        rsp = PlayerStatus()
        rsp.player_name = self.player_name
        rsp.player_id = self.player_id
        rsp.counter = self.counter
        rsp.buyin_time = self.buyin_time
        rsp.active = self.active
        rsp.ready = self.ready
        rsp.pool = self.pool
        for suit, value in self.hands.get_pokers():
            rsp.public.append(Poker(suit=suit, value=value))
        return rsp

    def BuyIn(self, buyin):
        self.buyin_time += 1
        self.counter += buyin

    def Speak(self, target, queue, btn):
        while True:
            #allin
            if self.counter == 0:
                return target
            try:
                user_name, action = self.queue.get(timeout = 20)
                if user_name != self.player_name:
                    continue
                if action['action'] == 'call':
                    money = target - self.pool
                    self.counter -= money
                    self.pool += money
                    return target
                if action['action'] == 'fold':
                    self.active = False
                    return target
                if action['action'] == 'raise':
                    money = action['raise_target'] - self.pool
                    self.counter -= money
                    self.pool += money
                    return self.pool
