def generate_summary(repository):

    repository_name = repository.get("repository_name", "Unknown Repository")

    project_type = repository.get("project_type", "General Software Repository")

    frontend = repository.get("frontend_framework")

    backend = repository.get("backend_framework")

    database = repository.get("database")

    total_files = repository.get("total_files", 0)

    total_folders = repository.get("total_folders", 0)

    languages = repository.get("languages", [])

    summary = []

    # Repository introduction
    summary.append(
        f"**{repository_name}** is a **{project_type}** containing **{total_files} files** and **{total_folders} folders**."
    )

    # Technologies
    tech = []

    if frontend:
        tech.append(f"uses **{frontend}** for the frontend")

    if backend:
        tech.append(f"uses **{backend}** for the backend")

    if database:
        tech.append(f"stores data in **{database}**")

    if tech:
        summary.append(
            "The project " + ", ".join(tech) + "."
        )

    # Languages
    if languages:

        important = []

        for language in languages:

            if language not in ["JSON", "Markdown"]:
                important.append(language)

        if important:
            summary.append(
                "Primary technologies include **" +
                ", ".join(important[:5]) +
                "**."
            )

    # Repository size
    if total_files > 3000:

        summary.append(
            "This is a **large-scale repository**, indicating a mature and actively developed project."
        )

    elif total_files > 500:

        summary.append(
            "This is a **medium-sized repository** suitable for production-level development."
        )

    else:

        summary.append(
            "This is a **small repository**, making it easier to understand and contribute to."
        )

    return "\n\n".join(summary)