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
        == "674168d7005e806cc89401385b962fcaa650d34ed2927c4ae25dfc991cb9e321"
    )
    reader = StreamReader(cast(RawIOBase, output))
    decoder = Decoder(reader)
    messages = [m for m in decoder.messages]
    assert len(messages) == 20
