from typing import override

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
  def __init__(
    self,
    tag: str | None,
    value: str,
    props: dict[str, str] | None = None,
  ) -> None:
    super().__init__(tag, value, None, props)

  @override
  def to_html(self) -> str:
    if self.value is None:
      raise ValueError("All leaf nodes must have a value")

    if not self.tag:
      return self.value

    p = super().props_to_html()
    props = f" {p}" if p else ""

    return f"<{self.tag}{props}>{self.value}</{self.tag}>"

  @override
  def __repr__(self) -> str:
    return f"LeafNode({self.tag}, {self.value}, {super().props_to_html()})"
