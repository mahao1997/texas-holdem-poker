import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
user_info = texas_pb2.UserInfo(user_name='test', passwd='test')
def regist():
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.UserRegister(user_info)
    print(response)

def login():
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.UserLogin(user_info)
    print(response)

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

def get_status(room_id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.GetStatus(texas_pb2.GetStatusRequest(user_info=user_info, room_id=room_id))
    print(response)

if __name__ == '__main__':
    regist()
    login()
    res = create_room()
    room_id = res.room_id
    getin_room(room_id)
    get_status(room_id)
