import os

from app.detectors.utils import (
    load_json,
    file_exists,
    find_package_json_files
)


def detect_node_project(repo_path: str):

    result = {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": None
    }

    print("\n========== NODE DETECTOR ==========")
    print("Repository Path :", repo_path)

    # ----------------------------------
    # Skip Laravel / PHP Projects
    # ----------------------------------

    if file_exists(repo_path, "composer.json"):
        print("Laravel/PHP project detected. Skipping Node detector.")
        return None

    package_files = find_package_json_files(repo_path)

    print("Package Files Found :", len(package_files))

    if not package_files:
        print("No package.json found.")
        return None

    dependency_names = set()
    package_names = set()

    ignored_folders = {
        "test",
        "tests",
        "__tests__",
        "example",
        "examples",
        "fixture",
        "fixtures",
        "benchmark",
        "benchmarks",
        "docs",
        "documentation",
        ".github",
        "scripts"
    }

    for package_file in package_files:

        relative_path = os.path.relpath(package_file, repo_path).lower()

        if any(folder in relative_path.split(os.sep) for folder in ignored_folders):
            print("Ignoring :", relative_path)
            continue

        print("Reading :", relative_path)

        package = load_json(package_file)

        if package is None:
            continue

        package_name = package.get("name", "").lower()

        if package_name:
            package_names.add(package_name)

        dependency_names.update(
            dep.lower()
            for dep in package.get("dependencies", {}).keys()
        )

        dependency_names.update(
            dep.lower()
            for dep in package.get("devDependencies", {}).keys()
        )

    print("Package Names :", package_names)
    print("Total Dependencies :", len(dependency_names))

    # ----------------------------------
    # Frontend Detection
    # ----------------------------------

    if (
        "react" in dependency_names
        or "react" in package_names
        or os.path.exists(os.path.join(repo_path, "packages", "react"))
        or file_exists(repo_path, "vite.config.js")
        or file_exists(repo_path, "vite.config.ts")
    ):
        result["frontend_framework"] = "React"

    elif (
        "next" in dependency_names
        or "next" in package_names
        or file_exists(repo_path, "next.config.js")
    ):
        result["frontend_framework"] = "Next.js"

    elif (
        "vue" in dependency_names
        or "vue" in package_names
        or file_exists(repo_path, "vue.config.js")
    ):
        result["frontend_framework"] = "Vue.js"

    elif (
        "@angular/core" in dependency_names
        or file_exists(repo_path, "angular.json")
    ):
        result["frontend_framework"] = "Angular"

    elif (
        "svelte" in dependency_names
        or "svelte" in package_names
    ):
        result["frontend_framework"] = "Svelte"

    # ----------------------------------
    # Backend Detection
    # ----------------------------------

    backend_indicators = (
        os.path.exists(os.path.join(repo_path, "server")) or
        os.path.exists(os.path.join(repo_path, "backend")) or
        file_exists(repo_path, "server.js") or
        file_exists(repo_path, "app.js") or
        file_exists(repo_path, "index.js")
    )

    if backend_indicators and "express" in dependency_names:
        result["backend_framework"] = "Express.js"

    elif (
        backend_indicators and
        (
            "@nestjs/core" in dependency_names
            or "nestjs" in dependency_names
        )
    ):
        result["backend_framework"] = "NestJS"

    # ----------------------------------
    # Database Detection
    # ----------------------------------

    if result["backend_framework"]:

        if (
            "mongoose" in dependency_names
            or "mongodb" in dependency_names
        ):
            result["database"] = "MongoDB"

        elif "mysql2" in dependency_names:
            result["database"] = "MySQL"

        elif "pg" in dependency_names:
            result["database"] = "PostgreSQL"

        elif "sqlite3" in dependency_names:
            result["database"] = "SQLite"

    # ----------------------------------
    # Project Type
    # ----------------------------------

    if (
        result["frontend_framework"] == "React"
        and result["backend_framework"] == "Express.js"
        and result["database"] == "MongoDB"
    ):
        result["project_type"] = "MERN Stack"

    elif (
        result["frontend_framework"]
        and result["backend_framework"]
    ):
        result["project_type"] = (
            f"{result['frontend_framework']} + "
            f"{result['backend_framework']} Application"
        )

    elif result["frontend_framework"]:
        result["project_type"] = (
            f"{result['frontend_framework']} Application"
        )

    elif result["backend_framework"]:
        result["project_type"] = (
            f"{result['backend_framework']} Backend"
        )

    # ----------------------------------
    # Return Result
    # ----------------------------------

    if (
        result["frontend_framework"] is None
        and result["backend_framework"] is None
        and result["database"] is None
    ):
        print("No Node.js framework detected.")
        print("===================================\n")
        return None

    print("Detection Result :", result)
    print("===================================\n")

    return result