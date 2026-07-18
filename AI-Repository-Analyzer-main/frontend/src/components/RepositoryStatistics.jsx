import "./RepositoryStatistics.css";

function RepositoryStatistics({ repository }) {

    if (!repository) return null;

    const stats = repository.statistics || {};

    return (

        <div className="card">

            <h2>📊 Repository Statistics</h2>

            <div className="statistics-grid">

                <div>
                    <strong>📄 Total Files</strong>
                    <p>{stats.total_files ?? repository.total_files}</p>
                </div>

                <div>
                    <strong>📁 Total Folders</strong>
                    <p>{stats.total_folders ?? repository.total_folders}</p>
                </div>

                <div>
                    <strong>💻 Source Files</strong>
                    <p>{stats.source_files ?? 0}</p>
                </div>

                <div>
                    <strong>🧪 Test Files</strong>
                    <p>{stats.test_files ?? 0}</p>
                </div>

                <div>
                    <strong>⚙️ Configuration Files</strong>
                    <p>{stats.config_files ?? 0}</p>
                </div>

                <div>
                    <strong>📚 Documentation Files</strong>
                    <p>{stats.documentation_files ?? 0}</p>
                </div>

                <div>
                    <strong>🎨 Style Files</strong>
                    <p>{stats.style_files ?? 0}</p>
                </div>

                <div>
                    <strong>🖼️ Image Files</strong>
                    <p>{stats.image_files ?? 0}</p>
                </div>

                <div>
                    <strong>🗄️ Database Files</strong>
                    <p>{stats.database_files ?? 0}</p>
                </div>

                <div>
                    <strong>📦 Build Files</strong>
                    <p>{stats.build_files ?? 0}</p>
                </div>

                <div>
                    <strong>📂 Other Files</strong>
                    <p>{stats.other_files ?? 0}</p>
                </div>

                <div>
                    <strong>👁️ Hidden Files</strong>
                    <p>{stats.hidden_files ?? 0}</p>
                </div>

            </div>

        </div>

    );

}

export default RepositoryStatistics;