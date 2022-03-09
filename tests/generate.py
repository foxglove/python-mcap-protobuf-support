from pathlib import Path
from typing import IO, Any

from google.protobuf.descriptor_pb2 import FileDescriptorSet
from mcap.mcap0.writer import Writer as McapWriter

from .Messages_pb2 import SimpleMessage, ComplexMessage


def generate_sample_data(output: IO[Any]):
    mcap_writer = McapWriter(output)
    mcap_writer.start(profile="protobuf", library="test")

    proto = Path("tests/Messages.fds").read_bytes()
    print(proto)
    fds = FileDescriptorSet.FromString(proto)
    print(fds.SerializeToString() == proto)
    simple_schema_id = mcap_writer.register_schema(
        name="SimpleMessage", encoding="protobuf", data=fds.SerializeToString()
    )
    complex_schema_id = mcap_writer.register_schema(
        name="ComplexMessage", encoding="protobuf", data=fds.SerializeToString()
    )

    simple_channel_id = mcap_writer.register_channel(
        topic="/chatter_simple", message_encoding="protobuf", schema_id=simple_schema_id
    )

    complex_channel_id = mcap_writer.register_channel(
        topic="/chatter_complex",
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
    output.seek(0)
