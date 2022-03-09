from pathlib import Path
from typing import IO, Any

from google.protobuf.descriptor_pb2 import FileDescriptorSet
from mcap.mcap0.writer import Writer as McapWriter

from .simple_pb2 import SimpleMessage


def generate_sample_data(output: IO[Any]):
    mcap_writer = McapWriter(output)
    mcap_writer.start(profile="protobuf", library="test")

    proto = Path("tests/SimpleMessage.out").read_bytes()
    fds = FileDescriptorSet.FromString(proto)
    schema_id = mcap_writer.register_schema(
        name="SimpleMessage", encoding="protobuf", data=fds.SerializeToString()
    )

    channel_id = mcap_writer.register_channel(
        topic="/chatter", message_encoding="protobuf", schema_id=schema_id
    )

    for i in range(1, 11):
        message = SimpleMessage(data=f"Hello MCAP protobuf world #{i}!")
        mcap_writer.add_message(
            channel_id=channel_id,
            log_time=i * 1000,
            data=message.SerializeToString(),
            publish_time=0,
        )

    mcap_writer.finish()
    output.seek(0)
