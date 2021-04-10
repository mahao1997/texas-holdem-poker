import os
import unittest
import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
from concurrent import futures
from texas_server import Texas


class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        texas_pb2_grpc.add_TexasServicer_to_server(Texas(), self.server)
        self.server.add_insecure_port("[::]:50051")
        self.server.start()

    def test_regist_and_login(self):
        channel = grpc.insecure_channel("localhost:50051")
        stub = texas_pb2_grpc.TexasStub(channel)

        # regist
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = stub.UserRegister(user_info)
        self.assertEqual(rsp.code, 0)

        # regist same name
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = stub.UserRegister(user_info)
        self.assertEqual(rsp.code, -1)

        # regist empty name
        user_info = texas_pb2.UserInfo(user_name="", passwd="password")
        rsp = stub.UserRegister(user_info)
        self.assertEqual(rsp.code, -1)

        # regist empty password
        user_info = texas_pb2.UserInfo(user_name="username", passwd="")
        rsp = stub.UserRegister(user_info)
        self.assertEqual(rsp.code, -1)

        # login
        user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = stub.UserLogin(user_info)
        self.assertEqual(rsp.code, 0)

        # wrong username
        user_info = texas_pb2.UserInfo(user_name="no one", passwd="password")
        rsp = stub.UserLogin(user_info)
        self.assertEqual(rsp.code, -1)

        # wrong password
        user_info = texas_pb2.UserInfo(user_name="username", passwd="")
        rsp = stub.UserLogin(user_info)
        self.assertEqual(rsp.code, -1)

    def tearDown(self):
        self.server.stop(0)
