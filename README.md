# KerrCounty



## Claude Desktop setup
```json
{
  "mcpServers": {
    "kerr-county-minutes": {
      "command": "C:\\LocalProgramming\\KerrCounty\\start_mcp.bat",
      "args": []
    }
  }
}
```

## Comments
Had issues getting Claude to launch wsl and have uv and dependencies installed.
The only solution I could get to work was having a bat file for Claude to run and having a .sh file to run it.