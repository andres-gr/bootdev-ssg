import re
from enum import Enum


class BlockType(Enum):
  CODE = "code"
  HEADING = "heading"
  ORDERED_LIST = "ordered_list"
  PARAGRAPH = "paragraph"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"


def check_ordered_list(lines: list[str]) -> bool:
  lng = len(lines)

  for i in range(lng):
    if not lines[i].startswith(f"{i + 1}. "):
      return False

  return True


def block_to_block_type(block: str) -> BlockType:
  if re.match(r"^#{1,6} ", block):
    return BlockType.HEADING

  if block.startswith("```\n") and block.endswith("```"):
    return BlockType.CODE

  if block.startswith(">"):
    return BlockType.QUOTE

  if block.startswith("- "):
    return BlockType.UNORDERED_LIST

  if block.startswith("1. "):
    lines = block.split("\n")

    if check_ordered_list(lines):
      return BlockType.ORDERED_LIST

  return BlockType.PARAGRAPH
