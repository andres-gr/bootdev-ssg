import unittest

from generate_pages.extract_title import extract_title_from_md


class TestExtractTitleFromMd(unittest.TestCase):
  def test_none(self):
    self.assertRaises(ValueError, extract_title_from_md, "")

  def test_no_title(self):
    self.assertRaises(Exception, extract_title_from_md, "this is some text")

  def test_found_title(self):
    md = """
# Head 1

## Head #2

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item

### Head Num. 3

```
this is some code block heere at the wall
```

> This is a quote, or a greentext

1. Ordered Item List
2. Another Item
3. Yet Another Item
"""
    title = extract_title_from_md(md)

    self.assertEqual(title, "Head 1")


if __name__ == "__main__":
  unittest.main()
