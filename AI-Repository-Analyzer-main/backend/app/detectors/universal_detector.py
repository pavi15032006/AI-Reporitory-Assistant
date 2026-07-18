import os


def scan_repository(repo_path: str):
    """
    Returns a list of every file in the repository.
    """

    all_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            all_files.append(
                os.path.join(root, file)
            )

    return all_files


def file_exists_anywhere(repo_path: str, filename: str):
    """
    Returns True if the given file exists anywhere
    inside the repository.

    Supports:
    - Exact filenames (package.json)
    - Extension search (.csproj, .sln)
    """

    for root, dirs, files in os.walk(repo_path):

        # Extension search
        if filename.startswith("."):

            for file in files:

                if file.lower().endswith(filename.lower()):
                    return True

        # Exact filename search
        else:

            if filename in files:
                return True

    return False


def folder_exists_anywhere(repo_path: str, folder_name: str):
    """
    Returns True if the folder exists anywhere
    inside the repository.
    """

    for root, dirs, files in os.walk(repo_path):

        if folder_name in dirs:
            return True

    return False


def find_all_files(repo_path: str, filename: str):
    """
    Returns every matching file path.
    """

    matches = []

    for root, dirs, files in os.walk(repo_path):

        if filename.startswith("."):

            for file in files:

                if file.lower().endswith(filename.lower()):

                    matches.append(
                        os.path.join(root, file)
                    )

        else:

            if filename in files:

                matches.append(
                    os.path.join(root, filename)
                )

    return matches


def detect_languages(repo_path: str):
    """
    Counts programming language file extensions.
    """

    extensions = {}

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            extension = os.path.splitext(file)[1].lower()

            if extension:

                extensions[extension] = (
                    extensions.get(extension, 0) + 1
                )

    return extensions


def detect_special_files(repo_path: str):
    """
    Detects important project files.
    """

    important_files = [

        "package.json",
        "package-lock.json",
        "yarn.lock",
        "pnpm-lock.yaml",
        "requirements.txt",
        "pyproject.toml",
        "Pipfile",
        "manage.py",
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        "Cargo.toml",
        "go.mod",
        "composer.json",
        "pom.xml",
        "build.gradle",
        "build.gradle.kts",
        ".gitignore",
        "README.md",
        "README.MD",
        "LICENSE",
        ".env.example",
        "vite.config.js",
        "vite.config.ts",
        "next.config.js",
        "angular.json",
        "tsconfig.json",
        ".github"

    ]

    found = []

    for item in important_files:

        if file_exists_anywhere(repo_path, item):

            found.append(item)

    return found


def find_package_json_files(repo_path: str):
    """
    Returns every package.json inside the repository.
    Useful for monorepos like React, NestJS, Nx, Turborepo.
    """

    package_files = []

    for root, dirs, files in os.walk(repo_path):

        if "package.json" in files:

            package_files.append(
                os.path.join(root, "package.json")
            )

    return package_files


def repository_summary(repo_path: str):
    """
    Returns a quick summary of the repository.
    """

    return {

        "total_files": len(scan_repository(repo_path)),

        "languages": detect_languages(repo_path),

        "special_files": detect_special_files(repo_path),

        "package_json_files": len(
            find_package_json_files(repo_path)
        )

    }