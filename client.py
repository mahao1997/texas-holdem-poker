import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
import time
import json
user_info = None
def regist(input_user_info):
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.UserRegister(input_user_info)
    print(response)
    return response

def login(input_user_info):
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.UserLogin(input_user_info)
    print(response)
    return response


def create_room():
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    req = texas_pb2.CreateRoomRequest(room_name='my_test_room', blind=5, buyin=200, user_info=user_info)
    response = stub.CreateRoom(req)
    print(response)
    return response

def getin_room(room_id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    req = texas_pb2.GetinRoomRequest(room_id=room_id, user_info=user_info)
    response = stub.GetinRoom(req)
    print(response)
    return response

def get_status(room_id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.GetStatus(texas_pb2.GetStatusRequest(user_info=user_info, room_id=room_id))
    return response
def send_action(extra, room_id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.Action(texas_pb2.ActionRequest(user_info=user_info, room_id=room_id, extra=json.dumps(extra)))
    print(response)
    return response
   
def get_myid(status):
    for player in status.room_status.players:
        print('player name = {}, user name = {}, equal = {}'.format(player.player_name, user_info.user_name, player.player_name == user_info.user_name))
        if player.player_name == user_info.user_name:
            return player.player_id
if __name__ == '__main__':
    begin_get = False
    room_id = None
    while True: 
        st = input("input your action\nr : regist\nl : login\nc : create room\ng : get in room\n")
        if st == 'r':
            user_name = input("input your user name\n").strip()
            pass_wd = input("input your password\n").strip()
            regist_user_info = texas_pb2.UserInfo(user_name=user_name, passwd=pass_wd)
            rsp = regist(regist_user_info)
            if rsp.code == 0:
                user_info = regist_user_info
        if st == 'l':
            user_name = input("input your user name\n").strip()
            pass_wd = input("input your password\n").strip()
            login_user_info = texas_pb2.UserInfo(user_name=user_name, passwd=pass_wd)
            rsp = login(login_user_info)
            if rsp.code == 0:
                user_info = login_user_info
        if st == 'c':
            create_room()
        if st == 'g':
            room_id = int(input("input room id\n").strip())
            rsp = getin_room(room_id)
            if (rsp.code == 0):
                break
    pre_status = None
    while True:
        status = get_status(room_id)
        time.sleep(0.5)
        if status == pre_status:
            continue
        else:
            print(status)
            pre_status = status
            myid = get_myid(status)
            print('myid = {}'.format(myid))
            if status.room_status.speak == 0 and status.room_status.players[myid - 1].ready:
                continue
            if status.room_status.speak == 0:
                st = input("input your action\nready\nquit\n")
                if st == 'ready':
                    send_action({'action': 'ready'}, room_id) 
                if st == 'quit':
                    send_action({'action': 'quit'}, room_id)
            if myid == status.room_status.speak:
                st = input("input your action\ncall\ncheck\nfold\nraise\n")
                if st == 'call' or st == 'check':
                    send_action({'action': 'call'}, room_id)
                if st == 'fold': 
                    send_action({'action': 'fold'}, room_id)
                if st == 'raise':
                    target = int(input("input your target"))
                    send_action({'action': 'call', 'raise_target': target}, room_id)
