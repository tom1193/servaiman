from concurrent import futures
from threading import Thread
import time
import sys
import grpc
import numpy as np

sys.path.insert(0, '../servaiman_proto')
import servaiman_pb2
import servaiman_pb2_grpc

PORT_NUM = '[::]:50051'
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

CN = servaiman_pb2.TwoDMatrix()
AB = servaiman_pb2.TwoDMatrix()
CF = servaiman_pb2.TwoDMatrix()
DIMS = [0,0]
GNB = 2

NUM_EL_PER_CHUNK = 64*1024//8  #recommended chunk size for grpc streaming is 16 to 64 KiB
def responseChunker(field):
    for i in range(0, len(field.data), NUM_EL_PER_CHUNK):
        if (i + NUM_EL_PER_CHUNK > len(field.data)):
            yield servaiman_pb2.TwoDMatrix(rows=field.rows, data=field.data[i:])
        else:
            yield servaiman_pb2.TwoDMatrix(rows=field.rows, data=field.data[i:i+NUM_EL_PER_CHUNK])

class Servaiman(servaiman_pb2_grpc.ServaimanServicer):
    
    #POST methods called by caiman/onacid
    def PostMeta(self, request, context):
        global DIMS, GNB
        DIMS = request.dims
        GNB = request.gnb
        print(str(DIMS), str(GNB))
        return servaiman_pb2.Status(success=True)
    
    def PostCn(self, request_iterator, context):
        global CN
        CN = servaiman_pb2.TwoDMatrix()
        start_time = time.time()
        first = True
        for chunk in request_iterator:
            if first: CN.rows = chunk.rows
            CN.data.extend(chunk.data)
        elapsed_time = time.time() - start_time
        print("cn length:"+ str(len(CN.data)))
        print("PostCn: " + str(elapsed_time))
        return servaiman_pb2.Status(success=True)
    
    def PostAb(self, request_iterator, context):
        global AB
        AB = servaiman_pb2.TwoDMatrix()
        start_time = time.time()
        first = True
        for chunk in request_iterator:
            if first: AB.rows = chunk.rows
            AB.data.extend(chunk.data)
        elapsed_time = time.time() - start_time
        print("ab length:"+ str(len(AB.data)))
        print("PostAb: " + str(elapsed_time))
        return servaiman_pb2.Status(success=True)

    def PostCf(self, request_iterator, context):
        global CF
        CF = servaiman_pb2.TwoDMatrix()
        start_time = time.time()
        first = True
        for chunk in request_iterator:
            if first: CF.rows = chunk.rows
            CF.data.extend(chunk.data)
        elapsed_time = time.time() - start_time
        print("cf length:"+ str(len(CF.data)))
        print("PostCf: " + str(elapsed_time))
        return servaiman_pb2.Status(success=True)
    
    #GET methods called by visualization client
    def GetMeta(self, request, context):
        print(request.size)
        return servaiman_pb2.Meta(dims=DIMS,gnb = GNB)
    
    def GetCn(self, request, context):
        return responseChunker(CN)
        
    def GetAb(self, request, context):
        return responseChunker(AB)
    
    def GetCf(self, request, context):
        return responseChunker(CF)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servaiman_pb2_grpc.add_ServaimanServicer_to_server(Servaiman(), server)
    server.add_insecure_port(PORT_NUM)
    print("Servaiman Running")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

