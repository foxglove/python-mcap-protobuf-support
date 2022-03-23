import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from mcap.mcap0.stream_reader import StreamReader
from mcap_protobuf.decoder import Decoder

reader = StreamReader("example.mcap")
decoder = Decoder(reader)
for m in decoder.messages:
    print(m)
