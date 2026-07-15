from typing import override


class HTMLNode:
  def __init__(
    self,
    tag: str | None = None,
    value: str | None = None,
    children: list["HTMLNode"] | None = None,
    props: dict[str, str] | None = None,
  ) -> None:
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self) -> str:
    raise NotImplementedError

  def propt_to_html(self) -> str:
    if self.props:
      return " ".join([f'{k}="{v}"' for k, v in self.props.items()])

    return ""

  @override
  def __repr__(self) -> str:
    return (
      f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.propt_to_html()})"
    )
