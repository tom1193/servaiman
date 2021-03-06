# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import servaiman_pb2 as servaiman__pb2


class ServaimanStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PostMeta = channel.unary_unary(
        '/servaiman_proto.Servaiman/PostMeta',
        request_serializer=servaiman__pb2.Meta.SerializeToString,
        response_deserializer=servaiman__pb2.Status.FromString,
        )
    self.PostCn = channel.stream_unary(
        '/servaiman_proto.Servaiman/PostCn',
        request_serializer=servaiman__pb2.TwoDMatrix.SerializeToString,
        response_deserializer=servaiman__pb2.Status.FromString,
        )
    self.PostAb = channel.stream_unary(
        '/servaiman_proto.Servaiman/PostAb',
        request_serializer=servaiman__pb2.TwoDMatrix.SerializeToString,
        response_deserializer=servaiman__pb2.Status.FromString,
        )
    self.PostCf = channel.stream_unary(
        '/servaiman_proto.Servaiman/PostCf',
        request_serializer=servaiman__pb2.TwoDMatrix.SerializeToString,
        response_deserializer=servaiman__pb2.Status.FromString,
        )
    self.GetMeta = channel.unary_unary(
        '/servaiman_proto.Servaiman/GetMeta',
        request_serializer=servaiman__pb2.Request.SerializeToString,
        response_deserializer=servaiman__pb2.Meta.FromString,
        )
    self.GetCn = channel.unary_stream(
        '/servaiman_proto.Servaiman/GetCn',
        request_serializer=servaiman__pb2.Request.SerializeToString,
        response_deserializer=servaiman__pb2.TwoDMatrix.FromString,
        )
    self.GetAb = channel.unary_stream(
        '/servaiman_proto.Servaiman/GetAb',
        request_serializer=servaiman__pb2.Request.SerializeToString,
        response_deserializer=servaiman__pb2.TwoDMatrix.FromString,
        )
    self.GetCf = channel.unary_stream(
        '/servaiman_proto.Servaiman/GetCf',
        request_serializer=servaiman__pb2.Request.SerializeToString,
        response_deserializer=servaiman__pb2.TwoDMatrix.FromString,
        )


class ServaimanServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PostMeta(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PostCn(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PostAb(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PostCf(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMeta(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAb(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCf(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServaimanServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PostMeta': grpc.unary_unary_rpc_method_handler(
          servicer.PostMeta,
          request_deserializer=servaiman__pb2.Meta.FromString,
          response_serializer=servaiman__pb2.Status.SerializeToString,
      ),
      'PostCn': grpc.stream_unary_rpc_method_handler(
          servicer.PostCn,
          request_deserializer=servaiman__pb2.TwoDMatrix.FromString,
          response_serializer=servaiman__pb2.Status.SerializeToString,
      ),
      'PostAb': grpc.stream_unary_rpc_method_handler(
          servicer.PostAb,
          request_deserializer=servaiman__pb2.TwoDMatrix.FromString,
          response_serializer=servaiman__pb2.Status.SerializeToString,
      ),
      'PostCf': grpc.stream_unary_rpc_method_handler(
          servicer.PostCf,
          request_deserializer=servaiman__pb2.TwoDMatrix.FromString,
          response_serializer=servaiman__pb2.Status.SerializeToString,
      ),
      'GetMeta': grpc.unary_unary_rpc_method_handler(
          servicer.GetMeta,
          request_deserializer=servaiman__pb2.Request.FromString,
          response_serializer=servaiman__pb2.Meta.SerializeToString,
      ),
      'GetCn': grpc.unary_stream_rpc_method_handler(
          servicer.GetCn,
          request_deserializer=servaiman__pb2.Request.FromString,
          response_serializer=servaiman__pb2.TwoDMatrix.SerializeToString,
      ),
      'GetAb': grpc.unary_stream_rpc_method_handler(
          servicer.GetAb,
          request_deserializer=servaiman__pb2.Request.FromString,
          response_serializer=servaiman__pb2.TwoDMatrix.SerializeToString,
      ),
      'GetCf': grpc.unary_stream_rpc_method_handler(
          servicer.GetCf,
          request_deserializer=servaiman__pb2.Request.FromString,
          response_serializer=servaiman__pb2.TwoDMatrix.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'servaiman_proto.Servaiman', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
