# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: texas.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='texas.proto',
  package='texas',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0btexas.proto\x12\x05texas\"W\n\x11GetStatusResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04info\x18\x02 \x01(\t\x12&\n\x0broom_status\x18\x03 \x01(\x0b\x32\x11.texas.RoomStatus\"\x9b\x01\n\nRoomStatus\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x07players\x18\x02 \x03(\x0b\x32\x13.texas.PlayerStatus\x12\x1c\n\x06public\x18\x03 \x03(\x0b\x32\x0c.texas.Poker\x12\x1a\n\x04hand\x18\x04 \x03(\x0b\x32\x0c.texas.Poker\x12\x0e\n\x06\x62\x61nker\x18\x05 \x01(\x05\x12\r\n\x05speak\x18\x06 \x01(\x08\"}\n\x0cPlayerStatus\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\x12\x11\n\tplayer_id\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ounter\x18\x03 \x01(\x05\x12\x12\n\nbuyin_time\x18\x04 \x01(\x05\x12\x10\n\x08seat_num\x18\x05 \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x06 \x01(\x08\"$\n\x05Poker\x12\x0c\n\x04suit\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\"G\n\x10GetStatusRequest\x12\"\n\tuser_info\x18\x01 \x01(\x0b\x32\x0f.texas.UserInfo\x12\x0f\n\x07room_id\x18\x02 \x01(\x05\"-\n\x08UserInfo\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0e\n\x06passwd\x18\x02 \x01(\t\"S\n\rActionRequest\x12\"\n\tuser_info\x18\x01 \x01(\x0b\x32\x0f.texas.UserInfo\x12\x0f\n\x07room_id\x18\x02 \x01(\x05\x12\r\n\x05\x65xtra\x18\x03 \x01(\t\",\n\x0e\x41\x63tionResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04info\x18\x02 \x01(\t\"h\n\x11\x43reateRoomRequest\x12\x11\n\troom_name\x18\x01 \x01(\t\x12\r\n\x05\x62lind\x18\x02 \x01(\x05\x12\r\n\x05\x62uyin\x18\x03 \x01(\x05\x12\"\n\tuser_info\x18\x04 \x01(\x0b\x32\x0f.texas.UserInfo\"G\n\x10GetinRoomRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\x05\x12\"\n\tuser_info\x18\x02 \x01(\x0b\x32\x0f.texas.UserInfo\"l\n\x0cRoomResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x11\n\troom_name\x18\x03 \x01(\t\x12\x0f\n\x07room_id\x18\x04 \x01(\x05\x12\r\n\x05\x62lind\x18\x05 \x01(\x05\x12\r\n\x05\x62uyin\x18\x06 \x01(\x05\x32\xef\x02\n\x05Texas\x12\x35\n\tUserLogin\x12\x0f.texas.UserInfo\x1a\x15.texas.ActionResponse\"\x00\x12\x38\n\x0cUserRegister\x12\x0f.texas.UserInfo\x1a\x15.texas.ActionResponse\"\x00\x12@\n\tGetStatus\x12\x17.texas.GetStatusRequest\x1a\x18.texas.GetStatusResponse\"\x00\x12\x37\n\x06\x41\x63tion\x12\x14.texas.ActionRequest\x1a\x15.texas.ActionResponse\"\x00\x12=\n\nCreateRoom\x12\x18.texas.CreateRoomRequest\x1a\x13.texas.RoomResponse\"\x00\x12;\n\tGetinRoom\x12\x17.texas.GetinRoomRequest\x1a\x13.texas.RoomResponse\"\x00\x62\x06proto3'
)




_GETSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetStatusResponse',
  full_name='texas.GetStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='texas.GetStatusResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='texas.GetStatusResponse.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_status', full_name='texas.GetStatusResponse.room_status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=109,
)


_ROOMSTATUS = _descriptor.Descriptor(
  name='RoomStatus',
  full_name='texas.RoomStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='texas.RoomStatus.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='players', full_name='texas.RoomStatus.players', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public', full_name='texas.RoomStatus.public', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hand', full_name='texas.RoomStatus.hand', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='banker', full_name='texas.RoomStatus.banker', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speak', full_name='texas.RoomStatus.speak', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=267,
)


_PLAYERSTATUS = _descriptor.Descriptor(
  name='PlayerStatus',
  full_name='texas.PlayerStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_name', full_name='texas.PlayerStatus.player_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='texas.PlayerStatus.player_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counter', full_name='texas.PlayerStatus.counter', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buyin_time', full_name='texas.PlayerStatus.buyin_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seat_num', full_name='texas.PlayerStatus.seat_num', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='texas.PlayerStatus.active', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=394,
)


_POKER = _descriptor.Descriptor(
  name='Poker',
  full_name='texas.Poker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='suit', full_name='texas.Poker.suit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='texas.Poker.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=432,
)


_GETSTATUSREQUEST = _descriptor.Descriptor(
  name='GetStatusRequest',
  full_name='texas.GetStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='texas.GetStatusRequest.user_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='texas.GetStatusRequest.room_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=505,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='texas.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='texas.UserInfo.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='texas.UserInfo.passwd', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=552,
)


_ACTIONREQUEST = _descriptor.Descriptor(
  name='ActionRequest',
  full_name='texas.ActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='texas.ActionRequest.user_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='texas.ActionRequest.room_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra', full_name='texas.ActionRequest.extra', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=637,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='texas.ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='texas.ActionResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='texas.ActionResponse.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=639,
  serialized_end=683,
)


