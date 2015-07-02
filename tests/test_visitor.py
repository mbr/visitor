import json


def test_example_code():
    from example import JSONEncoder, data

    json.loads(JSONEncoder().visit(data))
