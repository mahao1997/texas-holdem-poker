import os
import unittest
from render import Render
from grpc_lib import texas_pb2


class TestRender(unittest.TestCase):
    def test_nothing(self):
        render = Render()
        render.draw()

    def test_basic(self):
        status = texas_pb2.RoomStatus()
        status.stage = 2

        status.players.append(texas_pb2.PlayerStatus())
        status.players[0].player_name = "syx"
        status.players[0].player_id = 1
        status.players[0].counter = 190
        status.players[0].buyin_time = 1
        status.players[0].active = True
        status.players[0].ready = True
        status.players[0].pool = 10
        status.players[0].hands.append(texas_pb2.Poker())
        status.players[0].hands.append(texas_pb2.Poker())
        status.players[0].hands[0].suit = 12
        status.players[0].hands[0].value = 1
        status.players[0].hands[1].suit = 10
        status.players[0].hands[1].value = 4

        status.players.append(texas_pb2.PlayerStatus())
        status.players[1].player_name = "Shuai Shao"
        status.players[1].player_id = 2
        status.players[1].counter = 195
        status.players[1].buyin_time = 1
        status.players[1].active = True
        status.players[1].ready = True
        status.players[1].pool = 5

        status.public.append(texas_pb2.Poker())
        status.public.append(texas_pb2.Poker())
        status.public.append(texas_pb2.Poker())
        status.public[0].suit = 0
        status.public[0].value = 2
        status.public[1].suit = 1
        status.public[1].value = 4
        status.public[2].suit = 2
        status.public[2].value = 8

        status.banker = 1
        status.speak = 2
        render = Render()
        render.parse(status)
        render.draw()

    def test_longname(self):
        status = texas_pb2.RoomStatus()
        status.players.append(texas_pb2.PlayerStatus())
        status.players[
            0
        ].player_name = "Pablo Diego José Francisco de Paula Juan Nepomuceno Crispín Crispiniano María Remedios de la Santísima Trinidad Ruiz Picasso"

        render = Render()
        render.parse(status)
        render.draw()
