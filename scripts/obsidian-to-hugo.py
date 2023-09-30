from obsidian_to_hugo import ObsidianToHugo
from pathlib import Path
import frontmatter


def included_in_hugo(file_contents: str, file_path: str) -> bool:
    # do something with the file path and contents
    try:
        metadata, _ = frontmatter.parse(file_contents)
    except:
        metadata = {}
    if "hugo" in metadata.keys():
        return True  # copy file
    else:
        return False  # skip file


obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir=Path.home() / "jd_wiki",
    hugo_content_dir=Path.cwd() / "content",
    filters=[included_in_hugo],
    copy_exclusions=["books", ".obsidian",
                     "peace-corps", "journal", "tattoos"],
)

obsidian_to_hugo.run()
