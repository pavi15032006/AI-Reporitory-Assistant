import os
import re

from app.detectors.utils import (
    load_json,
    find_package_json_files
)

from app.detectors.universal_detector import (
    file_exists_anywhere
)
# ==========================================================
# TECHNOLOGY DATABASE
# ==========================================================

TECHNOLOGY_DATABASE = {

    # --------------------------------------------------
    # Frontend Frameworks
    # --------------------------------------------------

    "react": ("Frontend", "React"),
    "next": ("Frontend", "Next.js"),
    "nextjs": ("Frontend", "Next.js"),
    "vue": ("Frontend", "Vue.js"),
    "nuxt": ("Frontend", "Nuxt.js"),
    "angular": ("Frontend", "Angular"),
    "@angular/core": ("Frontend", "Angular"),
    "svelte": ("Frontend", "Svelte"),
    "solid-js": ("Frontend", "SolidJS"),
    "solid": ("Frontend", "SolidJS"),
    "astro": ("Frontend", "Astro"),
    "gatsby": ("Frontend", "Gatsby"),
    "vite": ("Frontend", "Vite"),
    "webpack": ("Frontend", "Webpack"),
    "parcel": ("Frontend", "Parcel"),
    "ember": ("Frontend", "Ember.js"),
    "backbone": ("Frontend", "Backbone.js"),
    "jquery": ("Frontend", "jQuery"),
    "bootstrap": ("Frontend", "Bootstrap"),
    "tailwindcss": ("Frontend", "Tailwind CSS"),
    "bulma": ("Frontend", "Bulma"),
    "material-ui": ("Frontend", "Material UI"),
    "@mui/material": ("Frontend", "Material UI"),
    "chakra-ui": ("Frontend", "Chakra UI"),
    "@chakra-ui/react": ("Frontend", "Chakra UI"),
    "antd": ("Frontend", "Ant Design"),

    # --------------------------------------------------
    # Backend
    # --------------------------------------------------

    "express": ("Backend", "Express.js"),
    "koa": ("Backend", "Koa"),
    "hapi": ("Backend", "Hapi"),
    "fastify": ("Backend", "Fastify"),
    "nestjs": ("Backend", "NestJS"),
    "@nestjs/core": ("Backend", "NestJS"),
    "fastapi": ("Backend", "FastAPI"),
    "flask": ("Backend", "Flask"),
    "django": ("Backend", "Django"),
    "tornado": ("Backend", "Tornado"),
    "aiohttp": ("Backend", "AioHTTP"),
    "spring-boot": ("Backend", "Spring Boot"),
    "laravel": ("Backend", "Laravel"),
    "symfony": ("Backend", "Symfony"),
    "rails": ("Backend", "Ruby on Rails"),
    "sinatra": ("Backend", "Sinatra"),
    "aspnetcore": ("Backend", "ASP.NET Core"),

    # --------------------------------------------------
    # Databases
    # --------------------------------------------------

    "mongodb": ("Database", "MongoDB"),
    "mongoose": ("Database", "MongoDB"),
    "mysql": ("Database", "MySQL"),
    "mysql2": ("Database", "MySQL"),
    "postgres": ("Database", "PostgreSQL"),
    "postgresql": ("Database", "PostgreSQL"),
    "pg": ("Database", "PostgreSQL"),
    "sqlite": ("Database", "SQLite"),
    "sqlite3": ("Database", "SQLite"),
    "redis": ("Database", "Redis"),
    "cassandra": ("Database", "Cassandra"),
    "firebase": ("Database", "Firebase"),
    "firestore": ("Database", "Firestore"),
    "realm": ("Database", "Realm"),

    # --------------------------------------------------
    # AI / Machine Learning
    # --------------------------------------------------

    "tensorflow": ("AI", "TensorFlow"),
    "torch": ("AI", "PyTorch"),
    "pytorch": ("AI", "PyTorch"),
    "keras": ("AI", "Keras"),
    "opencv-python": ("AI", "OpenCV"),
    "opencv": ("AI", "OpenCV"),
    "ultralytics": ("AI", "YOLO"),
    "scikit-learn": ("AI", "Scikit-Learn"),
    "sklearn": ("AI", "Scikit-Learn"),
    "xgboost": ("AI", "XGBoost"),
    "lightgbm": ("AI", "LightGBM"),
    "catboost": ("AI", "CatBoost"),
    "pandas": ("AI", "Pandas"),
    "numpy": ("AI", "NumPy"),
    "scipy": ("AI", "SciPy"),
    "transformers": ("AI", "Transformers"),
    "langchain": ("AI", "LangChain"),
    "llama-index": ("AI", "LlamaIndex"),

    # --------------------------------------------------
    # Cloud
    # --------------------------------------------------

    "aws-sdk": ("Cloud", "AWS"),
    "@aws-sdk/client-s3": ("Cloud", "AWS"),
    "firebase-admin": ("Cloud", "Firebase"),
    "firebase": ("Cloud", "Firebase"),
    "supabase": ("Cloud", "Supabase"),
    "@supabase/supabase-js": ("Cloud", "Supabase"),
    "azure": ("Cloud", "Azure"),
    "google-cloud-storage": ("Cloud", "Google Cloud"),
    "google-cloud": ("Cloud", "Google Cloud"),

    # --------------------------------------------------
    # DevOps
    # --------------------------------------------------

    "docker": ("DevOps", "Docker"),
    "docker-compose": ("DevOps", "Docker Compose"),
    "kubernetes": ("DevOps", "Kubernetes"),
    "terraform": ("DevOps", "Terraform"),
    "ansible": ("DevOps", "Ansible"),
    "jenkins": ("DevOps", "Jenkins"),
    "github-actions": ("DevOps", "GitHub Actions"),

    # --------------------------------------------------
    # Mobile
    # --------------------------------------------------

    "react-native": ("Mobile", "React Native"),
    "flutter": ("Mobile", "Flutter"),
    "ionic": ("Mobile", "Ionic"),
    "xamarin": ("Mobile", "Xamarin"),

    # --------------------------------------------------
    # Testing
    # --------------------------------------------------

    "jest": ("Testing", "Jest"),
    "mocha": ("Testing", "Mocha"),
    "chai": ("Testing", "Chai"),
    "pytest": ("Testing", "PyTest"),
    "junit": ("Testing", "JUnit"),
    "cypress": ("Testing", "Cypress"),
    "playwright": ("Testing", "Playwright"),
    "selenium": ("Testing", "Selenium"),

    # --------------------------------------------------
    # Build Tools
    # --------------------------------------------------

    "gradle": ("Build Tool", "Gradle"),
    "maven": ("Build Tool", "Maven"),
    "rollup": ("Build Tool", "Rollup"),
    "gulp": ("Build Tool", "Gulp"),
    "grunt": ("Build Tool", "Grunt")
}


