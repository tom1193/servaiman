#!/bin/bash
python -m grpc_tools.protoc -I./protos --python_out=protos --gg rpc_python_out=protos protos/servaiman.proto