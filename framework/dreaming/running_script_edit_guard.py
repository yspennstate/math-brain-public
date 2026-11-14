#!/usr/bin/env python3
"""running_script_edit_guard.py - refuse an in-place edit of a shell script that a live bash is executing.

PreToolUse on Edit, Write, MultiEdit (a .sh / .bash path) and Bash / PowerShell (sed -i, a > or >> redirect, tee,
or cp onto a .sh path). bash reads a script by byte offset as it runs, so an edit that shifts the bytes makes it
resume mid-line: the rest of the run is skipped or garbled. Scar: 29 Oct push_lane13 (rc 127, push never ran) and
11 Nov rerun_arm.sh (two grand-hunt reruns lost session 2 to a syntax error after session 1); memory
editing_a_running_bash_script_shifts_its_lines_2026_10_30. The brain held the scar; nothing fired at the edit.

Decision: a bash / sh process whose command line runs the same file (bash <file>, sh <file>, source <file>,
. <file>, also inside bash -c "...") -> deny, with the way out (copy, edit the copy, mv it into place: a rename
leaves the running bash on the old file). Same file name but the path cannot be resolved -> a warning only.
Silent and fail-open on any error; about 0.1 s (psutil, bash processes only).
"""
import json
import os
import re
import shlex
import sys

SH_EXT = (".sh", ".bash")
RUNNERS = {"bash", "sh", "bash.exe", "sh.exe", "source", ".", "dash", "zsh"}


def norm(p, cwd=None):
    p = p.strip("\"'")
    # Git Bash spellings: ~ is home, /tmp is the Windows temp folder, /c/... is C:/...
    if p.startswith("~"):
        p = os.path.expanduser(p)
    elif p == "/tmp" or p.startswith("/tmp/"):
        tmp = os.environ.get("TEMP") or os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp")
        p = tmp + p[4:]
    m = re.match(r"^/([a-zA-Z])(/.*)?$", p)
    if m:
        p = m.group(1).upper() + ":" + (m.group(2) or "/")
    if not re.match(r"^[a-zA-Z]:[\\/]", p):
        if not cwd:
            return None
        p = os.path.join(cwd, p)
    return os.path.normcase(os.path.normpath(p))


def run_targets(argv):
    """Paths this command line runs as a script: the word after bash/sh/source/. (flags skipped), also inside -c."""
    out = []
    words = list(argv)
    i = 0
    while i < len(words):
        w = words[i]
        base = os.path.basename(w.replace("\\", "/")).lower()
        if base in RUNNERS:
            j = i + 1
            while j < len(words) and words[j].startswith("-"):
                if words[j] == "-c" and j + 1 < len(words):
                    try:
                        inner = shlex.split(words[j + 1], posix=True)
                    except ValueError:
                        inner = words[j + 1].split()
                    # split on shell separators so 'a; bash x.sh' is seen
                    flat = []
                    for t in inner:
                        flat.extend(x for x in re.split(r"[;&|()]+", t) if x)
                    out.extend(run_targets(flat))
                    j += 1
                j += 1
            if j < len(words) and words[j].lower().endswith(SH_EXT):
                out.append(words[j])
            i = j
        i += 1
    return out


def _psutil():
    # The hooks run as `python -s`, which hides the user site where psutil lives. Without this the import failed,
    # the guard failed open in silence and let a live edit through (11 Nov first live test; the unit tests ran plain
    # python and passed). Same remedy as math_sense._ensure_user_site.
    try:
        import psutil
        return psutil
    except ModuleNotFoundError:
        import site
        usp = site.getusersitepackages()
        if usp and os.path.isdir(usp) and usp not in sys.path:
            sys.path.append(usp)
        import psutil
        return psutil


