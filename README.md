# Python MCAP protobuf support

This package provides protobuf support for the Python MCAP file format reader.

## Installation

Install via [Pipenv](https://pipenv.pypa.io/en/latest/) by adding `mcap-protobuf-support` to your `Pipfile` or via the command line:

```bash
pipenv install mcap-protobuf-support
```

## MCAP protobuf writing example

First, compile all of your message definitions:

```bash
protoc *.proto --python_out .
```

Next, use the classes generated from those message definitions to register schema in the mcap file.

```python
from pathlib import Path
from typing import IO, Any

from mcap.mcap0.writer import Writer as McapWriter
from mcap_protobuf.schema import register_schema

from .complex_message_pb2 import ComplexMessage
from .simple_message_pb2 import SimpleMessage

output = open("example.mcap", "wb")
mcap_writer = McapWriter(output)
mcap_writer.start(profile="protobuf", library="test")

simple_schema_id = register_schema(writer=mcap_writer, message_class=SimpleMessage)

complex_schema_id = register_schema(
    writer=mcap_writer, message_class=ComplexMessage
)

simple_channel_id = mcap_writer.register_channel(
    topic="/simple_message",
    message_encoding="protobuf",
    schema_id=simple_schema_id,
)

complex_channel_id = mcap_writer.register_channel(
    topic="/complex_message",
    message_encoding="protobuf",
    schema_id=complex_schema_id,
)

for i in range(1, 11):
    simple_message = SimpleMessage(data=f"Hello MCAP protobuf world #{i}!")
    mcap_writer.add_message(
        channel_id=simple_channel_id,
        log_time=i * 1000,
        data=simple_message.SerializeToString(),
        publish_time=i * 1000,
    )
    complex_message = ComplexMessage(fieldA=f"Field A {i}", fieldB="Field B {i}")
    mcap_writer.add_message(
        channel_id=complex_channel_id,
        log_time=i * 1000,
        data=complex_message.SerializeToString(),
        publish_time=i * 1000,
    )

mcap_writer.finish()
output.close()
```

## MCAP protobuf decoding example

```python
from mcap.mcap0.stream_reader import StreamReader
from mcap_protobuf.decoder import Decoder

reader = StreamReader("my_data.mcap")
decoder = Decoder(reader)
for m in decoder.messages:
    print(m)
```

## Stay in touch

Join our [Slack channel](https://foxglove.dev/join-slack) to ask questions, share feedback, and stay up to date on what our team is working on.
