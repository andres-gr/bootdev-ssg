from enum import Enum
from typing import cast, override

from .leafnode import LeafNode


class TextType(Enum):
  BOLD = "bold"
  CODE = "code"
  IMAGE = "image"
  ITALIC = "italic"
  LINK = "link"
  TEXT = "text"


class TextNode:
  def __init__(
    self,
    text: str,
    text_type: TextType,
    url: str | None = None,
  ) -> None:
    self.text = text
    self.text_type = text_type
    self.url = url

  @override
  def __eq__(self, other: object, /) -> bool:
    if not isinstance(other, TextNode):
      return NotImplemented

    return (
      self.text == other.text
      and self.text_type == other.text_type
      and self.url == other.url
    )

  @override
  def __repr__(self) -> str:
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
  if text_node.text_type not in TextType:
    raise ValueError(f"Unsupported text type: {text_node.text_type}")

  match text_node.text_type:
    case TextType.BOLD:
      return LeafNode("b", text_node.text)

    case TextType.CODE:
      return LeafNode("code", text_node.text)

    case TextType.IMAGE:
      props = {
        "src": cast(str, text_node.url),
        "alt": text_node.text,
      }

      return LeafNode("img", "", props)

    case TextType.ITALIC:
      return LeafNode("i", text_node.text)

    case TextType.LINK:
      props = {
        "href": cast(str, text_node.url),
      }

      return LeafNode("a", text_node.text, props)

    case TextType.TEXT:
      return LeafNode(None, text_node.text)
