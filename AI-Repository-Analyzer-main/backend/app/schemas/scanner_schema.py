from pydantic import BaseModel


class ScannerRequest(BaseModel):
    repository_name: str