import unittest

from blocks.block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
  def test_heading(self):
    self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

  def test_code(self):
    self.assertEqual(block_to_block_type("```\nCode\n```"), BlockType.CODE)

  def test_quote(self):
    self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)

  def test_unordered_list(self):
    self.assertEqual(block_to_block_type("- Unordered List"), BlockType.UNORDERED_LIST)

  def test_ordered_list(self):
    self.assertEqual(
      block_to_block_type("1. Ordered Item List\n2. Another Item\n3. Yet Another Item"),
      BlockType.ORDERED_LIST,
    )

  def test_not_ordered_list(self):
    self.assertNotEqual(
      block_to_block_type("1. Ordered Item List\n5. Broken Item\n3. Yet Another Item"),
      BlockType.ORDERED_LIST,
    )

  def test_paragraph(self):
    self.assertEqual(block_to_block_type("Paragraph"), BlockType.PARAGRAPH)


if __name__ == "__main__":
  unittest.main()
