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
        == "693af8e1f070bbd11a0bfc7e8c870f37b48672b133bc4af81d2ab5c5a5cc46bc"
    )
    reader = StreamReader(cast(RawIOBase, output))
    decoder = Decoder(reader)
    messages = [m for m in decoder.messages]
    assert len(messages) == 20
