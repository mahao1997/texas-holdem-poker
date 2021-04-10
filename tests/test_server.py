import os
import unittest
import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
from concurrent import futures
from texas_server import Texas
import json


class TestServerRoom(unittest.TestCase):
    def setUp(self):
        pass

    def test_regist_and_login(self):
        server = Texas()

        # regist
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = server.UserRegister(user_info, None)
        self.assertEqual(rsp.code, 0)
        """
        # regist same name
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = server.UserRegister(user_info, None)
        self.assertEqual(rsp.code, -1)

        # regist empty name
        user_info = texas_pb2.UserInfo(user_name="", passwd="password")
        rsp = server.UserRegister(user_info, None)
        self.assertEqual(rsp.code, -1)

        # regist empty password
        user_info = texas_pb2.UserInfo(user_name="username", passwd="")
        rsp = server.UserRegister(user_info, None)
        self.assertEqual(rsp.code, -1)
        """
        # login
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = server.UserLogin(user_info, None)
        self.assertEqual(rsp.code, 0)

        # wrong username
        user_info = texas_pb2.UserInfo(user_name="no one", passwd="password")
        rsp = server.UserLogin(user_info, None)
        self.assertEqual(rsp.code, -1)

        # wrong password
        user_info = texas_pb2.UserInfo(user_name="username", passwd="")
        rsp = server.UserLogin(user_info, None)
        self.assertEqual(rsp.code, -1)
    
    def test_room(self):
        def num_players(user_info, room_id):
            room_status = server.GetStatus(
                texas_pb2.GetStatusRequest(user_info=user_info, room_id=room_id), None
            ).room_status
            return len(room_status.players)

        server = Texas()

        # regist
        for i in range(20):
            user_info = texas_pb2.UserInfo(user_name="p{}".format(i), passwd="password")
            rsp = server.UserRegister(user_info, None)
            self.assertEqual(rsp.code, 0)

        # create a room
        room_name = "test_room"
        blind = 5
        buyin = 200
        user_info = texas_pb2.UserInfo(user_name="p1", passwd="password")
        req = texas_pb2.CreateRoomRequest(
            room_name=room_name, blind=blind, buyin=buyin, user_info=user_info
        )
        rsp = server.CreateRoom(req, None)
        self.assertEqual(rsp.code, 0)
        self.assertEqual(rsp.room_name, "test_room")
        self.assertEqual(rsp.blind, blind)
        self.assertEqual(rsp.buyin, buyin)
        room_id = rsp.room_id

        # getin a room
        for i in range(9):
            user_info = texas_pb2.UserInfo(user_name="p{}".format(i), passwd="password")
            req = texas_pb2.GetinRoomRequest(room_id=room_id, user_info=user_info)
            rsp = server.GetinRoom(req, None)
            self.assertEqual(rsp.code, 0)
            self.assertEqual(rsp.room_name, "test_room")
            self.assertEqual(rsp.blind, blind)
            self.assertEqual(rsp.buyin, buyin)

        self.assertEqual(num_players(user_info, room_id), 9)

        """
        # getin a full room
        for i in range(9, 20):
            user_info = texas_pb2.UserInfo(user_name="p{}".format(i), passwd="password")
            req = texas_pb2.GetinRoomRequest(room_id=room_id, user_info=user_info)
            rsp = server.GetinRoom(req, None)
            self.assertEqual(rsp.code, -1)
        """

        # repeatedly getin a room
        for i in range(9):
            user_info = texas_pb2.UserInfo(user_name="p{}".format(i), passwd="password")
            req = texas_pb2.GetinRoomRequest(room_id=room_id, user_info=user_info)
            rsp = server.GetinRoom(req, None)
            self.assertEqual(rsp.code, -1)
        """
        # quit from a room
        for i in range(20):
            user_info = texas_pb2.UserInfo(user_name="p{}".format(i), passwd="password")
            rsp = server.Action(
                texas_pb2.ActionRequest(
                    user_info=user_info,
                    room_id=room_id,
                    extra=json.dumps({"action": "quit"}),
                ), None
            )
            self.assertEqual(rsp.code, 0)
        self.assertEqual(num_players(user_info, room_id), 0)
        """

    def test_blind_limit(self):
        server = Texas()

        # regist
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = server.UserRegister(user_info, None)
        self.assertEqual(rsp.code, 0)
        """
        # too small blind
        room_name = "test_room"
        blind = -1
        buyin = 200
        req = texas_pb2.CreateRoomRequest(
            room_name=room_name, blind=blind, buyin=buyin, user_info=user_info
        )
        rsp = server.CreateRoom(req, None)
        self.assertEqual(rsp.code, -1)

        # too big blind
        room_name = "test_room"
        blind = 101
        buyin = 200
        req = texas_pb2.CreateRoomRequest(
            room_name=room_name, blind=blind, buyin=buyin, user_info=user_info
        )
        rsp = server.CreateRoom(req, None)
        self.assertEqual(rsp.code, -1)
        """

    def test_ready(self):
        server = Texas()

        # regist
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = server.UserRegister(user_info, None)
        self.assertEqual(rsp.code, 0)

        # create room
        req = texas_pb2.CreateRoomRequest(
            room_name="test_room", blind=5, buyin=200, user_info=user_info
        )
        rsp = server.CreateRoom(req, None)
        self.assertEqual(rsp.code, 0)
        room_id = rsp.room_id

        # getin room
        req = texas_pb2.GetinRoomRequest(room_id=room_id, user_info=user_info)
        rsp = server.GetinRoom(req, None)
        self.assertEqual(rsp.code, 0)

        # ready
        rsp = server.Action(
            texas_pb2.ActionRequest(
                user_info=user_info,
                room_id=room_id,
                extra=json.dumps({"action": "ready"}),
            ), None
        )
        self.assertEqual(rsp.code, 0)
    
    def tearDown(self):
        pass