# ==========================================================
# DEFAULT RESULT
# ==========================================================

def create_result():

    return {
        "Frontend": [],
        "Backend": [],
        "Database": [],
        "AI": [],
        "Cloud": [],
        "DevOps": [],
        "Mobile": [],
        "Testing": [],
        "Build Tool": []
    }

# ==========================================================
# PACKAGE.JSON DETECTION
# ==========================================================

def detect_from_package_json(repo_path, result):

    package_files = find_package_json_files(repo_path)

    for package_file in package_files:

        package = load_json(package_file)

        if package is None:
            continue

        dependencies = {}

        dependencies.update(package.get("dependencies", {}))
        dependencies.update(package.get("devDependencies", {}))

        for dependency in dependencies.keys():

            dependency = dependency.lower()

            if dependency in TECHNOLOGY_DATABASE:

                category, technology = TECHNOLOGY_DATABASE[dependency]

                if technology not in result[category]:
                    result[category].append(technology)


# ==========================================================
# REQUIREMENTS.TXT DETECTION
# ==========================================================

def detect_from_requirements(repo_path, result):

    for root, _, files in os.walk(repo_path):

        if "requirements.txt" not in files:
            continue

        file_path = os.path.join(root, "requirements.txt")

        try:

            with open(file_path, "r", encoding="utf-8") as file:

                for line in file:

                    line = line.strip().lower()

                    if not line:
                        continue

                    package = re.split(r"[<>=]", line)[0]

                    if package in TECHNOLOGY_DATABASE:

                        category, technology = TECHNOLOGY_DATABASE[package]

                        if technology not in result[category]:
                            result[category].append(technology)

        except:
            pass


# ==========================================================
# PYPROJECT.TOML DETECTION
# ==========================================================

def detect_from_pyproject(repo_path, result):

    for root, _, files in os.walk(repo_path):

        if "pyproject.toml" not in files:
            continue

        file_path = os.path.join(root, "pyproject.toml")

        try:

            text = open(
                file_path,
                encoding="utf-8"
            ).read().lower()

            for dependency in TECHNOLOGY_DATABASE:

                if dependency in text:

                    category, technology = TECHNOLOGY_DATABASE[dependency]

                    if technology not in result[category]:
                        result[category].append(technology)

        except:
            pass


# ==========================================================
# GO MODULE DETECTION
# ==========================================================

def detect_from_go_mod(repo_path, result):

    for root, _, files in os.walk(repo_path):

        if "go.mod" not in files:
            continue

        file_path = os.path.join(root, "go.mod")

        try:

            text = open(
                file_path,
                encoding="utf-8"
            ).read().lower()

            for dependency in TECHNOLOGY_DATABASE:

                if dependency in text:

                    category, technology = TECHNOLOGY_DATABASE[dependency]

                    if technology not in result[category]:
                        result[category].append(technology)

        except:
            pass


# ==========================================================
# CARGO.TOML DETECTION
# ==========================================================

def detect_from_cargo(repo_path, result):

    for root, _, files in os.walk(repo_path):

        if "cargo.toml" not in files:
            continue

        file_path = os.path.join(root, "Cargo.toml")

        try:

            text = open(
                file_path,
                encoding="utf-8"
            ).read().lower()

            for dependency in TECHNOLOGY_DATABASE:

                if dependency in text:

                    category, technology = TECHNOLOGY_DATABASE[dependency]

                    if technology not in result[category]:
                        result[category].append(technology)

        except:
            pass


