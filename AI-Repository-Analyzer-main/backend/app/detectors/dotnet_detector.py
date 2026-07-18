from app.detectors.universal_detector import (
    file_exists_anywhere
)


def detect_dotnet_project(repo_path: str):

    result = {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": None
    }

    if not (
        file_exists_anywhere(repo_path, ".sln")
        or file_exists_anywhere(repo_path, ".csproj")
    ):
        return None

    result["backend_framework"] = ".NET"

    if (
        file_exists_anywhere(repo_path, "appsettings.json")
        or file_exists_anywhere(repo_path, "Program.cs")
    ):
        result["backend_framework"] = "ASP.NET Core"

    if (
        file_exists_anywhere(repo_path, "appsettings.json")
        or file_exists_anywhere(repo_path, "schema.sql")
    ):
        result["database"] = "SQL Database"

    if result["backend_framework"] == "ASP.NET Core":
        result["project_type"] = "ASP.NET Core Application"
    else:
        result["project_type"] = ".NET Application"

    print("\n========== DOTNET DETECTOR ==========")
    print("Repository :", repo_path)
    print("Detection :", result)
    print("=====================================\n")

    return result