import unittest
import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
from concurrent import futures
from texas_server import Texas
from client import Client
import time


class TestClient(unittest.TestCase):
    def setUp(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        texas_pb2_grpc.add_TexasServicer_to_server(Texas(), self.server)
        self.server.add_insecure_port("[::]:50051")
        self.server.start()

    def test_basic(self):
        num_players = 2
        client = [Client("p{}_{}".format(i, num_players)) for i in range(num_players)]
        for i in range(num_players):
            rsp = client[i].regist()
            self.assertEqual(rsp.code, 0)
            rsp = client[i].login()
            self.assertEqual(rsp.code, 0)
        room_id = client[0].create_room().room_id
        for i in range(num_players):
            rsp = client[i].getin_room(room_id)
            self.assertEqual(rsp.code, 0)
        for i in range(num_players):
            self.assertEqual(client[i].is_ready(), False)
            rsp = client[i].action({"action": "ready"})
            self.assertEqual(rsp.code, 0)
            while not client[i].is_ready():
                time.sleep(0.1)
            self.assertEqual(client[i].is_ready(), True)
            # client[i].get_myid()
        for stage in range(5):
            for i in range(num_players):
                rsp = client[i].action({"action": "call"})
                self.assertEqual(rsp.code, 0)
        for i in range(num_players):
            self.assertNotEqual(client[0].get_status().players[i].counter, 200)

    def tearDown(self):
        self.server.stop(0)
