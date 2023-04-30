from fastapi import FastAPI, Path
from typing import Optional
from constants import sudokus
from models import SudokuMatrix
from functions import solver
from json import dumps


app = FastAPI()

@app.get("/get_sudokus")
async def get_sudoku():
    return sudokus

@app.get("/get_sudoku_by_id/{id}")
async def get_sudoku_by_id(id:int = Path(gt=0)):
    if id not in sudokus:
        return {"Mssg" : "No Sudoku present"}
    return sudokus.get(id)

@app.get("/solve_sudoku_by_id/{id}")
async def solve_sudoku_by_id(id: int = Path(gt=0)):
    if id not in sudokus:
        return {"Mssg" : "No Sudoku present"}

    response = solver(sudokus[id])
    return response
    

@app.post("/sudoku_solver")
async def sudoku_solver(matrix:SudokuMatrix, id:int):
    if id in sudokus:
        return {"mssg": "ID existing"}
    
    sudokus[id] = matrix
    return {
        "mssg":f"{id} Stored successfully"
    }



