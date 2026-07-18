from git import Repo
import os


def clone_repository(github_url: str):

    # Folder where repositories will be stored
    uploads_folder = "app/uploads"

    # Extract repository name from URL
    # Example:
    # https://github.com/facebook/react
    # repo_name = react
    repo_name = github_url.split("/")[-1]

    # Full path where repository will be cloned
    clone_path = os.path.join(uploads_folder, repo_name)

    # Check if repository already exists
    if os.path.exists(clone_path):
        return {
            "status": "already_exists",
            "path": clone_path
        }

    try:
        # Clone only the latest version (faster)
        Repo.clone_from(
            github_url,
            clone_path,
            depth=1
        )

        return {
            "status": "success",
            "path": clone_path
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }