import re


def extract_md_images(txt: str) -> list[tuple[str, str]]:
  return re.findall(r"!\[(.*?)\]\((.*?)\)", txt)


def extract_md_urls(txt: str) -> list[tuple[str, str]]:
  return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", txt)
