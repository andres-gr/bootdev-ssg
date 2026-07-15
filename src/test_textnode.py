import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    txt1 = TextNode("Heere at the wall", TextType.PLAIN)
    txt2 = TextNode("Heere at the wall", TextType.PLAIN)

    self.assertEqual(txt1, txt2)

  def test_repr(self):
    txt = TextNode("Heere at the wall", TextType.PLAIN)

    self.assertEqual(repr(txt), "TextNode(Heere at the wall, plain, None)")

  def test_neq(self):
    txt1 = TextNode("Heere at the wall", TextType.PLAIN)
    txt2 = TextNode("Heere at the wall", TextType.PLAIN, "https://example.com")

    self.assertNotEqual(txt1, txt2)


if __name__ == "__main__":
  unittest.main()
