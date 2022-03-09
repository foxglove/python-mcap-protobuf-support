# Python MCAP protobuf support

This package provides protobuf support for the Python MCAP file format reader &amp; writer.

## Installation

Install via [Pipenv](https://pipenv.pypa.io/en/latest/) by adding `mcap-protobuf-support` to your `Pipfile` or via the command line:

```bash
pipenv install mcap-protobuf-support
```

## Example Usage

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
