import unittest

from utils.extract_md_links import extract_md_images, extract_md_urls


class TextExtractFromMdLinks(unittest.TestCase):
  def test_empty(self):
    txt = ""

    self.assertEqual(extract_md_images(txt), [])
    self.assertEqual(extract_md_urls(txt), [])

  def test_no_urls_or_images(self):
    txt = "this is just an md text"

    self.assertEqual(extract_md_images(txt), [])
    self.assertEqual(extract_md_urls(txt), [])

  def test_extract_only_images(self):
    txt = "this an md image test with ![image](https://example.com/image.png)"

    self.assertEqual(
      extract_md_images(txt),
      [("image", "https://example.com/image.png")],
    )

  def test_extract_only_urls(self):
    txt = "this an md url test with [our url](https://example.com/wiki.html)"

    self.assertEqual(
      extract_md_urls(txt),
      [("our url", "https://example.com/wiki.html")],
    )


if __name__ == "__main__":
  unittest.main()
