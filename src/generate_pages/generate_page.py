import os

from generate_pages.extract_title import extract_title_from_md
from nodes.md_to_html import md_to_html_node
from root_dir import ROOT_DIR


def generate_page_from_content(
  from_path: str,
  template_path: str,
  target_path: str,
) -> None:
  print("-" * 20)
  print(f"Generating page from {from_path} to {target_path} using {template_path}...")
  print("-" * 20)

  content_path = os.path.join(ROOT_DIR, from_path)
  html_temp_path = os.path.join(ROOT_DIR, template_path)
  dist_path = os.path.join(ROOT_DIR, target_path)
  content = template = ""

  with open(content_path) as md_file:
    content = md_file.read()

  with open(html_temp_path) as temp_file:
    template = temp_file.read()

  title = extract_title_from_md(content)
  html_str = md_to_html_node(content).to_html()
  html_content = template.replace(
    "{{ Title }}",
    title,
  ).replace(
    "{{ Content }}",
    html_str,
  )

  with open(dist_path, "w") as html_file:
    html_file.write(html_content)
