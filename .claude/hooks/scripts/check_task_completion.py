#!/usr/bin/env python3
"""
PostToolUse hook for Agent tool: Task Completion Guard.

When an Agent tool call completes, this script checks master-status.json
to determine if the workflow has finished. If completed, it emits a
mandatory instruction to update all in_progress tasks.

This replaces LLM memory with a deterministic trigger:
  "계산은 Python이, 판단은 LLM이" — the CHECK is Python, the UPDATE is LLM.
"""
import json
import sys
import os
from pathlib import Path


def get_project_root():
    return os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd())


def check_master_status():
    """Read master-status.json and return overall_status."""
    project_root = get_project_root()
    status_file = Path(project_root) / 'env-scanning' / 'integrated' / 'logs' / 'master-status.json'

    if not status_file.exists():
        return None

    try:
        with open(status_file, 'r') as f:
            data = json.load(f)
        return data.get('status', data.get('overall_status', None))
    except (json.JSONDecodeError, IOError):
        return None


def main():
    try:
        hook_data = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    except (json.JSONDecodeError, EOFError):
        hook_data = {}

    # Only act on Agent tool completions
    tool_name = hook_data.get('tool_name', '')
    if tool_name != 'Agent':
        return 0

    # Check if the agent was scan/orchestrator related
    tool_input = hook_data.get('tool_input', {})
    agent_type = tool_input.get('subagent_type', '')
    description = tool_input.get('description', '').lower()
    prompt = tool_input.get('prompt', '').lower()

    scan_keywords = [
        'orchestrator', 'env-scan', 'env scan', 'autopilot',
        'quadruple', 'environmental scanning', 'workflow',
        'wf1', 'wf2', 'wf3', 'wf4', 'integration',
    ]

    is_scan_agent = (
        'orchestrator' in agent_type
        or any(kw in description for kw in scan_keywords)
        or any(kw in prompt[:200] for kw in scan_keywords)
    )

    if not is_scan_agent:
        return 0

    # Check if workflow completed
    status = check_master_status()

    if status == 'completed':
        print(
            "⚠️ TASK COMPLETION GUARD: master-status.json shows 'completed'. "
            "You MUST now update ALL in_progress tasks to 'completed' using TaskUpdate "
            "BEFORE responding to the user. This is a mandatory post-workflow action."
        )

    return 0


if __name__ == '__main__':
    sys.exit(main())
