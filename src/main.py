from copy_static.copy_to_public import copy_to_public
from generate_pages.generate_page import generate_page_from_content


def main():
  copy_to_public()

  generate_page_from_content(
    from_path="content/index.md",
    template_path="template.html",
    target_path="public/index.html",
  )


if __name__ == "__main__":
  main()
