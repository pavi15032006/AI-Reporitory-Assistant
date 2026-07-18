from fastapi import APIRouter
from app.schemas.qa_schema import QARequest
from app.services.analysis_service import analyze_repository
from app.services.gemini_service import ask_gemini

router = APIRouter()


@router.post("/ask-question")
def ask_question(request: QARequest):

    # Analyze repository
    repository_data = analyze_repository(request.repository_name)

    # Ask Gemini
    answer = ask_gemini(
        request.question,
        repository_data
    )

    return {
        "question": request.question,
        "answer": answer
    }