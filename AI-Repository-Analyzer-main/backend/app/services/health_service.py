import os


def analyze_health(repo_path: str):

    score = 0

    checks = {
        "readme": False,
        "gitignore": False,
        "license": False,
        "dockerfile": False,
        "tests": False,
        "env_example": False
    }

    # Scan the repository
    for root, dirs, files in os.walk(repo_path):

        # README
        if "README.md" in files:
            checks["readme"] = True

        # .gitignore
        if ".gitignore" in files:
            checks["gitignore"] = True

        # LICENSE
        if "LICENSE" in files or "LICENSE.md" in files:
            checks["license"] = True

        # Dockerfile
        if "Dockerfile" in files:
            checks["dockerfile"] = True

        # Environment Example
        if ".env.example" in files:
            checks["env_example"] = True

        # Tests Folder
        if "tests" in dirs or "test" in dirs:
            checks["tests"] = True

    # -----------------------------
    # Calculate Health Score
    # -----------------------------

    if checks["readme"]:
        score += 20

    if checks["gitignore"]:
        score += 15

    if checks["license"]:
        score += 15

    if checks["dockerfile"]:
        score += 15

    if checks["tests"]:
        score += 20

    if checks["env_example"]:
        score += 15

    # -----------------------------
    # Health Status
    # -----------------------------

    if score >= 85:
        status = "Excellent"

    elif score >= 70:
        status = "Good"

    elif score >= 50:
        status = "Average"

    else:
        status = "Poor"

    # -----------------------------
    # Recommendations
    # -----------------------------

    recommendations = []

    if not checks["readme"]:
        recommendations.append(
            "Add a README.md file explaining the project."
        )

    if not checks["gitignore"]:
        recommendations.append(
            "Add a .gitignore file to ignore unnecessary files."
        )

    if not checks["license"]:
        recommendations.append(
            "Add a LICENSE file to define project usage permissions."
        )

    if not checks["dockerfile"]:
        recommendations.append(
            "Create a Dockerfile for easier deployment."
        )

    if not checks["tests"]:
        recommendations.append(
            "Add unit tests to improve code quality."
        )

    if not checks["env_example"]:
        recommendations.append(
            "Provide a .env.example file for easier project setup."
        )

    # -----------------------------
    # Return Result
    # -----------------------------

    return {
        "health_score": score,
        "health_status": status,
        "checks": checks,
        "recommendations": recommendations
    }