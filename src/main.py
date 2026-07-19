from copy_static.copy_to_public import copy_to_public
from generate_pages.generate_pages import generate_pages


def main():
  copy_to_public()

  generate_pages(
    from_dir="content",
    template_path="template.html",
    target_dir="public",
  )


if __name__ == "__main__":
  main()
