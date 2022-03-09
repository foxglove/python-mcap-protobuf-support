from io import BytesIO

from .generate import generate_sample_data


def test_protobuf_writer():
    output = BytesIO()
    generate_sample_data(output)
    assert len(output.getvalue()) == 1632
