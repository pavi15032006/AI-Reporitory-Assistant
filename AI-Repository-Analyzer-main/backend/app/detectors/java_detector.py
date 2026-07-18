from app.detectors.universal_detector import (
    file_exists_anywhere,
    folder_exists_anywhere
)

print("MY JAVA DETECTOR VERSION 3")


def detect_java_project(repo_path: str):

    result = {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": None
    }

    # ----------------------------------------
    # Skip .NET Repositories
    # ----------------------------------------

    if (
        file_exists_anywhere(repo_path, "global.json")
        or file_exists_anywhere(repo_path, "Directory.Build.props")
        or file_exists_anywhere(repo_path, "Directory.Build.targets")
    ):
        print("ASP.NET/.NET repository detected. Skipping Java detector.")
        return None

    # ----------------------------------------
    # Java source folder must exist
    # ----------------------------------------

    if not folder_exists_anywhere(repo_path, "src"):
        return None

    # ----------------------------------------
    # Build System Detection
    # ----------------------------------------

    is_gradle = (
        file_exists_anywhere(repo_path, "settings.gradle")
        or file_exists_anywhere(repo_path, "settings.gradle.kts")
        or file_exists_anywhere(repo_path, "build.gradle")
        or file_exists_anywhere(repo_path, "build.gradle.kts")
    )

    is_maven = file_exists_anywhere(repo_path, "pom.xml")

    if not (is_gradle or is_maven):
        return None

    # ----------------------------------------
    # Spring Boot Detection
    # ----------------------------------------

    if (
        file_exists_anywhere(repo_path, "application.properties")
        or file_exists_anywhere(repo_path, "application.yml")
        or file_exists_anywhere(repo_path, "application.yaml")
    ):

        result["backend_framework"] = "Spring Boot"

    else:

        result["backend_framework"] = "Java"

    # ----------------------------------------
    # Database Detection
    # ----------------------------------------

    if (
        file_exists_anywhere(repo_path, "schema.sql")
        or file_exists_anywhere(repo_path, "data.sql")
    ):

        result["database"] = "SQL Database"

    # ----------------------------------------
    # Project Type
    # ----------------------------------------

    if result["backend_framework"] == "Spring Boot":

        result["project_type"] = "Spring Boot Application"

    elif is_gradle:

        result["project_type"] = "Java Gradle Project"

    elif is_maven:

        result["project_type"] = "Java Maven Project"

    else:

        result["project_type"] = "Java Project"

    print("\n========== JAVA DETECTOR ==========")
    print("Repository :", repo_path)
    print("Gradle :", is_gradle)
    print("Maven :", is_maven)
    print("Detection :", result)
    print("==================================\n")

    return result