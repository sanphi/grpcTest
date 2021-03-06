# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: email/email.proto

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
  name='email/email.proto',
  package='email',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x65mail/email.proto\x12\x05\x65mail\"h\n\x0fSendMailRequest\x12\n\n\x02To\x18\x01 \x01(\t\x12\x0f\n\x07Subject\x18\x02 \x01(\t\x12\x0c\n\x04\x42ody\x18\x03 \x01(\t\x12\x12\n\nIsBodyHtml\x18\x04 \x01(\x08\x12\x16\n\x0eMaxResendTimes\x18\x05 \x01(\x05\"9\n\x10SendMailResponse\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x14\n\x0c\x45rrorMessage\x18\x02 \x01(\t2E\n\x08\x45mailSrv\x12\x39\n\x04Send\x12\x16.email.SendMailRequest\x1a\x17.email.SendMailResponse\"\x00\x42\x0b\xaa\x02\x08\x46M.Emailb\x06proto3')
)




_SENDMAILREQUEST = _descriptor.Descriptor(
  name='SendMailRequest',
  full_name='email.SendMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='To', full_name='email.SendMailRequest.To', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Subject', full_name='email.SendMailRequest.Subject', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Body', full_name='email.SendMailRequest.Body', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IsBodyHtml', full_name='email.SendMailRequest.IsBodyHtml', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MaxResendTimes', full_name='email.SendMailRequest.MaxResendTimes', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=132,
)


_SENDMAILRESPONSE = _descriptor.Descriptor(
  name='SendMailResponse',
  full_name='email.SendMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='email.SendMailResponse.Success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ErrorMessage', full_name='email.SendMailResponse.ErrorMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['SendMailRequest'] = _SENDMAILREQUEST
DESCRIPTOR.message_types_by_name['SendMailResponse'] = _SENDMAILRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendMailRequest = _reflection.GeneratedProtocolMessageType('SendMailRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDMAILREQUEST,
  __module__ = 'email.email_pb2'
  # @@protoc_insertion_point(class_scope:email.SendMailRequest)
  ))
_sym_db.RegisterMessage(SendMailRequest)

SendMailResponse = _reflection.GeneratedProtocolMessageType('SendMailResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDMAILRESPONSE,
  __module__ = 'email.email_pb2'
  # @@protoc_insertion_point(class_scope:email.SendMailResponse)
  ))
_sym_db.RegisterMessage(SendMailResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\010FM.Email'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class EmailSrvStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Send = channel.unary_unary(
          '/email.EmailSrv/Send',
          request_serializer=SendMailRequest.SerializeToString,
          response_deserializer=SendMailResponse.FromString,
          )


  class EmailSrvServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Send(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_EmailSrvServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Send': grpc.unary_unary_rpc_method_handler(
            servicer.Send,
            request_deserializer=SendMailRequest.FromString,
            response_serializer=SendMailResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'email.EmailSrv', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaEmailSrvServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Send(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaEmailSrvStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Send(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Send.future = None


  def beta_create_EmailSrv_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('email.EmailSrv', 'Send'): SendMailRequest.FromString,
    }
    response_serializers = {
      ('email.EmailSrv', 'Send'): SendMailResponse.SerializeToString,
    }
    method_implementations = {
      ('email.EmailSrv', 'Send'): face_utilities.unary_unary_inline(servicer.Send),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_EmailSrv_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('email.EmailSrv', 'Send'): SendMailRequest.SerializeToString,
    }
    response_deserializers = {
      ('email.EmailSrv', 'Send'): SendMailResponse.FromString,
    }
    cardinalities = {
      'Send': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'email.EmailSrv', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
