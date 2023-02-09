# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mila.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mila.proto',
  package='mila',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nmila.proto\x12\x04mila\x1a\x1bgoogle/protobuf/empty.proto\"\x16\n\x06\x43lient\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x16\n\x05Token\x12\r\n\x05token\x18\x01 \x01(\t\",\n\nCheckpoint\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\">\n\x05Model\x12\x1a\n\x12json_configuration\x18\x01 \x01(\x0c\x12\x19\n\x11latest_checkpoint\x18\x02 \x01(\x0c\x32\x81\x02\n\x04Mila\x12+\n\x0c\x41uthenticate\x12\x0c.mila.Client\x1a\x0b.mila.Token\"\x00\x12\x32\n\tHeartbeat\x12\x0b.mila.Token\x1a\x16.google.protobuf.Empty\"\x00\x12.\n\x05\x43lose\x12\x0b.mila.Token\x1a\x16.google.protobuf.Empty\"\x00\x12*\n\x0cRequestModel\x12\x0b.mila.Token\x1a\x0b.mila.Model\"\x00\x12<\n\x0eSendCheckpoint\x12\x10.mila.Checkpoint\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='mila.Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mila.Client.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=49,
  serialized_end=71,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='mila.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='mila.Token.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=73,
  serialized_end=95,
)


_CHECKPOINT = _descriptor.Descriptor(
  name='Checkpoint',
  full_name='mila.Checkpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='mila.Checkpoint.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='mila.Checkpoint.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=97,
  serialized_end=141,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='mila.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_configuration', full_name='mila.Model.json_configuration', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latest_checkpoint', full_name='mila.Model.latest_checkpoint', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=143,
  serialized_end=205,
)

DESCRIPTOR.message_types_by_name['Client'] = _CLIENT
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['Checkpoint'] = _CHECKPOINT
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), dict(
  DESCRIPTOR = _CLIENT,
  __module__ = 'mila_pb2'
  # @@protoc_insertion_point(class_scope:mila.Client)
  ))
_sym_db.RegisterMessage(Client)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), dict(
  DESCRIPTOR = _TOKEN,
  __module__ = 'mila_pb2'
  # @@protoc_insertion_point(class_scope:mila.Token)
  ))
_sym_db.RegisterMessage(Token)

Checkpoint = _reflection.GeneratedProtocolMessageType('Checkpoint', (_message.Message,), dict(
  DESCRIPTOR = _CHECKPOINT,
  __module__ = 'mila_pb2'
  # @@protoc_insertion_point(class_scope:mila.Checkpoint)
  ))
_sym_db.RegisterMessage(Checkpoint)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), dict(
  DESCRIPTOR = _MODEL,
  __module__ = 'mila_pb2'
  # @@protoc_insertion_point(class_scope:mila.Model)
  ))
_sym_db.RegisterMessage(Model)



_MILA = _descriptor.ServiceDescriptor(
  name='Mila',
  full_name='mila.Mila',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=208,
  serialized_end=465,
  methods=[
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='mila.Mila.Authenticate',
    index=0,
    containing_service=None,
    input_type=_CLIENT,
    output_type=_TOKEN,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Heartbeat',
    full_name='mila.Mila.Heartbeat',
    index=1,
    containing_service=None,
    input_type=_TOKEN,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Close',
    full_name='mila.Mila.Close',
    index=2,
    containing_service=None,
    input_type=_TOKEN,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RequestModel',
    full_name='mila.Mila.RequestModel',
    index=3,
    containing_service=None,
    input_type=_TOKEN,
    output_type=_MODEL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendCheckpoint',
    full_name='mila.Mila.SendCheckpoint',
    index=4,
    containing_service=None,
    input_type=_CHECKPOINT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MILA)

DESCRIPTOR.services_by_name['Mila'] = _MILA

# @@protoc_insertion_point(module_scope)
