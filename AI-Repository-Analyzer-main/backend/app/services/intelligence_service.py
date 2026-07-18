from app.detectors.node_detector import detect_node_project
from app.detectors.python_detector import detect_python_project
from app.detectors.java_detector import detect_java_project
from app.detectors.go_detector import detect_go_project
from app.detectors.php_detector import detect_php_project
from app.detectors.rust_detector import detect_rust_project
from app.detectors.dotnet_detector import detect_dotnet_project


def detect_project(repo_path: str):

    print("\n========== PROJECT DETECTION ==========")
    print("Repository:", repo_path)

    detectors = [

        ("Node.js", detect_node_project),

        ("Python", detect_python_project),

        ("Java", detect_java_project),

        ("Go", detect_go_project),

        ("PHP", detect_php_project),

        ("Rust", detect_rust_project),

        (".NET", detect_dotnet_project)

    ]

    for detector_name, detector in detectors:

        print(f"Trying {detector_name} detector...")

        result = detector(repo_path)

        if result is not None:

            print(f"✓ {detector_name} detector matched.")
            print("=======================================\n")

            return result

    print("✗ No detector matched.")
    print("=======================================\n")

    return {
        "frontend_framework": None,
        "backend_framework": None,
        "database": None,
        "project_type": "General Software Repository"
    }