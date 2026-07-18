import json
import os


def load_json(file_path: str):
    """
    Read a JSON file safely.
    Returns a dictionary or None.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return None


def load_text(file_path: str):
    """
    Read a text file safely.
    Returns the file content as a string.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().lower()
    except Exception:
        return ""


def file_exists(repo_path: str, filename: str):
    """
    Check whether a file exists inside the repository.
    """

    return os.path.exists(
        os.path.join(repo_path, filename)
    )


def get_package_json(repo_path: str):
    """
    Return the root package.json path if it exists.
    """

    package_json = os.path.join(
        repo_path,
        "package.json"
    )

    if os.path.exists(package_json):
        return package_json

    return None

import os


def find_package_json_files(repo_path: str):

    package_files = []

    for root, dirs, files in os.walk(repo_path):

        if "node_modules" in dirs:
            dirs.remove("node_modules")

        if ".git" in dirs:
            dirs.remove(".git")

        if "package.json" in files:
            package_files.append(
                os.path.join(root, "package.json")
            )

    return package_files