from fastapi import FastAPI, Path
from typing import Optional
from store import sudokus
from fastapi.responses import JSONResponse
import json
from pprint import pprint

app = FastAPI()

@app.get("/get_sudokus")
async def get_sudoku(id:Optional[int] = None , description="This will a give all the Sudokus we have to solve with there ID's"):
    return json.dumps(sudokus)
    # response = JSONResponse(content=sudokus) # beautfiying the response and sending
    # return response

@app.get(("/get_sudoku_by_id/{id}"))
async def get_sudoku_by_id(id:int = Path(gt=0)): # id should be greater than 0
    response = sudokus.get(id)
    return {id: response}


