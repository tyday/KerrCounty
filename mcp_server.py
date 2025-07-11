import asyncio
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Sequence
from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the FastMCP server
mcp = FastMCP("Kerr County Minutes")

MINUTES_DIR = Path("minutes")

@mcp.tool()
def list_files() -> str:
    """List all available .txt files in the minutes directory"""
    try:
        txt_files = []
        for file_path in MINUTES_DIR.rglob("*.txt"):
            txt_files.append(str(file_path.relative_to(MINUTES_DIR)))
        
        if not txt_files:
            return "No .txt files found in the minutes directory."
        
        return f"Available .txt files:\n" + "\n".join(txt_files)
    except Exception as e:
        logger.error(f"Error listing files: {e}")
        return f"Error listing files: {e}"

@mcp.tool()
def read_file(filename: str) -> str:
    """Read the content of a specific .txt file from the minutes directory"""
    try:
        if not filename:
            return "Error: filename parameter is required"
        
        file_path = MINUTES_DIR / filename
        
        # Security check: ensure file is within minutes directory
        try:
            file_path = file_path.resolve(strict=True)
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"
        
        if not str(file_path).startswith(str(MINUTES_DIR.resolve())):
            return "Error: Invalid file path"
        
        if not file_path.is_file() or not file_path.suffix.lower() == ".txt":
            return "Error: Not a .txt file"
        
        content = file_path.read_text(encoding="utf-8", errors="replace")
        return f"File content for '{filename}':\n\n{content}"
        
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        return f"Error reading file: {e}"

if __name__ == "__main__":
    mcp.run(transport='stdio')