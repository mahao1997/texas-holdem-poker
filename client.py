import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
def regist():
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.UserRegister(texas_pb2.UserInfo(user_name='test', passwd='test'))
    print(response)

def login():
    channel = grpc.insecure_channel('localhost:50051')
    stub = texas_pb2_grpc.TexasStub(channel)
    response = stub.UserLogin(texas_pb2.UserInfo(user_name='test', passwd='test'))
    print(response)

if __name__ == '__main__':
    regist()
    login()
