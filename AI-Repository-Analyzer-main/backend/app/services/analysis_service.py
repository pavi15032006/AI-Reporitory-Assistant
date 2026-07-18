import os

from app.services.scanner_service import scan_repository
from app.services.repository_statistics_service import get_repository_statistics
from app.services.intelligence_service import detect_project
from app.services.health_service import analyze_health
from app.services.readme_service import analyze_readme
from app.services.summary_service import generate_summary

from app.detectors.technology_detector import detect_technologies


def analyze_repository(repository_name: str):

    repo_path = os.path.join("app", "uploads", repository_name)

    # -------------------------
    # Scan Repository
    # -------------------------

    result = scan_repository(repo_path)

    # -------------------------
    # Repository Statistics
    # -------------------------

    result["statistics"] = get_repository_statistics(repo_path)

    # -------------------------
    # Project Detection
    # -------------------------

    result.update(detect_project(repo_path))

    # -------------------------
    # Technology Detection
    # -------------------------

    technologies = detect_technologies(repo_path)

    result["technologies"] = technologies

    # -------------------------
    # Health Analysis
    # -------------------------

    result.update(analyze_health(repo_path))

    # -------------------------
    # README Analysis
    # -------------------------

    result["readme_analysis"] = analyze_readme(repo_path)

    # -------------------------
    # Summary
    # -------------------------

    result["summary"] = generate_summary(result)

    return result