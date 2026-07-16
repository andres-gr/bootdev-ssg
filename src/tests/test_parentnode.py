import unittest

from nodes.leafnode import LeafNode
from nodes.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
  def test_to_html_with_childs(self):
    child = LeafNode("span", "Heere at the child")
    paren = ParentNode("div", [child])

    self.assertEqual(paren.to_html(), "<div><span>Heere at the child</span></div>")

  def test_to_html_with_paren_childs(self):
    child = LeafNode("span", "Heere at the child")
    paren = ParentNode("div", [child], {"class": "paren"})
    top_paren = ParentNode("div", [paren])

    self.assertEqual(
      top_paren.to_html(),
      '<div><div class="paren"><span>Heere at the child</span></div></div>',
    )

  def test_to_html_with_empty_childs(self):
    child = LeafNode(None, "Heere at the child")
    paren = ParentNode("div", [child])

    self.assertEqual(paren.to_html(), "<div>Heere at the child</div>")

  def test_to_html_with_empty_paren_childs(self):
    child = LeafNode("p", "Heere at the child")
    sib = ParentNode("div", [child], {"class": "sib"})
    paren = ParentNode("div", [child, sib])

    self.assertEqual(
      paren.to_html(),
      '<div><p>Heere at the child</p><div class="sib"><p>Heere at the child</p></div></div>',
    )


if __name__ == "__main__":
  unittest.main()
