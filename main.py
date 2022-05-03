#!/usr/bin/env python3

import http.client
#import json
#import ssl
import sys
import os
import grpc

from sf.substreams.v1 import substreams_pb2_grpc
from sf.substreams.v1.substreams_pb2 import Request, Response, STEP_IRREVERSIBLE
from sf.substreams.v1.manifest_pb2 import Manifest
import sf.ethereum.type.v1.type_pb2 as eth_pb2
#from google.protobuf.json_format import MessageToJson

jwt_token = os.getenv("SUBSTREAMS_API_TOKEN")
if not jwt_token: raise Error("set SUBSTREAMS_API_TOKEN")
endpoint = "bsc-dev.streamingfast.io:443"
manifest_yaml_pb = "../substreams-playground/pcs-rust/substreams.yaml.pb"
output_modules = ["block_to_pairs", "pairs"]
start_block = 6_810_706
end_block = 6_810_710

def substreams_service():
    credentials = grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(),
        grpc.access_token_call_credentials(jwt_token),
    )
    channel = grpc.secure_channel(endpoint, credentials=credentials)
    return substreams_pb2_grpc.StreamStub(channel)

def main():
    with open(manifest_yaml_pb, 'rb') as f:
        manifest = Manifest()
        manifest.ParseFromString(f.read())

    service = substreams_service()
    stream = service.Blocks(Request(
        start_block_num=start_block,
        stop_block_num=end_block,
        fork_steps=[STEP_IRREVERSIBLE],
        manifest=manifest,
        output_modules=output_modules,
    ))

    for response in stream:
        print(response)

main()
