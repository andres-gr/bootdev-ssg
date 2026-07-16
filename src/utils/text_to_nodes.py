from nodes.textnode import TextNode, TextType
from utils.splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_url


def text_to_nodes(txt: str) -> list[TextNode]:
  if not txt:
    raise ValueError("No text to convert")

  if txt.strip() == "":
    return []

  node = TextNode(txt, TextType.TEXT)
  res: list[TextNode] = split_nodes_delimiter(
    old_nodes=[node],
    delimiter="`",
    text_type=TextType.CODE,
  )

  res = split_nodes_delimiter(
    old_nodes=res,
    delimiter="_",
    text_type=TextType.ITALIC,
  )

  res = split_nodes_delimiter(
    old_nodes=res,
    delimiter="**",
    text_type=TextType.BOLD,
  )

  res = split_nodes_image(
    old_nodes=res,
  )

  res = split_nodes_url(
    old_nodes=res,
  )

  return res
