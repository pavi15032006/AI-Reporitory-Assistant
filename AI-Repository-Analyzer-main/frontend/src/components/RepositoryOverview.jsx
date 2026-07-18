import "./RepositoryOverview.css";

function RepositoryOverview({ repository }) {

    let repositorySize = "Unknown";

    if (repository.total_files <= 500) {
        repositorySize = "🟢 Small Repository";
    }
    else if (repository.total_files <= 3000) {
        repositorySize = "🟡 Medium Repository";
    }
    else {
        repositorySize = "🔴 Large Repository";
    }

    return (

        <div className="overview-card">

            <h2 className="overview-title">
                📦 Repository Overview
            </h2>

            <div className="overview-grid">

                <div className="overview-item">
                    <span className="overview-label">
                        📁 Repository
                    </span>

                    <span className="overview-value">
                        {repository.repository_name}
                    </span>
                </div>

                <div className="overview-item">
                    <span className="overview-label">
                        🏷 Category
                    </span>

                    <span className="overview-value">
                        {repository.project_type}
                    </span>
                </div>

                <div className="overview-item">
                    <span className="overview-label">
                        📦 Repository Size
                    </span>

                    <span className="overview-value">
                        {repositorySize}
                    </span>
                </div>

            </div>

        </div>

    );

}

export default RepositoryOverview;