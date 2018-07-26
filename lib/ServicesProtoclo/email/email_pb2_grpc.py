# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

# from email import email_pb2 as email_dot_email__pb2
import email_pb2 as email_dot_email__pb2

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
        request_serializer=email_dot_email__pb2.SendMailRequest.SerializeToString,
        response_deserializer=email_dot_email__pb2.SendMailResponse.FromString,
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
          request_deserializer=email_dot_email__pb2.SendMailRequest.FromString,
          response_serializer=email_dot_email__pb2.SendMailResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'email.EmailSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))