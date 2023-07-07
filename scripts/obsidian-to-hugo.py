from obsidian_to_hugo import ObsidianToHugo
from pathlib import Path
import frontmatter as fm

def included_in_hugo(file_contents: str, file_path: str) -> bool:
    # do something with the file path and contents
    if "include_in_hugo: true" in file_contents:
        return True # copy file
    else:
        return False # skip file

obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir=Path.home() / "obsidian_vaults/personal_vault",
    hugo_content_dir=Path.cwd() / "content",
    filters=[included_in_hugo],
    copy_exclusions = ["books", ".obsidian", "peace-corps", "journal", "tattoos"],
    direct_copies = [Path("02_Areas/peace-corps"), Path("03_Resources/books")]
)

obsidian_to_hugo.run()