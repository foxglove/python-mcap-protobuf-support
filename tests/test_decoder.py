import hashlib
from io import BytesIO, RawIOBase
from typing import cast

from mcap.mcap0.stream_reader import StreamReader
from mcap_protobuf.decoder import Decoder

from .generate import generate_sample_data


def test_protobuf_decoder():
    output = BytesIO()
    generate_sample_data(output)
    assert (
        hashlib.sha256(output.getvalue()).hexdigest()
        == "98e4525e60b24435a3ee93b46f55f533a42b192db58d6bd1eca636d5b40078b8"
    )
    reader = StreamReader(cast(RawIOBase, output))
    decoder = Decoder(reader)
    messages = [m for m in decoder.messages]
    assert len(messages) == 20
