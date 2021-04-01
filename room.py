from multiprocessing.dummy import Lock
import queue
from queue import Queue
from grpc_lib.texas_pb2 import RoomResponse, RoomStatus, PlayerStatus, Poker
import json
from poker import PokerEngine, Deck, CalWinners

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
        self.stage = 1 #未开局/翻牌/转牌/河牌/开牌
        self.players = []
        self.banker = 1
        self.speak = 0 #all speak
        self.queue = Queue()
        self.poker_engine = PokerEngine()
        self.public = Deck()
        self.players_cache = {}

    def AddPlayer(self, player_name):
        if player_name not in self.players_cache:
            player = Player(player_name, self.buyin, len(self.players) + 1)
            self.players_cache[player_name] = player
        else:
            player = self.players_cache[player_name]
        player.player_id = len(self.players) + 1
        player.active = False
        player.ready = False
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
            if player.user_id == user_id or self.stage == 1:
                rsp.players.append(player.GetStatus(hands=True))
            else:
                rsp.players.append(player.GetStatus(hands=False))
        for suit, value in self.public.get_pokers():
            rsp.public.append(Poker(suit=suit, value=value))
        rsp.banker = self.banker
        rsp.speak = self.speak
        return rsp

    def active_player(self):
        res = 0
        for player in self.players:
            if player.ready:
                res += 1
        return res

    def find_player(self, player_name):
        for player in self.players:
            if player.player_name == player_name:
                return player

    def run(self):
        target = 0
        btn = 0
        ptr = 0
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
                        player.ready = True
                    except queue.Empty:
                        for player in self.players:
                            if not player.ready:
                                self.DelPlayer(player.player_name)
                        continue
                for player in self.players:
                    if player.counter < self.blind * 2:
                        player.BuyIn(self.buyin)
                self.stage = 2
            elif self.stage == 2:
                self.PokerEngine.wash()
                #TODO:发牌和清除状态
                for player in self.players:
                    player.hands.clear()
                    player.hands.draw(self.PokerEngine)
                    player.hands.draw(self.PokerEngine)
                self.public.clear()
                sb_idx = next_id(self.banker)
                sb = self.players[sb_idx]
                sb.PutBlind(self.blind)
                bb_idx = next_id(sb_idx)
                bb = self.platyers[bb_idx]
                bb.PutBlind(self.blind * 2)
                ptr = next_id(bb_idx)
                btn = ptr
                target = self.blind * 2
                first_ptr_flag = True
                while ptr != btn or (ptr == btn and first_ptr_flag):
                    if ptr == btn and first_ptr_flag:
                        first_ptr_flag = False
                    if self.players[ptr].active:
                        new_target = self.players[ptr].Speak(target, self.queue)
                        if new_target != target:
                            target = new_target
                            btn = ptr
                    ptr = next_id(ptr)
                self.stage = 3
            elif self.stage == 3:
                for i in range(3):
                    self.public.draw(self.PokerEngine)
                ptr = next_id(self.banker)
                btn = ptr
                first_ptr_flag = True
                while ptr != btn or (ptr == btn and first_ptr_flag):
                    if ptr == btn and first_ptr_flag:
                        first_ptr_flag = False
                    if self.players[ptr].active:
                        new_target = self.players[ptr].Speak(target, self.queue)
                        if new_target != target:
                            target = new_target
                            btn = ptr
                    ptr = next_id(ptr)
                self.stage = 4
            elif self.stage == 4:
                ptr = next_id(self.banker)
                btn = ptr
                first_ptr_flag = True
                while ptr != btn or (ptr == btn and first_ptr_flag):
                    if ptr == btn and first_ptr_flag:
                        first_ptr_flag = False
                    if self.players[ptr].active:
                        new_target = self.players[ptr].Speak(target, self.queue)
                        if new_target != target:
                            target = new_target
                            btn = ptr
                    ptr = next_id(ptr)
                self.stage = 5
            elif self.stage == 5:
                #按牌型大小排序
                winners = CalWinners(self.players, self.public)
                for idx, win_player in enumerate(winners):
                    if win_player.active:#如果玩家没有fold
                        for lose_player_idx in range(idx, len(winners)):
                            lose_player = winners[lose_player_idx]
                            if win_player.pool >= lose_player.pool:
                                money = lose_player.pool
                            else:
                                money = win_player.pool
                            win_player.counter += money
                            lose_player.pool -= money
                self.stage = 1
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