# ==========================================================
# COMPOSER DETECTION
# ==========================================================

def detect_from_composer(repo_path, result):

    for root, _, files in os.walk(repo_path):

        if "composer.json" not in files:
            continue

        file_path = os.path.join(root, "composer.json")

        try:

            text = open(
                file_path,
                encoding="utf-8"
            ).read().lower()

            for dependency in TECHNOLOGY_DATABASE:

                if dependency in text:

                    category, technology = TECHNOLOGY_DATABASE[dependency]

                    if technology not in result[category]:
                        result[category].append(technology)

        except:
            pass


# ==========================================================
# GEMFILE DETECTION
# ==========================================================

def detect_from_gemfile(repo_path, result):

    for root, _, files in os.walk(repo_path):

        if "Gemfile" not in files:
            continue

        file_path = os.path.join(root, "Gemfile")

        try:

            text = open(
                file_path,
                encoding="utf-8"
            ).read().lower()

            for dependency in TECHNOLOGY_DATABASE:

                if dependency in text:

                    category, technology = TECHNOLOGY_DATABASE[dependency]

                    if technology not in result[category]:
                        result[category].append(technology)

        except:
            pass


# ==========================================================
# PUBSPEC DETECTION
# ==========================================================

def detect_from_pubspec(repo_path, result):

    for root, _, files in os.walk(repo_path):

        if "pubspec.yaml" not in files:
            continue

        file_path = os.path.join(root, "pubspec.yaml")

        try:

            text = open(
                file_path,
                encoding="utf-8"
            ).read().lower()

            for dependency in TECHNOLOGY_DATABASE:

                if dependency in text:

                    category, technology = TECHNOLOGY_DATABASE[dependency]

                    if technology not in result[category]:
                        result[category].append(technology)

        except:
            pass

# ==========================================================
# FILE BASED DETECTION
# ==========================================================

def detect_from_files(repo_path, result):

    # ---------------- Docker ----------------

    if file_exists_anywhere(repo_path, "Dockerfile"):

        if "Docker" not in result["DevOps"]:
            result["DevOps"].append("Docker")

    # ---------------- Kubernetes ----------------

    if (
        file_exists_anywhere(repo_path, "deployment.yaml")
        or file_exists_anywhere(repo_path, "deployment.yml")
        or file_exists_anywhere(repo_path, "service.yaml")
        or file_exists_anywhere(repo_path, "service.yml")
    ):

        if "Kubernetes" not in result["DevOps"]:
            result["DevOps"].append("Kubernetes")

    # ---------------- GitHub Actions ----------------

    github_workflows = os.path.join(
        repo_path,
        ".github",
        "workflows"
    )

    if os.path.exists(github_workflows):

        if "GitHub Actions" not in result["DevOps"]:
            result["DevOps"].append("GitHub Actions")

    # ---------------- Spring Boot ----------------

    if (
        file_exists_anywhere(repo_path, "application.properties")
        or file_exists_anywhere(repo_path, "application.yml")
        or file_exists_anywhere(repo_path, "application.yaml")
    ):

        if "Spring Boot" not in result["Backend"]:
            result["Backend"].append("Spring Boot")

    # ---------------- Maven ----------------

    if file_exists_anywhere(repo_path, "pom.xml"):

        if "Maven" not in result["Build Tool"]:
            result["Build Tool"].append("Maven")

    # ---------------- Gradle ----------------

    if (
        file_exists_anywhere(repo_path, "build.gradle")
        or file_exists_anywhere(repo_path, "build.gradle.kts")
    ):

        if "Gradle" not in result["Build Tool"]:
            result["Build Tool"].append("Gradle")

    # ---------------- Flutter ----------------

    if file_exists_anywhere(repo_path, "pubspec.yaml"):

        if "Flutter" not in result["Mobile"]:
            result["Mobile"].append("Flutter")

    # ---------------- ASP.NET ----------------

    for root, _, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".csproj"):

                if "ASP.NET Core" not in result["Backend"]:
                    result["Backend"].append("ASP.NET Core")

                break


# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

def remove_duplicates(result):

    for category in result:

        result[category] = sorted(
            list(set(result[category]))
        )

    return result


# ==========================================================
# MAIN FUNCTION
# ==========================================================

def detect_technologies(repo_path):

    result = create_result()

    detect_from_package_json(repo_path, result)

    detect_from_requirements(repo_path, result)

    detect_from_pyproject(repo_path, result)

    detect_from_go_mod(repo_path, result)

    detect_from_cargo(repo_path, result)

    detect_from_composer(repo_path, result)

    detect_from_gemfile(repo_path, result)

    detect_from_pubspec(repo_path, result)

    detect_from_files(repo_path, result)

    result = remove_duplicates(result)

    print("\n========== TECHNOLOGY DETECTOR ==========")

    for category, technologies in result.items():

        if technologies:

            print(category, ":", technologies)

    print("=========================================\n")


    return result