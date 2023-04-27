from fastapi import FastAPI, Path
from typing import Optional
from store import sudokus
from models import SudokuMatrix


app = FastAPI()

@app.get("/get_sudokus")
async def get_sudoku():
    return sudokus

@app.get(("/get_sudoku_by_id/{id}"))
async def get_sudoku_by_id(id:int = Path(gt=0)):
    if id not in sudokus:
        return {"Mssg" : "No Sudoku present"}
    return sudokus.get(id)

@app.post("/sudoku_solver")
async def sudoku_solver(matrix:SudokuMatrix, id:int):
    if id in sudokus:
        return {"mssg": "ID existing"}
    
    sudokus[id] = matrix
    return {
        "mssg":f"{id} Stored successfully"
    }



