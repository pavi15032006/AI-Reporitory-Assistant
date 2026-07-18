import "../styles/SuggestedQuestions.css";

function SuggestedQuestions({ onQuestionClick }) {

    const questions = [
        {
            label: "🛠 Technologies",
            question: "What technologies are used in this repository?"
        },
        {
            label: "📈 Health",
            question: "Is this repository production ready?"
        },
        {
            label: "🚀 Improvements",
            question: "What improvements do you recommend?"
        },
        {
            label: "📖 README",
            question: "Summarize the README."
        },
        {
            label: "🏗 Structure",
            question: "Explain the project structure."
        },
        {
            label: "☁ Deployment",
            question: "How can this repository be deployed?"
        }
    ];

    return (

        <div className="suggested-container">

            <h3>💡 Quick Questions</h3>

            <div className="suggested-buttons">

                {questions.map((item, index) => (

                    <button
                        key={index}
                        className="suggested-button"
                        onClick={() => onQuestionClick(item.question)}
                    >
                        {item.label}
                    </button>

                ))}

            </div>

        </div>

    );

}

export default SuggestedQuestions;