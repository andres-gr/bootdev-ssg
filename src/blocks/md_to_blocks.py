def md_to_blocks(md: str) -> list[str]:
  if md == "":
    return []
  
  res: list[str] = []
  lines = md.strip().split("\n\n")

  for line in lines:
    res.append(line.strip())

  return res
