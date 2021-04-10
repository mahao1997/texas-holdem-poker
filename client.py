import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
import time
import json
from render import Render


class Client:
    def __init__(self, username=None):
        channel = grpc.insecure_channel("localhost:50051")
        self.stub = texas_pb2_grpc.TexasStub(channel)
        if username is not None:
            self.set_username(username)
        self.myid = None

    def set_username(self, username):
        self.username = username
        self.password = "password"  # TODO
        self.user_info = texas_pb2.UserInfo(
            user_name=self.username, passwd=self.password
        )

    def regist(self):
        response = self.stub.UserRegister(self.user_info)
        return response

    def login(self):
        response = self.stub.UserLogin(self.user_info)
        return response

    def create_room(self, room_name=None, blind=5, buyin=200):
        if room_name is None:
            room_name = "{}'s room".format(self.username)
        req = texas_pb2.CreateRoomRequest(
            room_name=room_name, blind=blind, buyin=buyin, user_info=self.user_info
        )
        response = self.stub.CreateRoom(req)
        self.room_id = response.room_id
        return response

    def getin_room(self, room_id=None):
        if room_id is not None:
            self.room_id = room_id
        req = texas_pb2.GetinRoomRequest(room_id=self.room_id, user_info=self.user_info)
        response = self.stub.GetinRoom(req)
        return response

    def get_status(self):
        response = self.stub.GetStatus(
            texas_pb2.GetStatusRequest(user_info=self.user_info, room_id=self.room_id)
        )
        return response.room_status

    def action(self, extra):
        response = self.stub.Action(
            texas_pb2.ActionRequest(
                user_info=self.user_info, room_id=self.room_id, extra=json.dumps(extra)
            )
        )
        return response

    def get_myid(self):
        if self.myid is not None:
            return self.myid
        status = self.get_status()
        for player in status.players:
            if player.player_name == self.username:
                self.myid = player.player_id
        return self.myid

    def is_ready(self):
        status = self.get_status()
        for player in status.players:
            if player.player_name == self.username:
                return player.ready
        return False


if __name__ == "__main__":
    client = Client()
    render = Render()

    while True:
        st = input("input your action\nl : login\nc : create room\ng : get in room\n")
        if st == "l":
            user_name = input("input your user name\n").strip()
            client.set_username(user_name)
            client.regist()
            client.login()
        if st == "c":
            client.create_room()
            client.getin_room()
            break
        if st == "g":
            room_id = int(input("input room id\n").strip())
            client.getin_room(room_id)
            break

    pre_status = None
    pre_time = time.time()
    render.set_myid(client.get_myid())
    render.set_room_id(client.room_id)
    while True:
        status = client.get_status()
        time.sleep(0.5)
        if status == pre_status:
            continue
        else:
            myid = client.get_myid()
            render.parse(status)
            render.draw()

            pre_status = status
            pre_time = time.time()

            if status.speak == 0 and status.players[myid - 1].ready:
                continue
            if status.speak == 0:
                st = input("input your action:[ready][quit]\n")
                if st == "ready":
                    client.action({"action": "ready"})
                if st == "quit":
                    client.action({"action": "quit"})
            if myid == status.speak:
                st = input("input your action:[call][check][fold][raise]\n")
                if st == "call" or st == "check":
                    client.action({"action": "call"})
                if st == "fold":
                    client.action({"action": "fold"})
                if st == "raise":
                    target = int(input("input your target"))
                    client.action({"action": "call", "raise_target": target})
