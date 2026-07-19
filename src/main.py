import sys

from copy_static.copy_to_public import copy_to_public
from generate_pages.generate_pages import generate_pages

args = sys.argv
base_path = args[1] if len(args) > 1 else "/"


def main():
  copy_to_public()

  generate_pages(
    base_path=base_path,
    from_dir="content",
    target_dir="docs",
    template_path="template.html",
  )


if __name__ == "__main__":
  main()
