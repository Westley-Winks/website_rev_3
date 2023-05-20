import frontmatter
from pathlib import Path

book_folder = Path.home() /"obsidian_vaults/personal_vault/03_Resources/books"
content_folder = Path(".").parent / "content" / "books"

def convert_to_hugo(post):
    post['slug'] = post['title'].lower().replace(" ", "-")
    post['toc'] = False

    post = parse_summary(post)

    with open(content_folder.joinpath(post['title'] + ".md"), "w") as f:
        f.write(frontmatter.dumps(post))

def parse_summary(post):
    summary = ""
    h2_blocks = []
    block = ""
    idx = 0

    for line in post.content.splitlines():
        if line.startswith("## Highlights"):
            h2_blocks.append(block)
            break
        elif line.startswith("##") and idx == 0:
            block = line + "\n"
            idx += 1
        elif line.startswith("##"):
            h2_blocks.append(block)
            block = line + "\n"
            idx += 1
        else:
            block += line
            block += "\n"

    print(f"Total H2 Blocks: {idx}")
    summary = "".join(h2_blocks)
    post.content = summary
    return post

for file in book_folder.iterdir():
    with open(file) as f:
        post = frontmatter.load(f)
        if post.get("include_in_hugo"):
            convert_to_hugo(post)