def running_on(target):
    """(exact pids, name-only pids) of live bash processes running `target`."""
    psutil = _psutil()
    want = norm(target)
    name = os.path.basename(target.replace("\\", "/")).lower()
    me = {os.getpid()}
    try:
        me.update(p.pid for p in psutil.Process().parents())
    except Exception:
        pass
    exact, loose = [], []
    for p in psutil.process_iter(["name"]):
        n = (p.info.get("name") or "").lower()
        if n not in ("bash.exe", "sh.exe", "bash", "sh", "dash.exe") or p.pid in me:
            continue
        try:
            argv = p.cmdline()
        except Exception:
            continue
        for t in run_targets(argv):
            if os.path.basename(t.strip("\"'").replace("\\", "/")).lower() != name:
                continue
            try:
                cwd = p.cwd()
            except Exception:
                cwd = None
            r = norm(t, cwd)
            if r and want and r == want:
                exact.append(p.pid)
            else:
                loose.append(p.pid)
            break
    return exact, loose


def bash_write_targets(cmd):
    """.sh paths a shell command would rewrite in place (sed -i, > / >>, tee, cp onto)."""
    t = set()
    for m in re.finditer(r"(?:>>?|\btee(?:\s+-a)?)\s*([^\s;&|<>]+\.(?:sh|bash))\b", cmd):
        t.add(m.group(1))
    for m in re.finditer(r"\bsed\s+(?:-[a-zA-Z]*i[a-zA-Z]*|--in-place)\S*\s[^;&|]*?([^\s;&|'\"]+\.(?:sh|bash))\b", cmd):
        t.add(m.group(1))
    for m in re.finditer(r"\bcp\s+(?:-\S+\s+)*\S+\s+([^\s;&|]+\.(?:sh|bash))\s*(?:$|[;&|])", cmd):
        t.add(m.group(1))
    return [x.strip("\"'") for x in t]


def main():
    raw = getattr(sys.stdin, "buffer", sys.stdin).read()
    ev = json.loads(raw.decode("utf-8", "surrogateescape") if isinstance(raw, bytes) else raw)
    tool = ev.get("tool_name") or ""
    ti = ev.get("tool_input") or {}
    if tool in ("Edit", "Write", "MultiEdit"):
        targets = [ti.get("file_path") or ""]
    elif tool in ("Bash", "PowerShell"):
        cmd = ti.get("command") or ""
        if ".sh" not in cmd and ".bash" not in cmd:
            return
        targets = bash_write_targets(cmd)
    else:
        return
    targets = [t for t in targets if t.lower().endswith(SH_EXT)]
    if not targets:
        return
    for t in targets:
        if tool in ("Edit", "Write", "MultiEdit") and not os.path.exists(t):
            continue
        exact, loose = running_on(t)
        if exact:
            reason = ("RUNNING SCRIPT: %s is being executed right now by bash pid %s. bash reads a script by byte "
                      "offset as it runs, so editing it in place makes the run resume mid-line and skip or garble the "
                      "rest (29 Oct push_lane13; 11 Nov rerun_arm.sh lost session 2 of two hunt reruns). Copy it, edit "
                      "the copy, then mv the copy over it (a rename leaves the running bash on the old file), or wait "
                      "for the run to end. Memory editing_a_running_bash_script_shifts_its_lines_2026_10_30."
                      % (t, ", ".join(map(str, exact[:5]))))
            sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                                "permissionDecision": "deny",
                                                                "permissionDecisionReason": reason}}))
            return
        if loose:
            msg = ("[running-script] a bash process (pid %s) runs a script named %s; if it is this file, editing it "
                   "in place garbles that run (bash reads by byte offset): copy, edit, mv into place instead."
                   % (", ".join(map(str, loose[:5])), os.path.basename(t)))
            sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                                "additionalContext": msg}}))
            return


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # still fail open, but leave a trace: a guard that dies quietly reads as a guard that found nothing
        try:
            import time
            import traceback
            log = os.path.join(os.path.dirname(os.path.abspath(__file__)), "running_script_edit_guard.err")
            if not os.path.exists(log) or os.path.getsize(log) < 200000:
                with open(log, "a", encoding="utf-8") as f:
                    f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + traceback.format_exc() + "\n")
        except Exception:
            pass
