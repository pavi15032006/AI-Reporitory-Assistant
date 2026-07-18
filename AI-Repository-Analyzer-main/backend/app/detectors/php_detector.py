from app.detectors.universal_detector import (
    file_exists_anywhere
)


def detect_php_project(repo_path: str):

    result = {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": None
    }

    if not file_exists_anywhere(repo_path, "composer.json"):
        return None

    result["backend_framework"] = "PHP"

    if file_exists_anywhere(repo_path, "artisan"):
        result["backend_framework"] = "Laravel"

    if (
        file_exists_anywhere(repo_path, ".env")
        or file_exists_anywhere(repo_path, "database.php")
    ):
        result["database"] = "SQL Database"

    if result["backend_framework"] == "Laravel":
        result["project_type"] = "Laravel Application"
    else:
        result["project_type"] = "PHP Application"

    print("\n========== PHP DETECTOR ==========")
    print("Repository :", repo_path)
    print("Detection :", result)
    print("==================================\n")

    return result