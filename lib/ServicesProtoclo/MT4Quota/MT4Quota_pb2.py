# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MT4Quota/MT4Quota.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MT4Quota/MT4Quota.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x17MT4Quota/MT4Quota.proto\">\n\x05Quote\x12\t\n\x01\x62\x18\x01 \x02(\x01\x12\t\n\x01\x61\x18\x02 \x02(\x01\x12\t\n\x01s\x18\x03 \x02(\t\x12\t\n\x01t\x18\x04 \x02(\x01\x12\t\n\x01\x64\x18\x05 \x02(\x05')
)




_QUOTE = _descriptor.Descriptor(
  name='Quote',
  full_name='Quote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='b', full_name='Quote.b', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a', full_name='Quote.a', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s', full_name='Quote.s', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t', full_name='Quote.t', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='d', full_name='Quote.d', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['Quote'] = _QUOTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Quote = _reflection.GeneratedProtocolMessageType('Quote', (_message.Message,), dict(
  DESCRIPTOR = _QUOTE,
  __module__ = 'MT4Quota.MT4Quota_pb2'
  # @@protoc_insertion_point(class_scope:Quote)
  ))
_sym_db.RegisterMessage(Quote)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)