from fastapi import FastAPI, Path
from typing import Optional
from store import sudokus
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/get_sudoku_to_solve")
async def get_sudoku(id:Optional[int] = None , description="This will a give all the Sudokus we have to solve with there ID's"):

    # content = json.dumps(sudokus)
    response = JSONResponse(content=sudokus) # beautfiying the response and sending
    return response
