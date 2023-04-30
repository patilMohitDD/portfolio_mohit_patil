from pydantic import BaseModel
from typing import List

class SudokuMatrix(BaseModel):
    matrix: List[List[str]]