import "../styles/HealthCard.css";

function HealthCard({ repository }) {

    const checks = repository.checks;

    const getScoreColor = (score) => {

        if (score >= 80) return "#16a34a";
        if (score >= 60) return "#a35816";
        return "#ef4444";

    };

    return (

        <div className="health-card">

            <h2>📊 Repository Health</h2>

            <div
                className="health-score"
                style={{ borderColor: getScoreColor(repository.health_score) }}
            >

                <h1
                    style={{ color: getScoreColor(repository.health_score) }}
                >
                    {repository.health_score}
                </h1>

                <span>/100</span>

            </div>

            <div
                className="health-status"
                style={{ background: getScoreColor(repository.health_score) }}
            >
                {repository.health_status}
            </div>

            <h3>Project Checks</h3>

            <div className="checks-grid">

                <div className="check-box">
                    <span>README</span>
                    <strong>{checks.readme ? "✅" : "❌"}</strong>
                </div>

                <div className="check-box">
                    <span>.gitignore</span>
                    <strong>{checks.gitignore ? "✅" : "❌"}</strong>
                </div>

                <div className="check-box">
                    <span>LICENSE</span>
                    <strong>{checks.license ? "✅" : "❌"}</strong>
                </div>

                <div className="check-box">
                    <span>Dockerfile</span>
                    <strong>{checks.dockerfile ? "✅" : "❌"}</strong>
                </div>

                <div className="check-box">
                    <span>Tests</span>
                    <strong>{checks.tests ? "✅" : "❌"}</strong>
                </div>

                <div className="check-box">
                    <span>.env.example</span>
                    <strong>{checks.env_example ? "✅" : "❌"}</strong>
                </div>

            </div>

        </div>

    );

}

export default HealthCard;