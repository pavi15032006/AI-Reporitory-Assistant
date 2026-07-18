from fastapi import APIRouter

from app.schemas.scanner_schema import ScannerRequest
from app.services.analysis_service import analyze_repository

router = APIRouter()


@router.post("/scan-repository")
def scan_repo(request: ScannerRequest):

    return analyze_repository(request.repository_name)