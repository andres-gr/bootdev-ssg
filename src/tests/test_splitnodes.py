import unittest

from nodes.textnode import TextNode, TextType
from utils.splitnodes import split_nodes_delimiter, split_nodes_image


class TestSplitNodesDelimiter(unittest.TestCase):
  def test_no_delimiters(self):
    nodes = [
      TextNode("Heere at ", TextType.TEXT),
      TextNode("the wall", TextType.TEXT),
    ]
    res = split_nodes_delimiter(nodes, "", TextType.TEXT)

    self.assertEqual(res, nodes)

  def test_with_delimiters(self):
    nodes = [
      TextNode("Heere `at the` wall", TextType.TEXT),
    ]
    res = split_nodes_delimiter(nodes, "`", TextType.CODE)

    self.assertEqual(
      res,
      [
        TextNode("Heere ", TextType.TEXT),
        TextNode("at the", TextType.CODE),
        TextNode(" wall", TextType.TEXT),
      ],
    )


class TestSplitNodesImage(unittest.TestCase):
  def test_split_only_no_images(self):
    nodes = [
      TextNode("heere there are no images", TextType.TEXT),
      TextNode("another no images text", TextType.TEXT),
    ]
    nodes = split_nodes_image(nodes)

    self.assertListEqual(
      nodes,
      [
        TextNode("heere there are no images", TextType.TEXT),
        TextNode("another no images text", TextType.TEXT),
      ],
    )

  def test_split_only_one_image(self):
    nodes = [
      TextNode("![the image](https://web.co/image.png)", TextType.TEXT),
    ]
    nodes = split_nodes_image(nodes)

    self.assertListEqual(
      nodes,
      [
        TextNode("the image", TextType.IMAGE, "https://web.co/image.png"),
      ],
    )

  def test_split_image_at_start(self):
    nodes = [
      TextNode(
        "![the image](https://web.co/image.png) heere at the wall", TextType.TEXT
      ),
    ]
    nodes = split_nodes_image(nodes)

    self.assertListEqual(
      nodes,
      [
        TextNode("the image", TextType.IMAGE, "https://web.co/image.png"),
        TextNode(" heere at the wall", TextType.TEXT),
      ],
    )

  def test_split_image_at_end(self):
    nodes = [
      TextNode(
        "heere at the wall ![the image](https://web.co/image.png)", TextType.TEXT
      ),
    ]
    nodes = split_nodes_image(nodes)

    self.assertListEqual(
      nodes,
      [
        TextNode("heere at the wall ", TextType.TEXT),
        TextNode("the image", TextType.IMAGE, "https://web.co/image.png"),
      ],
    )


class TestSplitNodesUrl(unittest.TestCase):
  pass


if __name__ == "__main__":
  unittest.main()
