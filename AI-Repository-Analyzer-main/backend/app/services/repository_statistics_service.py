import os


def get_repository_statistics(repo_path: str):

    stats = {
        "total_files": 0,
        "total_folders": 0,

        "source_files": 0,
        "test_files": 0,
        "config_files": 0,
        "documentation_files": 0,

        "style_files": 0,
        "image_files": 0,
        "database_files": 0,
        "build_files": 0,

        "other_files": 0,
        "hidden_files": 0
    }

    source_extensions = {
        ".py", ".java", ".js", ".jsx", ".ts", ".tsx",
        ".cpp", ".c", ".cs", ".go", ".php",
        ".rb", ".swift", ".kt", ".rs"
    }

    style_extensions = {
        ".css", ".scss", ".sass", ".less"
    }

    image_extensions = {
        ".png", ".jpg", ".jpeg", ".gif",
        ".svg", ".ico", ".bmp", ".webp"
    }

    documentation_extensions = {
        ".md", ".txt", ".rst"
    }

    config_extensions = {
        ".json", ".yaml", ".yml",
        ".xml", ".ini", ".cfg",
        ".properties", ".toml"
    }

    database_extensions = {
        ".sql", ".db", ".sqlite", ".sqlite3"
    }

    build_extensions = {
        ".jar", ".war", ".class", ".dll", ".exe"
    }

    ignored_dirs = {
        ".git",
        "node_modules",
        "__pycache__",
        "dist",
        "build",
        "target",
        ".idea",
        ".vscode",
        "bin",
        "obj"
    }

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in ignored_dirs]

        stats["total_folders"] += len(dirs)

        for file in files:

            stats["total_files"] += 1

            if file.startswith("."):
                stats["hidden_files"] += 1

            extension = os.path.splitext(file)[1].lower()

            if extension in source_extensions:

                stats["source_files"] += 1

            elif extension in style_extensions:

                stats["style_files"] += 1

            elif extension in image_extensions:

                stats["image_files"] += 1

            elif extension in documentation_extensions:

                stats["documentation_files"] += 1

            elif extension in config_extensions:

                stats["config_files"] += 1

            elif extension in database_extensions:

                stats["database_files"] += 1

            elif extension in build_extensions:

                stats["build_files"] += 1

            else:

                stats["other_files"] += 1

            lower = file.lower()

            if "test" in lower or "spec" in lower:

                stats["test_files"] += 1

    return stats