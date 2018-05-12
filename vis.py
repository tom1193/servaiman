PORT_NUM = ':50051'

CN = servaiman_pb2.TwoDMatrix()
AB = servaiman_pb2.TwoDMatrix()
CF = servaiman_pb2.TwoDMatrix()
DIMS = []
GNB = 2

def matrix(rows, data):
    return np.array(data).reshape(rows, len(data)//rows)

def streamToNp(responses, field):
    first = True
    for response in responses:
        if first: field.rows = response.rows
        field.data.extend(response.data)
    mat = matrix(field.rows, field.data)
    print(str(field.rows))
    print(mat[0][0])
    print(mat.shape)
        
def getMeta(stub):
    response = stub.GetMeta(servaiman_pb2.Request(size=10))
    DIMS = response.dims
    GNB = response.gnb
        
def getCN(stub):
    global CN
    responses = stub.GetCn(servaiman_pb2.Request(size=10))
    streamToNp(responses, CN)
    
def getAB(stub):
    global AB
    responses = stub.GetAb(servaiman_pb2.Request(size=10))
    streamToNp(responses, AB)
    
def getCF(stub):
    global CF
    responses = stub.GetCf(servaiman_pb2.Request(size=10))
    streamToNp(responses, CF)

def run():
    channel = grpc.insecure_channel('localhost'+PORT_NUM)
    stub = servaiman_pb2_grpc.ServaimanStub(channel)
    getMeta(stub)
    getCN(stub)
    getAB(stub)
    getCF(stub)
    

if __name__ == '__main__':
    run()