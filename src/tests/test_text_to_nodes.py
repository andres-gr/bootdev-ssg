import unittest

from nodes.textnode import TextNode, TextType
from utils.text_to_nodes import text_to_nodes


class TestTextToNodes(unittest.TestCase):
  def test_empty(self):
    txt = ""

    self.assertRaises(ValueError, text_to_nodes, txt)

  def test_no_text(self):
    txt = " "
    res = text_to_nodes(txt)

    self.assertEqual(res, [])

  def test_all_types(self):
    txt = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    res = text_to_nodes(txt)

    self.assertListEqual(
      res,
      [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ],
    )


if __name__ == "__main__":
  unittest.main()
