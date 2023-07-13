import unittest

from main import HashMap


class HashMapTestCase(unittest.TestCase):
    def test_put_and_get(self):
        hash_map = HashMap()
        hash_map.put("apple", 1)
        hash_map.put("banana", 2)
        hash_map.put("cherry", 3)

        self.assertEqual(hash_map.get("apple"), 1)
        self.assertEqual(hash_map.get("banana"), 2)
        self.assertEqual(hash_map.get("cherry"), 3)

    def test_len(self):
        hash_map = HashMap()
        self.assertEqual(len(hash_map), 0)

        hash_map.put("apple", 1)
        self.assertEqual(len(hash_map), 1)

        hash_map.put("banana", 2)
        hash_map.put("cherry", 3)
        self.assertEqual(len(hash_map), 3)

    def test_contains_key(self):
        hash_map = HashMap()
        hash_map.put("apple", 1)
        hash_map.put("banana", 2)

        self.assertTrue(hash_map.contains_key("apple"))
        self.assertTrue(hash_map.contains_key("banana"))
        self.assertFalse(hash_map.contains_key("cherry"))

    def test_keys(self):
        hash_map = HashMap()
        hash_map.put("apple", 1)
        hash_map.put("banana", 2)
        hash_map.put("cherry", 3)

        self.assertEqual(set(hash_map.keys()), {"apple", "banana", "cherry"})

    def test_values(self):
        hash_map = HashMap()
        hash_map.put("apple", 1)
        hash_map.put("banana", 2)
        hash_map.put("cherry", 3)

        self.assertEqual(set(hash_map.values()), {1, 2, 3})

    def test_items(self):
        hash_map = HashMap()
        hash_map.put("apple", 1)
        hash_map.put("banana", 2)
        hash_map.put("cherry", 3)

        self.assertEqual(set(hash_map.items()), {("apple", 1), ("banana", 2), ("cherry", 3)})

    def test_remove(self):
        hash_map = HashMap()
        hash_map.put("apple", 1)
        hash_map.put("banana", 2)
        hash_map.put("cherry", 3)

        hash_map.remove("banana")
        self.assertNotIn("banana", hash_map)
        self.assertEqual(len(hash_map), 2)


if __name__ == '__main__':
    unittest.main()
