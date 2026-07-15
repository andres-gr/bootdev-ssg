import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    txt1 = TextNode("Heere at the wall", TextType.TEXT)
    txt2 = TextNode("Heere at the wall", TextType.TEXT)

    self.assertEqual(txt1, txt2)

  def test_repr(self):
    txt = TextNode("Heere at the wall", TextType.TEXT)

    self.assertEqual(repr(txt), "TextNode(Heere at the wall, text, None)")

  def test_neq(self):
    txt1 = TextNode("Heere at the wall", TextType.TEXT)
    txt2 = TextNode("Heere at the wall", TextType.TEXT, "https://example.com")

    self.assertNotEqual(txt1, txt2)

  def test_bold(self):
    node = TextNode("Bold", TextType.BOLD)
    html = text_node_to_html_node(node)

    self.assertEqual(html.to_html(), "<b>Bold</b>")
    self.assertEqual(html.tag, "b")
    self.assertEqual(html.value, "Bold")

  def test_code(self):
    node = TextNode("Code", TextType.CODE)
    html = text_node_to_html_node(node)

    self.assertEqual(html.to_html(), "<code>Code</code>")
    self.assertEqual(html.tag, "code")
    self.assertEqual(html.value, "Code")

  def test_image(self):
    node = TextNode("Image", TextType.IMAGE, "https://example.com/image.png")
    html = text_node_to_html_node(node)

    self.assertEqual(
      html.to_html(), '<img src="https://example.com/image.png" alt="Image"></img>'
    )
    self.assertEqual(html.tag, "img")

    if html.props:
      self.assertEqual(html.props["alt"], "Image")
      self.assertEqual(html.props["src"], "https://example.com/image.png")

  def test_italic(self):
    node = TextNode("Italic", TextType.ITALIC)
    html = text_node_to_html_node(node)

    self.assertEqual(html.to_html(), "<i>Italic</i>")
    self.assertEqual(html.tag, "i")
    self.assertEqual(html.value, "Italic")

  def test_link(self):
    node = TextNode("Link", TextType.LINK, "https://example.com")
    html = text_node_to_html_node(node)

    self.assertEqual(html.to_html(), '<a href="https://example.com">Link</a>')

    if html.props:
      self.assertEqual(html.tag, "a")
      self.assertEqual(html.props["href"], "https://example.com")

  def test_text(self):
    node = TextNode("Text", TextType.TEXT)
    html = text_node_to_html_node(node)

    self.assertEqual(html.to_html(), "Text")
    self.assertEqual(html.tag, None)
    self.assertEqual(html.value, "Text")


if __name__ == "__main__":
  unittest.main()
