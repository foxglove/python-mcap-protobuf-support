from io import BytesIO

from mcap.mcap0.stream_reader import StreamReader
from mcap_protobuf.decoder import Decoder

from .generate import generate_sample_data


def test_protobuf_decoder():
    pass
    # output = BytesIO()
    # generate_sample_data(output)
    # reader = StreamReader(output)
    # decoder = Decoder(reader)
    # for message in decoder.messages:
    #     print(message)
