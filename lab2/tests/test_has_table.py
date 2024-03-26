import unittest

from datastructures.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def test_init(self):
        table = HashTable[str, int]()

        self.assertIsInstance(table, HashTable)

    def test_set_and_get(self):
        table = HashTable[str, str]()
        table["key1"] = "value1"
        table["key2"] = "value2"

        self.assertEqual(table["key1"], "value1")
        self.assertEqual(table["key2"], "value2")

    def test_contains(self):
        table = HashTable[str, str]()
        table["key1"] = "value1"

        self.assertTrue("key1" in table)
        self.assertFalse("key2" in table)

    def test_del(self):
        table = HashTable[str, str]()
        table["key1"] = "value1"
        del table["key1"]

        self.assertFalse("key1" in table)

    def test_str(self):
        table = HashTable[str, str]()
        table["key1"] = "value1"

        self.assertEqual("{'key1' : 'value1'}", str(table))

    def test_len(self):
        table1 = HashTable[str, str]()
        table1["key1"] = "value1"
        table1["key2"] = "value2"

        table2 = HashTable[str, str]()
        table2["key1"] = "value1"
        table2["key2"] = "value2"
        table2["key3"] = "value2"

        self.assertEqual(2, len(table1))
        self.assertEqual(3, len(table2))

    def test_get(self):
        table = HashTable[str, str]()
        table["key1"] = "value1"

        self.assertEqual("value1", table.get("key1"))
        self.assertEqual(None, table.get("key2"))

    def test_values(self):
        table = HashTable[str, str]()
        table["key1"] = "value1"

        self.assertEqual(table.values(), ['value1'])

    def test_keys(self):
        table = HashTable[str, str]()
        table["key1"] = "value1"

        self.assertEqual(table.keys(), ['key1'])


if __name__ == "__main__":
    unittest.main()
