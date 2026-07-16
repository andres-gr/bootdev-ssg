import unittest

from nodes.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
  def test_to_html_p(self):
    nod = LeafNode("p", "Heere at the wall")

    self.assertEqual(nod.to_html(), "<p>Heere at the wall</p>")

  def test_to_html_a(self):
    nod = LeafNode("a", "Heere at the wall", {"href": "https://example.com"})

    self.assertEqual(
      nod.to_html(), '<a href="https://example.com">Heere at the wall</a>'
    )

  def test_to_html_span(self):
    nod = LeafNode("span", "Heere at the wall", {"id": "wall"})

    self.assertEqual(nod.to_html(), '<span id="wall">Heere at the wall</span>')


if __name__ == "__main__":
  unittest.main()
