import os

from app.detectors.utils import file_exists


def read_text_file(path):

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read().lower()
    except Exception:
        return ""


def detect_python_project(repo_path: str):

    result = {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": None
    }

    print("\n========== PYTHON DETECTOR ==========")
    print("Repository :", repo_path)

    requirements = read_text_file(
        os.path.join(repo_path, "requirements.txt")
    )

    pyproject = read_text_file(
        os.path.join(repo_path, "pyproject.toml")
    )

    pipfile = read_text_file(
        os.path.join(repo_path, "Pipfile")
    )

    poetry = read_text_file(
        os.path.join(repo_path, "poetry.lock")
    )

    all_dependencies = (
        requirements
        + "\n"
        + pyproject
        + "\n"
        + pipfile
        + "\n"
        + poetry
    )

    # ---------------------------------
    # Flask
    # ---------------------------------

    if "flask" in all_dependencies:

        result["backend_framework"] = "Flask"
        result["project_type"] = "Flask Application"

    # ---------------------------------
    # FastAPI
    # ---------------------------------

    elif "fastapi" in all_dependencies:

        result["backend_framework"] = "FastAPI"
        result["project_type"] = "FastAPI Application"

    # ---------------------------------
    # Django
    # ---------------------------------

    elif "django" in all_dependencies:

        result["backend_framework"] = "Django"
        result["project_type"] = "Django Application"

    # ---------------------------------
    # Streamlit
    # ---------------------------------

    elif "streamlit" in all_dependencies:

        result["frontend_framework"] = "Streamlit"
        result["project_type"] = "Streamlit Application"

    # ---------------------------------
    # Gradio
    # ---------------------------------

    elif "gradio" in all_dependencies:

        result["frontend_framework"] = "Gradio"
        result["project_type"] = "Gradio Application"

    # ---------------------------------
    # Databases
    # ---------------------------------

    if "pymongo" in all_dependencies:

        result["database"] = "MongoDB"

    elif "psycopg2" in all_dependencies:

        result["database"] = "PostgreSQL"

    elif "mysqlclient" in all_dependencies:

        result["database"] = "MySQL"

    elif "sqlite3" in all_dependencies:

        result["database"] = "SQLite"

    # ---------------------------------
    # Extra Detection
    # ---------------------------------

    if (
        result["backend_framework"] is None
        and file_exists(repo_path, "manage.py")
    ):

        result["backend_framework"] = "Django"
        result["project_type"] = "Django Application"

    print("Detection :", result)
    print("===============================\n")

    if (
        result["frontend_framework"] is None
        and result["backend_framework"] is None
    ):
        return None

    return result