import unittest
import json
import sys
sys.path.append('../')

import filesort.core as fs
import toJson.core as tojson
from Vector.core import Vector
import wr.core as wr
from fromJson.core import from_json, is_digit
import Singleton.core as st


class Tests(unittest.TestCase):
    fs.sort("numbers.txt", "output.txt")

    def test_filesort(self):
        def correct_sort(filename):
            with open(filename) as f:
                line = f.readline()
                while line:
                    cur_line = f.readline()
                    if int(line) > int(cur_line):
                        return False
                    line = f.readline()
            return True

        self.assertTrue(correct_sort("output.txt"))

    def test_json(self):
        d = {
            "name": "Viktor",
            "age": 30,
            "married": True,
            "divorced": False,
            "children": ("Anna", "Bogdan"),
            "pets": None,
            "cars": [
                {"model": "BMW 230", "mpg": 27.5},
                {"model": "Ford Edge", "mpg": 24.1}
            ]
        }
        str_ = json.dumps(d)
        self.assertEqual(json.dumps(d), tojson.obj_to_json(d))
        self.assertEqual(json.loads(str_), from_json(str_))

    def test_vector(self):
        v1 = Vector(1, 2, 3, 4)
        v2 = Vector(4, 3, 2, 1)
        v0 = Vector(0, 0, 0, 0)
        v3 = Vector()
        self.assertEqual(v1 + v2, Vector(5, 5, 5, 5))
        self.assertEqual(v1 - v1, Vector(0, 0, 0, 0))
        self.assertEqual(v1 * v2, Vector(4, 6, 6, 4))
        self.assertTrue(v1 == v1)
        self.assertFalse(v1 != v1)
        self.assertEqual(2 * v1, v1 * 2)
        self.assertEqual(v1 * 2, Vector(2, 4, 6, 8))
        self.assertTrue(v0 < v1)
        self.assertTrue(v0 <= v1)
        self.assertFalse(v0 > v1)
        self.assertFalse(v0 >= v1)
        self.assertEqual(v1 ** 2, Vector(1, 4, 9, 16))
        self.assertFalse(v1 == v2)
        self.assertTrue(v1 != v2)
        self.assertEqual(v1[99], -1)
        self.assertEqual(str(v1), '(1, 2, 3, 4)')
        self.assertEqual(v1[0], 1)

    def test_wrapper(self):
        self.assertEqual(wr.sum_(1, 2, 3, 4, 5), wr.sum_(1, 2, 3, 4, 5))
        self.assertEqual(wr.mul_(1, 2, 3, 4, 5), wr.mul_(1, 2, 3, 4, 5))

    def test_singelton(self):
        x1 = st.Cl()
        x2 = st.Cl()
        self.assertEqual(x1, x2)


if __name__ == '__main__':
    unittest.main()
