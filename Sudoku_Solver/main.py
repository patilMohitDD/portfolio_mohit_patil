from fastapi import FastAPI, Path, Request
from typing import Optional
from models import SudokuMatrix
from functions import solver, generate_id
from json import dumps, loads, dump
import logging

logger = logging.getLogger()


# This is your main storage
db = {}
with open('db.json') as f:
    db = loads(f.read())


app = FastAPI()

@app.get("/get_sudokus")
async def get_sudoku():
    return db

@app.get("/get_sudoku_by_id/{id}")
async def get_sudoku_by_id(id:int = Path(gt=0)):
    if str(id) not in db:
        return {"Mssg" : "No Sudoku present"}

    return db.get(str(id))

@app.get("/solve_sudoku_by_id/{id}")
async def solve_sudoku_by_id(id: int = Path(gt=0)):
    if str(id) not in db:
        return {"Mssg" : "No Sudoku present"}

    response = solver(db[str(id)])
    return response

@app.post("/input_sudoku/")# matrix: SudokuMatrix
async def input_sudoku(matrix: SudokuMatrix, request:Request):
    #generate ID for matrix
    id = generate_id()

    matrix = await (request.json())
    # print(matrix["matrix"])

    # Populating new matirx into DB
    db[id] = matrix["matrix"]

    with open('db.json', 'w') as f:
        dump(db, f)

    return {
        "id": int(id),
        "mssg": "Stored Successfully"
    }





