import os

from generate_pages.generate_page import generate_page_from_content
from root_dir import ROOT_DIR


def generate_pages(
  from_dir: str,
  template_path: str,
  target_dir: str,
  base_path: str = "/",
) -> None:
  content_root_path = os.path.join(ROOT_DIR, from_dir)
  html_template_path = os.path.join(ROOT_DIR, template_path)
  target_root_path = os.path.join(ROOT_DIR, target_dir)

  for i in os.listdir(content_root_path):
    curr = os.path.join(content_root_path, i)
    target_path = os.path.join(target_root_path, i)

    if os.path.isfile(curr) and curr.endswith(".md"):
      generate_page_from_content(
        base_path=base_path,
        from_path=curr,
        target_path=target_path,
        template_path=html_template_path,
      )

      continue

    generate_pages(
      base_path=base_path,
      from_dir=curr,
      target_dir=target_path,
      template_path=template_path,
    )
