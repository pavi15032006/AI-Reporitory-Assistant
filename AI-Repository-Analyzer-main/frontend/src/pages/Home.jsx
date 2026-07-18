import { useState } from "react";
import API from "../services/api";
import "../styles/Home.css";

import RepositoryOverview from "../components/RepositoryOverview";
import RepositoryStatistics from "../components/RepositoryStatistics";
import SummaryCard from "../components/SummaryCard";
import TechnologyCard from "../components/TechnologyCard";
import HealthCard from "../components/HealthCard";
import AIChat from "../components/AIChat";

function Home() {

    const [githubUrl, setGithubUrl] = useState("");
    const [repositoryData, setRepositoryData] = useState(null);

    const analyzeRepository = async () => {

        if (!githubUrl.trim()) {
            alert("Please enter a GitHub repository URL.");
            return;
        }

        try {

            await API.post("/clone-repository", {
                github_url: githubUrl
            });

            const repositoryName = githubUrl
                .trim()
                .replace(/\/$/, "")
                .split("/")
                .pop();

            const response = await API.post("/scan-repository", {
                repository_name: repositoryName
            });

            setRepositoryData(response.data);

        } catch (error) {

            console.error(error);
            alert("Failed to analyze repository.");

        }

    };

    return (

        <div className="home-container">

            <h1>🤖 AI Repository Assistant</h1>

            <p>
                Analyze any GitHub repository using Artificial Intelligence.
            </p>

            <div className="input-section">

                <input
                    type="text"
                    placeholder="Enter GitHub Repository URL"
                    value={githubUrl}
                    onChange={(e) => setGithubUrl(e.target.value)}
                />

                <button onClick={analyzeRepository}>
                    Analyze Repository
                </button>

            </div>

            {repositoryData && (

                <>

                    {/* Repository Overview */}
                    <RepositoryOverview repository={repositoryData} />

                    {/* Statistics */}
                    <RepositoryStatistics repository={repositoryData} />

                    {/* Two Cards */}
                    <div className="dashboard-grid">

                        <TechnologyCard repository={repositoryData} />

                        <HealthCard repository={repositoryData} />

                    </div>

                    {/* Summary */}
                    <SummaryCard repository={repositoryData} />

                    {/* AI Chat */}
                    <AIChat repository={repositoryData} />

                </>

            )}

        </div>

    );

}

export default Home;