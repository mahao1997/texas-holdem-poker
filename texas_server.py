from concurrent import futures
import time
import grpc
from grpc_lib import texas_pb2_grpc, texas_pb2
from grpc_lib.texas_pb2 import *
from engine import game_engine
import traceback
import json
class Texas(texas_pb2_grpc.TexasServicer):
    # 实现 proto 文件中定义的 rpc 调用
    #def SayHelloAgain(self, request, context):
    #    return helloworld_pb2.HelloReply(message='hello {msg}'.format(msg = request.name))
    def UserRegister(self, request, context):
        try:
            game_engine.add_user(request)
            return ActionResponse(code=0, info="add user success")
        except:
            return ActionResponse(code=-1, info="add user failed:\n{}".format(traceback.format_exc()))

    def UserLogin(self, request, context):
        try:
            res = game_engine.login_user(request)
            if res:
                return ActionResponse(code=0, info="login user success")
            else:
                return ActionResponse(code=-1, info="login user failed:\nWrong user or password")
        except:
            return ActionResponse(code=-1, info="login user failed:\n{}".format(traceback.format_exc()))

    def GetStatus(self, request, context):
        try:
            res = game_engine.login_user(request.user_info)
            if not res:
                return GetStatusResponse(code=-1, info="get status failed:\nWrong user or password")
            return GetStatusResponse(code=0, info="get status success", room_status=game_engine.rooms[request.room_id].GetStatus(request.user_info.user_name))
        except:
            return GetStatusResponse(code=-1, info="get status failed:\n{}".format(traceback.format_exc()))

    def Action(self, request, context):
        try:
            res = game_engine.login_user(request.user_info)
            if not res:
                return ActionResponse(code=-1, info="login user failed:\nWrong user or password")
            game_engine.rooms[request.room_id].PushAction(request.user_info.user_name, json.loads(request.extra))
            return ActionResponse(code=0, info="action recieved success.")
        except:
            return ActionResponse(code=-1, info="action recieved failed:\n{}".format(traceback.format_exc()))

    def CreateRoom(self, request, context):
        try:
            res = game_engine.login_user(request.user_info)
            if not res:
                return RoomResponse(code=-1, info="login user failed:\nWrong user or password")
            room_id = game_engine.create_room(request.room_name, request.blind, request.buyin)
            return game_engine.rooms[room_id].GetRoomInfo()
        except:
            return RoomResponse(code=-1, info="create room failed:\n{}".format(traceback.format_exc()))

    def GetinRoom(self, request, context):
        try:
            res = game_engine.login_user(request.user_info)
            if not res:
                return RoomResponse(code=-1, info="login user failed:\nWrong user or password")
            res = game_engine.rooms[request.room_id].AddPlayer(request.user_info.user_name)
            if not res:
                return RoomResponse(code=-1, info="login user failed")
            return game_engine.rooms[request.room_id].GetRoomInfo()
        except:
            return RoomResponse(code=-1, info="create room failed:\n{}".format(traceback.format_exc()))

def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    texas_pb2_grpc.add_TexasServicer_to_server(Texas(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
