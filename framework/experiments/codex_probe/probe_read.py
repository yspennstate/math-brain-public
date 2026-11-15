"""probe_read.py <ID> [<ID> ...]: for each Codex harness probe in codex_probe/<ID>/, the tool calls of its rollout
in order (the functions each call names) beside the blocks of hook lines in its codex.log, and the totals:
calls by function, PreToolUse and PostToolUse blocks. A hook block is a run of consecutive 'hook:' lines.
Prints names and counts, plus REPORT.md (the probe's own short table)."""
import collections
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
H = os.environ.get("PROBE_CODEX_HOME", os.path.expanduser("~/.codex"))
for bid in sys.argv[1:]:
    D = os.path.join(HERE, bid)
    print("==== %s" % bid)
    seq = []
    usage = None
    for f in sorted(glob.glob(os.path.join(H, "sessions", "2026", "11", "1[12]", "*.jsonl")), key=os.path.getmtime)[-40:]:
        mine = False
        rows = []
        u = None
        with io.open(f, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                p = d.get("payload") if isinstance(d.get("payload"), dict) else {}
                if d.get("type") == "session_meta":
                    cw = str(p.get("cwd", "")).replace("\\", "/").rstrip("/")
                    mine = cw.endswith("codex_probe/" + bid)
                    if not mine:
                        break
                    continue
                pt = p.get("type")
                if pt == "custom_tool_call":
                    s = p.get("input") or ""
                    s = s if isinstance(s, str) else json.dumps(s)
                    found = re.findall(r"tools\.([A-Za-z_0-9]+)", s)
                    rows.append("%s(%s)" % (p.get("name"), "+".join(found) or "no tool named"))
                elif pt == "function_call":
                    rows.append("fn %s" % p.get("name"))
                elif pt == "token_count":
                    info = p.get("info") if isinstance(p.get("info"), dict) else {}
                    if isinstance(info.get("total_token_usage"), dict):
                        u = info["total_token_usage"]
        if mine:
            seq, usage = rows, u
    print("tool calls in the rollout, in order (%d):" % len(seq))
    for r in seq:
        print("   " + r)
    c = collections.Counter()
    for r in seq:
        for x in re.findall(r"[A-Za-z_0-9]+", r.split("(", 1)[1] if "(" in r else r):
            c[x] += 1
    print("by function:", dict(c))
    if usage:
        print("tokens: input %s (cached %s), output %s" % (usage.get("input_tokens"), usage.get("cached_input_tokens"), usage.get("output_tokens")))
    lp = os.path.join(D, "codex.log")
    lines = io.open(lp, encoding="utf-8", errors="replace").read().split("\n") if os.path.exists(lp) else []
    blocks = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("hook: "):
            ev = collections.Counter()
            while i < len(lines) and lines[i].startswith("hook: "):
                parts = lines[i].split()
                ev[(parts[1], parts[2] if len(parts) > 2 else "start")] += 1
                i += 1
            blocks.append(ev)
        else:
            i += 1
    pre = sum(1 for b in blocks if any(k[0] == "PreToolUse" and k[1] == "start" for k in b))
    post = sum(1 for b in blocks if any(k[0] == "PostToolUse" and k[1] == "start" for k in b))
    fail = sum(v for b in blocks for k, v in b.items() if k[1] == "Failed")
    print("log: %d lines; hook blocks %d; blocks with PreToolUse starts %d; with PostToolUse starts %d; failed hook lines %d"
          % (len(lines), len(blocks), pre, post, fail))
    for b in blocks:
        print("   " + ", ".join("%s %s %d" % (k[0], k[1], v) for k, v in sorted(b.items())))
    marks = [ln for ln in lines if re.match(r"^\d\d:\d\d(:\d\d)? (start|exit|held|gave)", ln)]
    print("launcher marks:", marks[-4:])
    rp = os.path.join(D, "REPORT.md")
    if os.path.exists(rp):
        print("REPORT.md:")
        print(io.open(rp, encoding="utf-8", errors="replace").read()[:1500])
    else:
        print("no REPORT.md yet")
