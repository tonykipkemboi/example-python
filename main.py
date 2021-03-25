import http.client
import json
import ssl
import sys
import grpc

from dfuse.bstream.v1 import bstream_pb2_grpc
from dfuse.bstream.v1.bstream_pb2 import BlocksRequestV2, STEP_IRREVERSIBLE, BLOCK_DETAILS_LIGHT
from dfuse.ethereum.codec.v1 import codec_pb2
from google.protobuf.json_format import MessageToJson


def token_for_api_key(apiKey):
    # Needs to be cached since this API is rate limited, the returned token is valid for 24h
    connection = http.client.HTTPSConnection("auth.dfuse.io")
    connection.request(
        'POST',
        '/v1/auth/issue',
        json.dumps({"api_key": apiKey}),
        {'Content-type': 'application/json'},
    )
    response = connection.getresponse()

    if response.status != 200:
        raise Exception(
            f" Status: {response.status} reason: {response.reason}")

    token = json.loads(response.read().decode())['token']
    connection.close()

    return token


def blockstream_v2():
    credentials = grpc.access_token_call_credentials(
        token_for_api_key(sys.argv[1]))
    channel = grpc.secure_channel(
        'bsc.streamingfast.io:443',
        credentials=grpc.composite_channel_credentials(grpc.ssl_channel_credentials(),
                                                       credentials))
    return bstream_pb2_grpc.BlockStreamV2Stub(channel)


def block_stats(block):
    call_count = 0
    log_count = 0
    for trx_trace in block.transaction_traces:
        for call in trx_trace.calls:
            log_count += len(call.logs)

        call_count += len(trx_trace.calls)

    return len(block.transaction_traces), call_count, log_count


def main():
    if len(sys.argv) <= 1:
        print("Error: Wrong number of arguments")
        print()
        print("usage: python3 main.py <apiKey> --full")
        exit(1)

    blockstream = blockstream_v2()
    stream = blockstream.Blocks(BlocksRequestV2(
        start_block_num=5_975_000,
        stop_block_num=5_975_010,

        # This could be used to filter the block so it contains only transactions you are intersted in
        # See https://github.com/streamingfast/streamingfast-client#query-language for details
        # include_filter_expr="to == '0x7a250d5630b4cf539739df2c5dacb4c659f2488d'"

        # Shows only block that are deemed "irreversible" (200 confirmations hard-coded for now)
        # To be live and deal with forks, use [STEP_NEW, STEP_UNDO]
        fork_steps=[STEP_IRREVERSIBLE],
    ))

    print_full = len(sys.argv) > 2 and sys.argv[2] == "--full"

    for response in stream:
        block = codec_pb2.Block()
        succeed = response.block.Unpack(block)
        if succeed != True:
            raise Exception(
                "Invalid target type, field to unpack is of type {} but tried to unpack it into type {}".format(response.block.TypeName(), block.DESCRIPTOR.full_name))

        trx_count, call_count, log_count = block_stats(block)

        print(
            "Block #{} ({}) - {} Transactions ({} calls, {} logs)".format(block.number, block.hash.hex(), trx_count, call_count, log_count))
        if print_full:
            print(MessageToJson(block))


main()
