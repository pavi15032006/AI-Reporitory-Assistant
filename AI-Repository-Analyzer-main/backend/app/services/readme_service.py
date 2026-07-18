import os


def analyze_readme(repo_path: str):

    readme_path = None

    # Search for README.md anywhere in the repository
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.lower() == "readme.md":
                readme_path = os.path.join(root, file)
                break

        if readme_path:
            break

    if readme_path is None:
        return {
            "exists": False,
            "message": "README.md not found."
        }

    with open(readme_path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()

    lines = content.splitlines()

    title = ""

    for line in lines:
        if line.strip().startswith("#"):
            title = line.replace("#", "").strip()
            break

    description = ""

    for line in lines:
        line = line.strip()

        if line and not line.startswith("#"):
            description = line
            break

    word_count = len(content.split())

    lower_content = content.lower()

    return {
        "exists": True,
        "readme_path": readme_path,
        "title": title,
        "description": description,
        "word_count": word_count,
        "has_installation": "installation" in lower_content,
        "has_usage": "usage" in lower_content,
        "has_features": "features" in lower_content
    }