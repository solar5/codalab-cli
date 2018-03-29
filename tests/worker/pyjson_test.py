import tempfile
import time
import unittest
from mock import Mock

from codalabworker import pyjson

class PyJSONTest(unittest.TestCase):
    def test_one(self):
        one = {
                "a_string": "blah",
                "a_set": set([1,3,4]),
                "a_list": [1,3,4],
                "list_of_sets": [
                    set(),
                    set([0])
                ]
        }
        s = pyjson.dumps(one)

        two = pyjson.loads(s)
        assert(two == one)
