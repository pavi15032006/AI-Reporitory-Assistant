import { useState } from "react";
import API from "../services/api";
import ChatMessage from "./ChatMessage";
import SuggestedQuestions from "./SuggestedQuestions";
import "../styles/AIChat.css";

function AIChat({ repository }) {

    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const askQuestion = async () => {

        if (!question.trim() || loading) return;

        const userQuestion = question;

        setMessages((prev) => [
            ...prev,
            {
                sender: "user",
                message: userQuestion
            }
        ]);

        setQuestion("");

        setLoading(true);

        try {

            const response = await API.post("/ask-question", {

                repository_name: repository.repository_name,

                question: userQuestion

            });

            setMessages((prev) => [

                ...prev,

                {

                    sender: "ai",

                    message: response.data.answer

                }

            ]);

        }

        catch {

            setMessages((prev) => [

                ...prev,

                {

                    sender: "ai",

                    message: "Sorry! I couldn't analyze this repository."

                }

            ]);

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div className="chat-card">

            <div className="chat-header">

                <div className="chat-icon">

                    🤖

                </div>

                <div>

                    <h2>AI Repository Assistant</h2>

                    <p>

                        Ask anything about this repository

                    </p>

                </div>

            </div>

            <SuggestedQuestions

                onQuestionClick={(q)=>setQuestion(q)}

            />

            <div className="chat-history">

                {

                    messages.length===0 && (

                        <div className="welcome-message">

                            👋 Welcome!

                            <br/><br/>

                            Try asking:

                            <ul>

                                <li>What technologies are used?</li>

                                <li>Explain the project.</li>

                                <li>How can I improve this repository?</li>

                            </ul>

                        </div>

                    )

                }

                {

                    messages.map((msg,index)=>(

                        <ChatMessage

                            key={index}

                            sender={msg.sender}

                            message={msg.message}

                        />

                    ))

                }

                {

                    loading && (

                        <div className="typing">

                            🤖 AI is analyzing the repository...

                        </div>

                    )

                }

            </div>

            <div className="chat-input">

                <input

                    type="text"

                    placeholder="Ask anything about this repository..."

                    value={question}

                    disabled={loading}

                    onChange={(e)=>setQuestion(e.target.value)}

                    onKeyDown={(e)=>{

                        if(e.key==="Enter"){

                            askQuestion();

                        }

                    }}

                />

                <button

                    onClick={askQuestion}

                    disabled={loading}

                >

                    {loading ? "Thinking..." : "Send"}

                </button>

            </div>

        </div>

    );

}

export default AIChat;