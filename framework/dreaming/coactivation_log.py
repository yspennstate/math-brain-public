#!/usr/bin/env python3
"""coactivation_log.py - PostToolUse hook: log which memories fire together (Hebbian).

"Cells that fire together wire together" (Hebb 1949; Lowel & Singer 1992). The nav graph is static
Jaccard - amnesic about its own use: two memories always retrieved together weigh the same as two
that merely share vocabulary. This logs each READ of a memory file to a per-session file; the Stop
hook (coactivation_end.py) aggregates a session's co-reads into coactivation.tsv, which
build_brain_architecture.py blends into the association graph - so links come to reflect what the
brain actually reasons with together.

Routes (3 Nov 2026): the Read tool on a memory file, and a Bash/PowerShell command that names a
memory file (cat/head/sed/grep on memory/<slug>.md) or asks brain.py node/neighbors <slug>. Measured
on 8 transcripts, the shell routes carried 14 of 24 used slugs and 39 of 54 co-use pairs that the
Read-only logger never saw. A command naming more than MAX_PER_CMD memories is a sweep, not a use,
and logs nothing.

Fail-safe silent; never blocks or slows a tool call. Reads stdin (PostToolUse JSON), no output.
"""
import sys, os, io, re, json

HOME = os.path.expanduser("~")
MEMDIR = os.path.join(HOME, ".claude", "projects", "{{BRAIN_SLUG}}", "memory").lower()
LOGDIR = os.environ.get("COACT_LOGDIR_TEST") or os.path.join(HOME, ".claude", "dreaming", "coactivation_session")
SKIP = {"MEMORY", "INDEX_ARCHIVE", "PREDICTIONS", "STATE_OF_MIND", "OPEN_QUESTIONS",
        "AUTOBIOGRAPHY", "MODEL_OF_PARTNER", "FASCINATIONS", "THE_OTHER_MINDS", "CONSCIENCE",
        "MISTAKES", "CURIOSITY"}  # substrate pages, not memories (MISTAKES leaked in as a false hub)
MAX_PER_CMD = 6
RX_PATH = re.compile(r"memory[/\\]+([A-Za-z0-9_.-]+?)\.md\b")
RX_NODE = re.compile(r"brain\.py\s+(?:node|neighbors)\s+([A-Za-z0-9_]+)")


def ok(slug):
    return slug and slug not in SKIP and not slug.startswith("dream_")


def shell_slugs(cmd):
    out = []
    for rx in (RX_PATH, RX_NODE):
        for m in rx.finditer(cmd):
            s = m.group(1)
            if ok(s) and s not in out and os.path.isfile(os.path.join(MEMDIR, s + ".md")):
                out.append(s)
    # a bare slug after cd into the memory dir: "cd .../memory && cat <slug>.md"
    if "memory" in cmd.lower() and not out:
        for m in re.finditer(r"(?<![/\\\w])([a-z0-9][a-z0-9_]{12,})\.md\b", cmd):
            s = m.group(1)
            if ok(s) and s not in out and os.path.isfile(os.path.join(MEMDIR, s + ".md")):
                out.append(s)
    return out if len(out) <= MAX_PER_CMD else []


def main():
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        # Discovery is not execution: this script writes, so a help request must
        # exit before any work. See script_help_flag_can_execute_work.
        print(__doc__ or os.path.basename(__file__))
        return
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return
    try:
        tool = data.get("tool_name")
        inp = data.get("tool_input", {}) or {}
        slugs = []
        if tool == "Read":
            fp = (inp.get("file_path", "") or "")
            fpl = fp.replace("/", "\\").lower()
            if MEMDIR not in fpl or not fpl.endswith(".md"):
                return
            s = os.path.basename(fp)[:-3]
            if ok(s):
                slugs = [s]
        elif tool in ("Bash", "PowerShell"):
            slugs = shell_slugs(str(inp.get("command", "") or ""))
        if not slugs:
            return
        sess = data.get("session_id") or "nosess"
        os.makedirs(LOGDIR, exist_ok=True)
        with io.open(os.path.join(LOGDIR, sess + ".log"), "a", encoding="utf-8") as f:
            f.write("".join(s + "\n" for s in slugs))
    except Exception:
        return


if __name__ == "__main__":
    try:
        import os as _o, sys as _s
        _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
        import brain_switch as _bsw
        _bsw.gate()
    except SystemExit:
        raise
    except Exception:
        pass
    main()
