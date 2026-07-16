import unittest

from nodes.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_props(self):
    html = HTMLNode("h1", "Heere at the wall", None, {"class": "title", "id": "wall"})

    self.assertEqual(html.props_to_html(), 'class="title" id="wall"')

  def test_to_html(self):
    html = HTMLNode("h1", "Heere at the wall", None, {"class": "title", "id": "wall"})

    self.assertRaises(NotImplementedError, html.to_html)

  def test_repr(self):
    html = HTMLNode("h1", "Heere at the wall", None, {"class": "title"})

    self.assertEqual(repr(html), 'HTMLNode(h1, Heere at the wall, None, class="title")')


if __name__ == "__main__":
  unittest.main()
