#!/usr/bin/env bash
# start_mcp.sh

# (optional) source your rc files
[ -f "$HOME/.bashrc" ] && source "$HOME/.bashrc"

# Run with full path so PATH isn’t an issue
/home/tyrda/.local/bin/uv run /mnt/c/LocalProgramming/KerrCounty/.venv/bin/python3.12 /mnt/c/LocalProgramming/KerrCounty/mcp_server.py
