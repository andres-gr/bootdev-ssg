import os
import shutil

from root_dir import ROOT_DIR

PUBLIC_DIR = "docs"
STATIC_DIR = "static"


def clean_path(path: str):
  if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)

    return

  shutil.rmtree(path)
  os.makedirs(path, exist_ok=True)


def copy_path_contents(path: str, target_path: str):
  if not os.path.exists(target_path):
    os.makedirs(target_path, exist_ok=True)

  for i in os.listdir(path):
    sub_path = os.path.join(path, i)

    if os.path.isdir(sub_path):
      new_target = os.path.join(target_path, i)
      copy_path_contents(sub_path, new_target)

      continue

    shutil.copy(sub_path, target_path)


def copy_to_public():
  public_path = os.path.join(ROOT_DIR, PUBLIC_DIR)
  clean_path(public_path)

  static_path = os.path.join(ROOT_DIR, STATIC_DIR)
  copy_path_contents(static_path, public_path)
