import re


def extract_title_from_md(md: str) -> str:
  if not md:
    raise ValueError("md is empty")

  match: list[str] = re.findall(r"(?<!#)#{1}\s(.*)", md)

  if len(match) > 0:
    return match[0]

  raise Exception("no title found")
