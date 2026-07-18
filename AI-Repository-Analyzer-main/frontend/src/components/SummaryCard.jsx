import ReactMarkdown from "react-markdown";
import "../styles/SummaryCard.css";

function SummaryCard({ repository }) {

    return (

        <div className="summary-card">

            <div className="summary-header">

                

                <h2 className="summary-title">
                     AI Repository Insights
                </h2>

                <p>
                    AI-generated analysis of the repository
                </p>

            </div>

            <div className="summary-content">

                <ReactMarkdown>
                    {repository.summary}
                </ReactMarkdown>

            </div>

        </div>

    );

}

export default SummaryCard;