from fastapi import FastAPI, HTTPException, Query
from pathlib import Path
from fastapi.responses import PlainTextResponse
from typing import List

app = FastAPI()
MINUTES_DIR = Path("minutes")

@app.get("/list_files", response_model=List[str])
def list_files():
    # Recursively list all .txt files relative to MINUTES_DIR
    return [str(p.relative_to(MINUTES_DIR)) for p in MINUTES_DIR.rglob("*.txt")]

@app.get("/read_file", response_class=PlainTextResponse)
def read_file(filename: str = Query(..., description="Relative path to the .txt file under minutes/")):
    file_path = MINUTES_DIR / filename
    # Prevent path traversal
    try:
        file_path = file_path.resolve(strict=True)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    if not str(file_path).startswith(str(MINUTES_DIR.resolve())):
        raise HTTPException(status_code=400, detail="Invalid file path")
    if not file_path.is_file() or not file_path.suffix.lower() == ".txt":
        raise HTTPException(status_code=400, detail="Not a .txt file")
    try:
        return file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")

# To run: uvicorn mcp_server:app --reload 