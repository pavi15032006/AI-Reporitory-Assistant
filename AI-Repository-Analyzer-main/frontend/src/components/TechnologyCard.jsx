import "../styles/TechnologyCard.css";

function TechnologyCard({ repository }) {

    const hasFrameworks =
        repository.frontend_framework ||
        repository.backend_framework ||
        repository.database;

    return (

        <div className="card">

            <h2>🛠 Technology Stack</h2>

            {hasFrameworks ? (

                <div className="framework-grid">

                    {repository.frontend_framework && (

                        <div className="framework-card">

                            <h3>🎨 Frontend</h3>

                            <span className="framework-badge">
                                {repository.frontend_framework}
                            </span>

                        </div>

                    )}

                    {repository.backend_framework && (

                        <div className="framework-card">

                            <h3>⚙️ Backend</h3>

                            <span className="framework-badge">
                                {repository.backend_framework}
                            </span>

                        </div>

                    )}

                    {repository.database && (

                        <div className="framework-card">

                            <h3>🗄 Database</h3>

                            <span className="framework-badge">
                                {repository.database}
                            </span>

                        </div>

                    )}

                </div>

            ) : (

                <p className="no-framework">
                    No major framework detected.
                </p>

            )}

            <h3 className="language-title">
                💻 Programming Languages
            </h3>

            <div className="language-container">

                {repository.languages.map((language, index) => (

                    <span
                        key={index}
                        className="language-badge"
                    >
                        {language}
                    </span>

                ))}

            </div>

        </div>

    );

}

export default TechnologyCard;