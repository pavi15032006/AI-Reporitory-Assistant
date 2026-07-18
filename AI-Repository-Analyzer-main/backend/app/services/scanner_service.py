import os

from app.services.repository_statistics_service import get_repository_statistics


def scan_repository(repo_path: str):

    total_files = 0
    total_folders = 0

    languages = set()
    important_files = set()

    extension_map = {
        ".py": "Python",
        ".js": "JavaScript",
        ".jsx": "React",
        ".ts": "TypeScript",
        ".tsx": "React TypeScript",
        ".html": "HTML",
        ".css": "CSS",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".json": "JSON",
        ".md": "Markdown"
    }

    important_file_names = {
        "README.md",
        "package.json",
        "requirements.txt",
        ".gitignore",
        "Dockerfile",
        ".env",
        ".env.example"
    }

    ignore_folders = {
        ".git",
        "node_modules",
        "__pycache__"
    }

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in ignore_folders]

        total_folders += len(dirs)
        total_files += len(files)

        for file in files:

            extension = os.path.splitext(file)[1].lower()

            if extension in extension_map:
                languages.add(extension_map[extension])

            if file in important_file_names:
                important_files.add(file)

    # Repository Statistics
    statistics = get_repository_statistics(repo_path)

    return {
        "repository_name": os.path.basename(repo_path),
        "repository_path": repo_path,
        "total_files": total_files,
        "total_folders": total_folders,
        "languages": sorted(list(languages)),
        "important_files": sorted(list(important_files)),
        "statistics": statistics
    }
