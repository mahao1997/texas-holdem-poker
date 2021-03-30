from room import Room
from multiprocessing.dummy import Pool as ThreadPool
import random

MAX_ROOM_NUM = 5
class Engine():
    def __init__(self, ):
        self.users = []
        self.rooms = {}
        self.pool = ThreadPool(MAX_ROOM_NUM)

    def add_user(self, user):
        self.users.append(user)

    def login_user(self, user):
        for it in self.users:
            if user == it:
                return True
        return False

    def create_room(self, room_name, blind, buyin):
        new_room = Room(room_name, blind, buyin, self.generate_roomid())
        self.pool.apply_async(new_room.run)
        self.rooms[new_room.room_id] = new_room
        return new_room.room_id
    def generate_roomid(self):
        new_id = random.randint(100000, 999999)
        while new_id in self.rooms:
            new_id = random.randint(100000, 999999)
        return new_id

game_engine = Engine()
