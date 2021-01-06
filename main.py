"""Like tree command by Python3.9.0

Todo:
    * Allows args to be specified so that it can be executed on the command line tool.
      - Plan to use "argparse"
    * I'd like to pytest it if possible.
"""
from pathlib import Path
from typing import Final

ADJUST_SEPARATE: Final = "┃   "
ADJUST_BLANK: Final = "    "


def tree(
    root_path: str = ".",
    is_hidden: bool = False,
    is_root: bool = True,
    depth_adjust=None,
) -> None:
    """Display directories & files like tree-command.

    Display directories & files of the specified path in order by name.

    Args:
        root_path (str)  : specified path
        is_hidden (bool) : True -> display hidden files / False -> no display them
        is_root (bool)   : True -> root scanning / False -> non-root scanning
        depth_adjust     : list of strings to represent the lower dir

    Returns:
        None

    """
    p = Path(root_path)
    if not p.exists():
        print("No Such File or Directory")
        return

    # List up directories & files
    if is_hidden:
        structures = [s for s in p.iterdir()]
    else:
        structures = [s for s in p.iterdir() if not s.name.startswith(".")]

    # Empty directory
    if not structures:
        return
    structures.sort()

    # Display root path
    if is_root is True:
        print(str(p.cwd().joinpath(root_path)) + "\n┃")

    # Display all directories & files
    adjust_strings: list[str] = []
    last_item_num: int = len(structures) - 1
    for idx, structure in enumerate(structures):
        if depth_adjust is not None:
            adjust_strings = depth_adjust
            print("".join(adjust_strings), end="")

        if last_item_num != idx:
            print(f"┣━ {structure.name}")
            if structure.is_dir():
                adjust_strings.append(ADJUST_SEPARATE)
                tree(str(structure), is_hidden, False, adjust_strings)
                adjust_strings.pop()
        else:
            print(f"┗━ {structure.name}")
            if structure.is_dir():
                adjust_strings.append(ADJUST_BLANK)
                tree(str(structure), is_hidden, False, adjust_strings)
                adjust_strings.pop()


if __name__ == "__main__":
    tree(root_path=".")
    tree(root_path="./test")
    tree(root_path="./test", is_hidden=True)
