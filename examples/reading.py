from mcap.mcap0.stream_reader import StreamReader
from mcap_protobuf.decoder import Decoder

reader = StreamReader("my_data.mcap")
decoder = Decoder(reader)
for m in decoder.messages:
    print(m)