_CREATEROOMREQUEST = _descriptor.Descriptor(
  name='CreateRoomRequest',
  full_name='texas.CreateRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_name', full_name='texas.CreateRoomRequest.room_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blind', full_name='texas.CreateRoomRequest.blind', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buyin', full_name='texas.CreateRoomRequest.buyin', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_info', full_name='texas.CreateRoomRequest.user_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=685,
  serialized_end=789,
)


_GETINROOMREQUEST = _descriptor.Descriptor(
  name='GetinRoomRequest',
  full_name='texas.GetinRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_id', full_name='texas.GetinRoomRequest.room_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_info', full_name='texas.GetinRoomRequest.user_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=791,
  serialized_end=862,
)


_ROOMRESPONSE = _descriptor.Descriptor(
  name='RoomResponse',
  full_name='texas.RoomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='texas.RoomResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='texas.RoomResponse.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_name', full_name='texas.RoomResponse.room_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='texas.RoomResponse.room_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blind', full_name='texas.RoomResponse.blind', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buyin', full_name='texas.RoomResponse.buyin', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=972,
)

_GETSTATUSRESPONSE.fields_by_name['room_status'].message_type = _ROOMSTATUS
_ROOMSTATUS.fields_by_name['players'].message_type = _PLAYERSTATUS
_ROOMSTATUS.fields_by_name['public'].message_type = _POKER
_ROOMSTATUS.fields_by_name['hand'].message_type = _POKER
_GETSTATUSREQUEST.fields_by_name['user_info'].message_type = _USERINFO
_ACTIONREQUEST.fields_by_name['user_info'].message_type = _USERINFO
_CREATEROOMREQUEST.fields_by_name['user_info'].message_type = _USERINFO
_GETINROOMREQUEST.fields_by_name['user_info'].message_type = _USERINFO
DESCRIPTOR.message_types_by_name['GetStatusResponse'] = _GETSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['RoomStatus'] = _ROOMSTATUS
DESCRIPTOR.message_types_by_name['PlayerStatus'] = _PLAYERSTATUS
DESCRIPTOR.message_types_by_name['Poker'] = _POKER
DESCRIPTOR.message_types_by_name['GetStatusRequest'] = _GETSTATUSREQUEST
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['ActionRequest'] = _ACTIONREQUEST
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateRoomRequest'] = _CREATEROOMREQUEST
DESCRIPTOR.message_types_by_name['GetinRoomRequest'] = _GETINROOMREQUEST
DESCRIPTOR.message_types_by_name['RoomResponse'] = _ROOMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStatusResponse = _reflection.GeneratedProtocolMessageType('GetStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSRESPONSE,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.GetStatusResponse)
  })
_sym_db.RegisterMessage(GetStatusResponse)

RoomStatus = _reflection.GeneratedProtocolMessageType('RoomStatus', (_message.Message,), {
  'DESCRIPTOR' : _ROOMSTATUS,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.RoomStatus)
  })
_sym_db.RegisterMessage(RoomStatus)

PlayerStatus = _reflection.GeneratedProtocolMessageType('PlayerStatus', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSTATUS,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.PlayerStatus)
  })
_sym_db.RegisterMessage(PlayerStatus)

Poker = _reflection.GeneratedProtocolMessageType('Poker', (_message.Message,), {
  'DESCRIPTOR' : _POKER,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.Poker)
  })
_sym_db.RegisterMessage(Poker)

GetStatusRequest = _reflection.GeneratedProtocolMessageType('GetStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSREQUEST,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.GetStatusRequest)
  })
_sym_db.RegisterMessage(GetStatusRequest)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

ActionRequest = _reflection.GeneratedProtocolMessageType('ActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONREQUEST,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.ActionRequest)
  })
_sym_db.RegisterMessage(ActionRequest)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONRESPONSE,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.ActionResponse)
  })
_sym_db.RegisterMessage(ActionResponse)

CreateRoomRequest = _reflection.GeneratedProtocolMessageType('CreateRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROOMREQUEST,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.CreateRoomRequest)
  })
_sym_db.RegisterMessage(CreateRoomRequest)

GetinRoomRequest = _reflection.GeneratedProtocolMessageType('GetinRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINROOMREQUEST,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.GetinRoomRequest)
  })
_sym_db.RegisterMessage(GetinRoomRequest)

RoomResponse = _reflection.GeneratedProtocolMessageType('RoomResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROOMRESPONSE,
  '__module__' : 'texas_pb2'
  # @@protoc_insertion_point(class_scope:texas.RoomResponse)
  })
_sym_db.RegisterMessage(RoomResponse)



_TEXAS = _descriptor.ServiceDescriptor(
  name='Texas',
  full_name='texas.Texas',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=975,
  serialized_end=1342,
  methods=[
  _descriptor.MethodDescriptor(
    name='UserLogin',
    full_name='texas.Texas.UserLogin',
    index=0,
    containing_service=None,
    input_type=_USERINFO,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UserRegister',
    full_name='texas.Texas.UserRegister',
    index=1,
    containing_service=None,
    input_type=_USERINFO,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='texas.Texas.GetStatus',
    index=2,
    containing_service=None,
    input_type=_GETSTATUSREQUEST,
    output_type=_GETSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Action',
    full_name='texas.Texas.Action',
    index=3,
    containing_service=None,
    input_type=_ACTIONREQUEST,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateRoom',
    full_name='texas.Texas.CreateRoom',
    index=4,
    containing_service=None,
    input_type=_CREATEROOMREQUEST,
    output_type=_ROOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetinRoom',
    full_name='texas.Texas.GetinRoom',
    index=5,
    containing_service=None,
    input_type=_GETINROOMREQUEST,
    output_type=_ROOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXAS)

DESCRIPTOR.services_by_name['Texas'] = _TEXAS

# @@protoc_insertion_point(module_scope)
