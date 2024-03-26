import unittest

from datastructures.stack import Stack


class TestStack(unittest.TestCase):
    def test_init(self):
        st = Stack[str]()

        self.assertIsInstance(st, Stack)

    def test_str_and_push(self):
        st = Stack[str]()
        st.push("3")
        st.push("2")
        st.push("1")

        self.assertEqual("['1','2','3']", str(st))

    def test_pop(self):
        st = Stack[str]()
        st.push("2")
        st.push("1")

        self.assertEqual(st.pop(), "1")

    def test_len_and_comparisons(self):
        st1 = Stack[str]()
        st1.push("3")
        st1.push("2")
        st1.push("1")

        st2 = Stack[str]()
        st2.push("2")
        st2.push("1")

        st3 = Stack[str]()
        st3.push("3")
        st3.push("2")
        st3.push("1")

        self.assertEqual(3, len(st1))
        self.assertEqual(2, len(st2))
        self.assertEqual(3, len(st3))

        self.assertTrue(st1 > st2)
        self.assertFalse(st2 > st1)

        self.assertTrue(st2 < st1)
        self.assertFalse(st1 < st2)

        self.assertTrue(st1 >= st2)
        self.assertFalse(st2 >= st1)
        self.assertTrue(st1 >= st3)
        self.assertTrue(st3 >= st1)

        self.assertFalse(st1 <= st2)
        self.assertTrue(st2 <= st1)
        self.assertTrue(st1 <= st3)
        self.assertTrue(st3 <= st1)

    def test_add(self):
        st1 = Stack[str]()
        st1.push("3")
        st1.push("2")
        st1.push("1")

        st2 = Stack[str]()
        st2.push("5")
        st2.push("4")

        self.assertEqual("['1','2','3','4','5']", str(st1 + st2))

    def test_is_empty(self):
        st1 = Stack[str]()
        st1.push("3")
        st1.push("2")
        st1.push("1")

        st2 = Stack[str]()

        self.assertTrue(st2.is_empty())
        self.assertFalse(st1.is_empty())

    def test_first_and_last(self):
        st = Stack[str]()
        st.push("3")
        st.push("2")
        st.push("1")

        self.assertEqual(st.first(), "1")
        self.assertEqual(st.last(), "3")


if __name__ == "__main__":
    unittest.main()
