from nodes.textnode import TextNode, TextType
from utils.extract_md_links import extract_md_images, extract_md_urls


def split_nodes_delimiter(
  old_nodes: list[TextNode],
  delimiter: str | None,
  text_type: TextType,
) -> list[TextNode]:
  if len(old_nodes) == 0 or not old_nodes:
    raise ValueError("No nodes to split")

  res: list[TextNode] = []

  for node in old_nodes:
    if node.text_type != TextType.TEXT or delimiter == "" or delimiter is None:
      res.append(node)
      continue

    text = node.text.split(delimiter)
    nodes: list[TextNode] = []

    if len(text) % 2 == 0:
      raise Exception("Unbalanced delimiters")

    for i in range(len(text)):
      if text[i] == "":
        continue

      if i % 2 != 0:
        nodes.append(TextNode(text[i], text_type))
      else:
        nodes.append(TextNode(text[i], TextType.TEXT))

    res.extend(nodes)

  return res


def split_nodes_links(
  links: list[tuple[str, str]],
  text: str,
  type: TextType,
) -> list[TextNode]:
  if type not in [TextType.IMAGE, TextType.LINK, TextType.TEXT]:
    raise ValueError(f"Unsupported type: {type}")

  res: list[TextNode] = []

  txt = text
  link_type = TextType.IMAGE if type == TextType.IMAGE else TextType.LINK
  split_type = "!" if type == TextType.IMAGE else ""

  for i in range(len(links)):
    lst = txt.split(f"{split_type}[{links[i][0]}]({links[i][1]})", maxsplit=1)
    lng = len(lst)

    if lng == 1:
      if lst[0] != "":
        res.append(TextNode(lst[0], TextType.TEXT))
      else:
        res.append(TextNode(links[i][0], link_type, links[i][1]))

      continue

    if lng == 2:
      if lst[0] != "":
        res.append(TextNode(lst[0], TextType.TEXT))

      res.append(TextNode(links[i][0], link_type, links[i][1]))

    if i == len(links) - 1:
      if lst[1] != "":
        res.append(TextNode(lst[1], TextType.TEXT))

    txt = lst[1]

  return res


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
  if len(old_nodes) == 0 or not old_nodes:
    raise ValueError("No nodes to split")

  nodes: list[TextNode] = []

  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      nodes.append(node)
      continue

    imgs = extract_md_images(node.text)

    if len(imgs) == 0:
      nodes.append(node)
      continue

    res = split_nodes_links(imgs, node.text, TextType.IMAGE)
    nodes.extend(res)

  return nodes


def split_nodes_url(old_nodes: list[TextNode]) -> list[TextNode]:
  if len(old_nodes) == 0 or not old_nodes:
    raise ValueError("No nodes to split")

  nodes: list[TextNode] = []

  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      nodes.append(node)
      continue

    imgs = extract_md_urls(node.text)

    if len(imgs) == 0:
      nodes.append(node)
      continue

    res = split_nodes_links(imgs, node.text, TextType.LINK)
    nodes.extend(res)

  return nodes
