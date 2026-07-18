import ReactMarkdown from "react-markdown";
import "../styles/ChatMessage.css";

function ChatMessage({ sender, message }) {

    return (

        <div
            className={
                sender === "user"
                    ? "chat-message user-message"
                    : "chat-message ai-message"
            }
        >

            <div className="chat-header">

                {sender === "user"
                    ? "👤 You"
                    : "🤖 AI Repository Assistant"}

            </div>

            <div className="chat-content">

                <ReactMarkdown>
                    {message}
                </ReactMarkdown>

            </div>

        </div>

    );

}

export default ChatMessage;