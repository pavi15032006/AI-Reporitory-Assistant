import os
import json


def detect_monorepo(repo_path: str):

    result = {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": None
    }

    packages_path = os.path.join(repo_path, "packages")

    if not os.path.exists(packages_path):
        return result

    for package in os.listdir(packages_path):

        package_json = os.path.join(
            packages_path,
            package,
            "package.json"
        )

        if not os.path.exists(package_json):
            continue

        try:

            with open(package_json, "r", encoding="utf-8") as file:
                data = json.load(file)

            package_name = data.get("name", "").lower()

            # ------------------------------
            # React
            # ------------------------------

            if package_name == "react":
                result["frontend_framework"] = "React"
                result["project_type"] = "React Framework"

            # ------------------------------
            # React DOM
            # ------------------------------

            elif package_name == "react-dom":

                if result["frontend_framework"] is None:
                    result["frontend_framework"] = "React"

        except Exception:
            continue

    return result