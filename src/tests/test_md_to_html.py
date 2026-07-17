import unittest

from nodes.md_to_html import md_to_html_node


def wrap_html(str: str) -> str:
  return f"<div>{str}</div>"


class TestMdToHTML(unittest.TestCase):
  def test_p(self):
    md = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
    res = md_to_html_node(md).to_html()

    self.assertEqual(
      res,
      wrap_html(
        "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
      ),
    )

  def test_head(self):
    md = """
# This is a heading

## Head #2

### Head Num. 3
"""
    res = md_to_html_node(md).to_html()

    self.maxDiff = None
    self.assertEqual(
      res,
      wrap_html(
        "<h1>This is a heading</h1><h2>Head #2</h2><h3>Head Num. 3</h3>",
      ),
    )

  def test_code(self):
    md = """
```
this is some code block heere at the wall, with custom **text** that should stay the _same_ for every line.
```
"""
    res = md_to_html_node(md).to_html()

    self.maxDiff = None
    self.assertEqual(
      res,
      wrap_html(
        "<pre><code>this is some code block heere at the wall, with custom **text** that should stay the _same_ for every line.</code></pre>",
      ),
    )

  def test_md_to_html(self):
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

    res = md_to_html_node(md).to_html()

    self.maxDiff = None
    self.assertEqual(
      res,
      wrap_html(
        "<h1>Head 1</h1><h2>Head #2</h2><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h3>Head Num. 3</h3><pre><code>this is some code block heere at the wall</code></pre><blockquote>This is a quote, or a greentext</blockquote><ol><li>Ordered Item List</li><li>Another Item</li><li>Yet Another Item</li></ol>"
      ),
    )


if __name__ == "__main__":
  unittest.main()
