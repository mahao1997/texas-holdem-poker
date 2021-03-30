from multiprocessing.dummy import Lock
import queue
from queue import Queue
from grpc_lib.texas_pb2 import RoomResponse, RoomStatus, PlayerStatus, Poker
import json
from poker import PokerCard, PokerEngine, PublicDeck, HandDeck

class Room():
    def __init__(self, room_name, blind, buyin, room_id):
        self.room_name = room_name
        if isinstance(blind, int) and blind < 100:
            self.blind = blind
        else:
            raise Exception('blind must be int and small than 100')          
        if isinstance(buyin, int):
            self.buyin = buyin
        else:
            raise Exception('buyin must be int')          
        self.lock = Lock()
        self.room_id = room_id
        self.stage = 1 #未开局/翻牌/转牌/河牌
        self.players = []
        self.banker = 1
        self.speak = 0 #all speak
        self.queue = Queue()
        self.poker_engine = PokerEngine()
        self.public = PublicDeck()
        self.hands = []
        self.players_cache = {}

    def AddPlayer(self, player_name):
        if player_name not in self.players_cache:
            player = Player(player_name, self.buyin, len(self.players) + 1)
            self.players_cache[player_name] = player
        else:
            player = self.players_cache[player_name]
        player.player_id = len(self.players) + 1
        player.active = False
        self.players.append(player)

    def DelPlayer(self, player_name):
        idx = -1
        for player_idx, player in enumerate(self.players):
            if players.player_name == player_name:
                idx = player_idx
        if idx == -1:
            raise Exception('can not find player {}'.format(player_name))

        self.players_cache[player_name] = self.players[idx]
        del self.players[idx]
        for player_idx, player in enumerate(self.players):
            player.player_id = player_idx

    def GetRoomInfo(self):
        rsp = RoomResponse()
        rsp.code = 0
        rsp.room_name = self.room_name
        rsp.room_id = self.room_id
        rsp.blind = self.blind
        rsp.buyin = self.buyin
        return rsp

    def PushAction(self, user_name, action):
        self.queue.push((user_name, json.loads(action)))
        
    def GetStatus(self, user_id)    
        rsp = RoomStatus()
        rsp.stage = self.stage
        for player in self.players:
            rsp.players.append(player.GetStatus())
        for suit, value in self.public.get_pokers():
            rsp.public.append(Poker(suit=suit, value=value))
        for idx, player in enumerate(self.players):
            if player.user_id == user_id:
                for suit, value in self.hands[idx].get_pokers():
                    rsp.hand.append(Poker(suit=suit, value=value))
                break
        rsp.banker = self.banker
        rsp.speak = self.speak
        return rsp

    def active_player(self):
        res = 0
        for player in self.players:
            if player.active:
                res += 1
        return res

    def find_player(self, player_name):
        for player in self.players:
            if player.player_name == player_name:
                return player

    def run(self):
        while True:
            if self.stage == 1:
                while not (len(self.players) >= 2 and self.active_player() == len(self.players)):
                    try:
                        user_name, action = self.queue.get(timeout = 20)
                        if action['action'] == 'quit':
                            self.DelPlayer(user_name)
                            continue
                        elif action['action'] != 'ready':
                            continue
                        player = self.find_player(user_name) 
                        player.active = True
                    except queue.Empty:
                        for player in self.players:
                            if not player.active:
                                self.DelPlayer(player.player_name)
                        continue
                for player in self.players:
                    if player.counter < self.blind * 2:
                        player.BuyIn(self.buyin)
                self.stage = 2
            elif self.stage == 2:
                sb = next_id(self.banker)
                sb.
                btn = 

                while  
    def next_id(self, idx, times=1):
        for i in range(times):
            idx = idx + 1
            if idx > len(self.players):
                idx = 1
        return idx
    
    def pre_id(self, idx, times=1):
        for i in range(times):
            idx = idx - 1
            if idx < 1:
                idx = len(self.players)
        return idx
class Player():
    def __init__(self, player_name, counter, player_id):
        self.player_name = player_name
        self.player_id = player_id
        self.counter = counter
        self.buyin_time = 1
        self.active = False
    def GetStatus(self):
        rsp = PlayerStatus()
        rsp.player_name = self.player_name
        rsp.player_id = self.player_id
        rsp.counter = self.counter
        rsp.buyin_time = self.buyin_time
        rsp.active = self.active
        return rsp  
    def BuyIn(self, buyin):
        self.buyin_time += 1
        self.counter += buyin
