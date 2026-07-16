from typing import override

from .htmlnode import HTMLNode


class ParentNode(HTMLNode):
  def __init__(
    self,
    tag: str,
    children: list["HTMLNode"],
    props: dict[str, str] | None = None,
  ) -> None:
    super().__init__(tag, None, children, props)

  @override
  def to_html(self) -> str:
    if not self.tag:
      raise ValueError("All parent nodes must have a tag")

    if not self.children or len(self.children) == 0:
      raise ValueError("All parent nodes must have children")

    p = super().props_to_html()
    props = f" {p}" if p else ""
    res = f"<{self.tag}{props}>"

    for child in self.children:
      res += child.to_html()

    res += f"</{self.tag}>"
    return res
