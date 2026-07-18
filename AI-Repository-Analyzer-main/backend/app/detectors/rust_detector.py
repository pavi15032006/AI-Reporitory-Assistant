from app.detectors.universal_detector import (
    file_exists_anywhere
)


def detect_rust_project(repo_path: str):

    result = {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": None
    }

    if not file_exists_anywhere(repo_path, "Cargo.toml"):
        return None

    result["backend_framework"] = "Rust"

    if (
        file_exists_anywhere(repo_path, "schema.sql")
        or file_exists_anywhere(repo_path, "migrations")
    ):
        result["database"] = "SQL Database"

    result["project_type"] = "Rust Application"

    print("\n========== RUST DETECTOR ==========")
    print("Repository :", repo_path)
    print("Detection :", result)
    print("===================================\n")

    return result