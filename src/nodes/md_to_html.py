from blocks.block_to_block_type import BlockType, block_to_block_type
from blocks.md_to_blocks import md_to_blocks
from nodes.htmlnode import HTMLNode
from nodes.leafnode import LeafNode
from nodes.parentnode import ParentNode
from nodes.textnode import TextNode, TextType, text_node_to_html_node
from utils.text_to_nodes import text_to_nodes


def block_type_to_node(type: BlockType, txt: str) -> HTMLNode:
  match type:
    case BlockType.CODE:
      code_txt = txt.strip("```\n").strip("\n```")
      code_node = TextNode(code_txt, TextType.CODE)
      code_child = text_node_to_html_node(code_node)

      return ParentNode(
        tag="pre",
        children=[code_child],
      )

    case BlockType.HEADING:
      cnt = 1

      for i in range(1, 7):
        if txt[i] == " ":
          break

        cnt += 1

      return LeafNode(
        tag=f"h{cnt}",
        value=txt[cnt:].strip(),
      )

    case BlockType.ORDERED_LIST | BlockType.UNORDERED_LIST:
      tag = "ul" if type == BlockType.UNORDERED_LIST else "ol"
      lines = txt.split("\n")
      lst_childs: list[HTMLNode] = []

      for line in lines:
        line_nodes = text_to_nodes(line[2:].strip())
        lst_nodes: list[HTMLNode] = []

        for n in line_nodes:
          lst_nodes.append(text_node_to_html_node(n))

        lst_childs.append(
          ParentNode(
            tag="li",
            children=lst_nodes,
          )
        )

      return ParentNode(
        tag=tag,
        children=lst_childs,
      )

    case BlockType.QUOTE:
      quo_childs: list[HTMLNode] = []
      quo_nodes = text_to_nodes(txt[2:].strip())

      for n in quo_nodes:
        quo_childs.append(text_node_to_html_node(n))

      return ParentNode(
        tag="blockquote",
        children=quo_childs,
      )

    case BlockType.PARAGRAPH:
      p_childs: list[HTMLNode] = []
      p_nodes = text_to_nodes(txt.strip())

      for n in p_nodes:
        p_childs.append(text_node_to_html_node(n))

      return ParentNode(
        tag="p",
        children=p_childs,
      )


def md_to_html_node(md: str) -> HTMLNode:
  childs: list[HTMLNode] = []

  blocks = md_to_blocks(md)

  for b in blocks:
    type = block_to_block_type(b)
    node = block_type_to_node(type, b)

    childs.append(node)

  return ParentNode(
    tag="div",
    children=childs,
  )
