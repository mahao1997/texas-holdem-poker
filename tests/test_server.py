import os
import unittest
import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
from concurrent import futures
from texas_server import Texas
from client import regist, login
import time

class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        texas_pb2_grpc.add_TexasServicer_to_server(Texas(), self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()

    def test_regist_and_login(self):
        # regist
        regist_user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = regist(regist_user_info)
        self.assertEqual(rsp.code, 0)

        # regist same name
        regist_user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = regist(regist_user_info)
        self.assertEqual(rsp.code, -1)

        # regist empty name
        regist_user_info = texas_pb2.UserInfo(user_name="", passwd="password")
        rsp = regist(regist_user_info)
        self.assertEqual(rsp.code, -1)

        # regist empty password
        regist_user_info = texas_pb2.UserInfo(user_name="username", passwd="")
        rsp = regist(regist_user_info)
        self.assertEqual(rsp.code, -1)

        # login
        login_user_info = texas_pb2.UserInfo(user_name="username", passwd="password")
        rsp = login(login_user_info)
        self.assertEqual(rsp.code, 0)

        # wrong username
        login_user_info = texas_pb2.UserInfo(user_name="no one", passwd="password")
        rsp = login(login_user_info)
        self.assertEqual(rsp.code, -1)

        # wrong password
        login_user_info = texas_pb2.UserInfo(user_name="username", passwd="")
        rsp = login(login_user_info)
        self.assertEqual(rsp.code, -1)


    def tearDown(self):
        self.server.stop(0)