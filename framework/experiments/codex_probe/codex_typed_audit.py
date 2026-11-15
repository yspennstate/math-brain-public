"""codex_typed_audit.py <rollout.jsonl> [...] [--guard <hook.py>] [--quiet] [--json <out>]

Codex runs its PreToolUse hooks on a command started as its own process (exec_command) and on a patch, and on
nothing typed into a shell that is already open (write_stdin). This check reads a finished rollout and puts every
typed line before the deny-only guard, the way Codex would have for a command of its own: the guard's real file, a
PreToolUse payload on stdin, tool name "Bash" (the name Codex reports for its shell), the rollout's own folder as cwd.

It never runs the typed text. It reports how many write_stdin calls it read, how many typed something, how many
typed something it could not read as a literal (so a pass over nothing is visible), and every line the guard would
have refused. Exit 0: nothing refused. Exit 4: at least one line refused. Exit 1: usage or an unreadable rollout.

Default guard: ~/.claude/dreaming/codex_help_guard_hook.py (no brain start, no state: the no-subagents policy, the
film picture policy and the local --help guard). Other hooks keep state for each session and are not run here."""
import io
import json
import os
import re
import subprocess
import sys

CALL = re.compile(r"tools\.(exec_command|write_stdin|apply_patch)\s*\(")
STR = r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`(?:[^`\\]|\\.)*`)'
CHARS_LIT = re.compile(r"chars\s*:\s*" + STR)
CHARS_ANY = re.compile(r"chars\s*:")
ESC = re.compile(r"\\(u[0-9a-fA-F]{4}|x[0-9a-fA-F]{2}|.)", re.S)
SIMPLE = {"n": "\n", "r": "\r", "t": "\t", "b": "\b", "f": "\f", "v": "\v", "0": "\0"}


def unescape(body):
    def one(m):
        g = m.group(1)
        if g[0] in "ux" and len(g) > 1:
            return chr(int(g[1:], 16))
        return SIMPLE.get(g, g)
    return ESC.sub(one, body)


def typed_lines(path):
    """(cwd, session id, counts, [(line number, text)]) of one rollout."""
    cwd, sid = "", ""
    counts = {"write_stdin calls": 0, "polls": 0, "typed": 0, "typed, not a literal": 0, "exec_command": 0, "apply_patch": 0}
    typed = []
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        for n, line in enumerate(fh, 1):
            try:
                d = json.loads(line)
            except Exception:
                continue
            p = d.get("payload") if isinstance(d.get("payload"), dict) else {}
            if d.get("type") == "session_meta":
                cwd, sid = str(p.get("cwd") or ""), str(p.get("id") or "")
                continue
            if p.get("type") != "custom_tool_call":
                continue
            s = p.get("input") or ""
            s = s if isinstance(s, str) else json.dumps(s)
            for m in CALL.finditer(s):
                if m.group(1) != "write_stdin":
                    counts[m.group(1)] += 1
                    continue
                counts["write_stdin calls"] += 1
                seg = s[m.end():m.end() + 20000]
                nxt = CALL.search(seg)
                if nxt:
                    seg = seg[:nxt.start()]
                lit = CHARS_LIT.search(seg)
                if lit:
                    text = unescape(lit.group(1)[1:-1])
                    if "".join(ch for ch in text if ch >= " ").strip():
                        counts["typed"] += 1
                        typed.append((n, text.strip("\r\n")))
                    else:
                        counts["polls"] += 1
                elif CHARS_ANY.search(seg):
                    counts["typed, not a literal"] += 1
                else:
                    counts["polls"] += 1
    return cwd, sid, counts, typed


def ask_guard(guard, cwd, sid, text):
    """('deny' | 'block' | 'exit2' | '', reason) from one guard for one typed text."""
    payload = {"session_id": "typed-audit-" + (sid or "x"), "hook_event_name": "PreToolUse", "cwd": cwd or os.getcwd(),
               "model": "", "tool_name": "Bash", "tool_input": {"command": text}}
    try:
        r = subprocess.run([sys.executable, "-B", guard], input=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120,
                           creationflags=0x08000000 if os.name == "nt" else 0)
    except Exception as e:
        return "guard did not answer", repr(e)[:160]
    out = r.stdout.decode("utf-8", "replace").strip()
    if r.returncode == 2:
        return "exit2", r.stderr.decode("utf-8", "replace")[:300]
    try:
        o = json.loads(out) if out else {}
    except Exception:
        return "", ""
    hso = o.get("hookSpecificOutput") if isinstance(o.get("hookSpecificOutput"), dict) else {}
    if hso.get("permissionDecision") == "deny":
        return "deny", str(hso.get("permissionDecisionReason") or "")[:300]
    if o.get("decision") == "block":
        return "block", str(o.get("reason") or "")[:300]
    return "", ""


def main(argv):
    quiet = "--quiet" in argv
    guards, files, out_json = [], [], None
    it = iter([a for a in argv if a != "--quiet"])
    for a in it:
        if a == "--guard":
            guards.append(next(it, ""))
        elif a == "--json":
            out_json = next(it, None)
        else:
            files.append(a)
    if not guards:
        guards = [os.path.expanduser("~/.claude/dreaming/codex_help_guard_hook.py")]
    if not files or not all(os.path.isfile(f) for f in files) or not all(os.path.isfile(g) for g in guards):
        print("usage: codex_typed_audit.py <rollout.jsonl> [...] [--guard hook.py] [--quiet] [--json out]  (a file was not found)")
        return 1
    report, refused_all, unanswered = [], 0, 0
    for f in files:
        cwd, sid, counts, typed = typed_lines(f)
        refused = []
        for n, text in typed:
            for g in guards:
                kind, reason = ask_guard(g, cwd, sid, text)
                if kind == "guard did not answer":
                    unanswered += 1
                elif kind:
                    refused.append({"rollout_line": n, "guard": os.path.basename(g), "kind": kind, "reason": reason,
                                    "typed_start": text[:60]})
        refused_all += len(refused)
        report.append({"rollout": f, "cwd": cwd, "counts": counts, "refused": refused})
        print("%s: write_stdin calls %d = polls %d + typed %d + typed but not a literal %d; own commands %d, patches %d; "
              "typed lines the guard would have refused: %d" % (os.path.basename(f)[:60], counts["write_stdin calls"],
              counts["polls"], counts["typed"], counts["typed, not a literal"], counts["exec_command"], counts["apply_patch"], len(refused)))
        for r in refused:
            print("   line %d  %s %s: %s%s" % (r["rollout_line"], r["guard"], r["kind"], r["reason"][:170].replace("\n", " "),
                  "" if quiet else "   | typed: " + r["typed_start"]))
        if counts["typed, not a literal"]:
            print("   NOT READ: %d typed text(s) were built at run time and could not be checked" % counts["typed, not a literal"])
    if unanswered:
        print("WARNING: the guard did not answer %d time(s); those lines are unchecked" % unanswered)
    if out_json:
        io.open(out_json, "w", encoding="utf-8").write(json.dumps(report, indent=1, ensure_ascii=False))
    return 4 if refused_all else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
