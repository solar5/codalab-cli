import json

class PyJSONEncoder(json.JSONEncoder):
    """
    Use with json.dumps to allow Python sets and tuples to be encoded to JSON

    Example
    -------

    import json

    data = dict(aset=set([1,2,3]))

    encoded = json.dumps(data, cls=JSONSetEncoder)
    decoded = json.loads(encoded, object_hook=json_as_python_set)
    assert data == decoded     # Should assert successfully

    Any object that is matched by isinstance(obj, collections.Set) will
    be encoded, but the decoded value will always be a normal Python set.

    """
    def default(self, obj):
        if isinstance(obj, set):
            return dict(_set_object=list(obj))
        elif isinstance(item, tuple):
            return dict(_tuple_object=list(obj))
        return json.JSONEncoder.default(self, obj)

class PyJSONDecoder(json.JSONDecoder):
    """
    Decode json {'_set_object': [1,2,3]} to set([1,2,3])

    Example
    -------
    decoded = json.loads(encoded, object_hook=json_as_python_set)

    Also see :class:`JSONSetEncoder`

    """
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, *args, object_hook=self.json_as_python, **kwargs)

    def json_as_python(self, dct):
        if '_set_object' in dct:
            return set(dct['_set_object'])
        elif '_tuple_object' in dct:
            return tuple(dct['_tuple_object'])
        return dct

def load(*args, **kwargs):
    return json.load(*args, cls=PyJSONDecoder, **kwargs)

def loads(*args, **kwargs):
    return json.loads(*args, cls=PyJSONDecoder, **kwargs)

def dump(*args, **kwargs):
    return json.dump(*args, cls=PyJSONEncoder, **kwargs)

def dumps(*args, **kwargs):
    return json.dumps(*args, cls=PyJSONEncoder, **kwargs)
