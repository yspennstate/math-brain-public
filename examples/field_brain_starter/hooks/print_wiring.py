"""Print the hook block that connects this brain to an agent, with this folder's absolute paths filled in.

Every hook here says "wire it with its absolute path". This writes that block for you, so a new brain is connected
by pasting one JSON object rather than by editing six paths by hand.

    python3 hooks/print_wiring.py --runtime claude    the "hooks" object for ~/.claude/settings.json
    python3 hooks/print_wiring.py --runtime codex     the "hooks" object for ~/.codex/hooks.json
    python3 hooks/print_wiring.py --selftest          check that both blocks parse and name files that exist

Paste the printed object as the value of "hooks" (merge it with any hooks you already have), then start a new
session: both runtimes read their hook files when a session starts. The commands use the Python that ran this
script, so the hooks run under the same interpreter you tested them with. On Windows the Codex block also carries
"commandWindows", which Codex runs there.

What goes where, and why, is in docs/codex-hooks-quickstart.md. Standard library only.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# event, script, extra arguments per runtime, timeout in seconds, matcher per runtime (None = every tool)
HOOKS = [
    ("start",  "wake_hook.py",       {"claude": ["--runtime", "claude"], "codex": []}, 30, None),
    ("prompt", "request_hook.py",    {"claude": ["--runtime", "claude"], "codex": []}, 30, None),
    ("prompt", "recall_hook.py",     {"claude": ["--runtime", "claude"], "codex": []}, 60, None),
    ("tool",   "scar_hook.py",       {"claude": [], "codex": []}, 30, {"claude": "Bash|Edit|Write", "codex": "Bash|apply_patch"}),
    ("stop",   "request_hook.py",    {"claude": ["--stop"], "codex": ["--stop"]}, 30, None),
    ("stop",   "write_back_hook.py", {"claude": [], "codex": []}, 60, None),
    ("compact", "compaction_hook.py", {"claude": ["--runtime", "claude"], "codex": []}, 30,
     {"claude": "compact", "codex": None}),
]

# Claude Code has a SessionStart event; Codex hands the wake to the first prompt, which wake_hook.py detects.
# Claude Code starts the session again with source "compact" after a compaction (the matcher picks that start);
# Codex has no compaction event, so compaction_hook.py looks for a new compaction on every prompt.
EVENTS = {
    "claude": {"start": "SessionStart", "prompt": "UserPromptSubmit", "tool": "PreToolUse", "stop": "Stop",
               "compact": "SessionStart"},
    "codex": {"start": "UserPromptSubmit", "prompt": "UserPromptSubmit", "tool": "PreToolUse", "stop": "Stop",
              "compact": "UserPromptSubmit"},
}


def quote(path):
    return '"%s"' % path if " " in path else path


def wiring(runtime, python=None, windows=None):
    python = python or sys.executable or "python3"
    windows = (os.name == "nt") if windows is None else windows
    out = {}
    for kind, script, extra, timeout, matcher in HOOKS:
        path = os.path.join(HERE, script)
        command = " ".join([quote(python), quote(path)] + extra[runtime])
        hook = {"type": "command", "command": command, "timeout": timeout}
        if runtime == "codex" and windows:
            hook["commandWindows"] = command
        group = {"hooks": [hook]}
        if matcher and matcher.get(runtime):
            group = {"matcher": matcher[runtime], "hooks": [hook]}
        out.setdefault(EVENTS[runtime][kind], []).append(group)
    return out


def selftest():
    failures = []
    for runtime in ("claude", "codex"):
        block = json.loads(json.dumps(wiring(runtime)))
        commands = [h["command"] for groups in block.values() for g in groups for h in g["hooks"]]
        if len(commands) != len(HOOKS):
            failures.append("%s: %d commands, expected %d" % (runtime, len(commands), len(HOOKS)))
        for _, script, _, _, _ in HOOKS:
            if not os.path.exists(os.path.join(HERE, script)):
                failures.append("%s: %s is missing" % (runtime, script))
        if "PreToolUse" not in block or "matcher" not in block["PreToolUse"][0]:
            failures.append("%s: the tool hook has no matcher" % runtime)
    if "SessionStart" not in wiring("claude") or "SessionStart" in wiring("codex"):
        failures.append("the wake hook is on the wrong event")
    if "commandWindows" not in json.dumps(wiring("codex", windows=True)):
        failures.append("the Codex block on Windows has no commandWindows")
    if "commandWindows" in json.dumps(wiring("claude", windows=True)):
        failures.append("the Claude Code block carries commandWindows")
    for f in failures:
        print("FAIL", f)
    print("print_wiring selftest:", "ok" if not failures else "%d failure(s)" % len(failures))
    return 1 if failures else 0


def main():
    argv = sys.argv[1:]
    if "--selftest" in argv:
        return selftest()
    runtime = argv[argv.index("--runtime") + 1] if "--runtime" in argv else "claude"
    if runtime not in EVENTS:
        print("--runtime is claude or codex", file=sys.stderr)
        return 2
    print(json.dumps({"hooks": wiring(runtime)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
