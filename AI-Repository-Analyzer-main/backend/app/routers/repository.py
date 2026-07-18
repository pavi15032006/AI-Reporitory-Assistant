from fastapi import APIRouter

from app.schemas.repository_schema import RepositoryRequest
from app.services.repository_service import clone_repository

router = APIRouter()


@router.post("/clone-repository")
def clone_repo(repository: RepositoryRequest):

    result = clone_repository(repository.github_url)

    return result