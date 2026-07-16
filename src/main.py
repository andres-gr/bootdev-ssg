from nodes.textnode import TextNode, TextType


def main():
  txt = TextNode("Heere at the wall", TextType.BOLD)

  # print(txt)

  t = "!! heere at the wall in the north !! in the south of the border !! with more text here as well"

  print("\n")
  print("text = ", t)
  print(t.split("!!", maxsplit=1))


if __name__ == "__main__":
  main()
