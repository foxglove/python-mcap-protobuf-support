from typing import Any, Dict

from google.protobuf.message import Message as ProtobufMessage
from mcap.mcap0.exceptions import McapError
from mcap.mcap0.records import Channel, Message, Schema
from mcap.mcap0.stream_reader import StreamReader


class Decoder:
    def __init__(self, reader: StreamReader):
        self.__reader = reader

    @property
    def messages(self):
        channels: Dict[int, Channel] = {}
        schemas: Dict[int, Schema] = {}
        for record in self.__reader.records:
            if isinstance(record, Schema):
                schemas[record.id] = record
                if record.encoding != "protobuf":
                    raise McapError(
                        f"Can't decode schema with encoding {record.encoding}"
                    )
            if isinstance(record, Channel):
                channels[record.id] = record
            if isinstance(record, Message):
                channel = channels[record.channel_id]
                schema = schemas[channel.schema_id]
                message = ProtobufMessage()
                message.ParseFromString(record.data)
                message.ListFields()
                yield (channel.topic, message)
