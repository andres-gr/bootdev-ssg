import unittest

from blocks.md_to_blocks import md_to_blocks


class TestMdToBlocks(unittest.TestCase):
  def test_empty_md(self):
    res = md_to_blocks("")

    self.assertEqual(res, [])

  def test_md_blocks(self):
    md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

    res = md_to_blocks(md)

    self.assertListEqual(
      res,
      [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
        "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
      ],
    )


if __name__ == "__main__":
  unittest.main()
