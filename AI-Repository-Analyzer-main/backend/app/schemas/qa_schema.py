from pydantic import BaseModel


class QARequest(BaseModel):
    repository_name: str
    question: str