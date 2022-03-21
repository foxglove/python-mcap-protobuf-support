from typing import Any
import google.protobuf.descriptor_pb2
from mcap.mcap0.writer import Writer as McapWriter


def register_schema(writer: McapWriter, message_class: Any):
    fds = google.protobuf.descriptor_pb2.FileDescriptorSet()
    fds.file.append(google.protobuf.descriptor_pb2.FileDescriptorProto())
    fds.file[0].ParseFromString(message_class.DESCRIPTOR.file.serialized_pb)
    data = fds.SerializeToString()

    return writer.register_schema(
        name=message_class.DESCRIPTOR.name, encoding="protobuf", data=data
    )
