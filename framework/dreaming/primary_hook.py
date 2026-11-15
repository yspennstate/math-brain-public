# -*- coding: utf-8 -*-
"""THE PRIMARY HOOK (his PRIMARY DIRECTIVE, dictated 6 Oct 2026, 18:0x-18:4x local time, transcript segment 8).

Written at the author's request.

What it does: on every prompt of every Claude and Codex session on this machine (they are all connected to the brain),
prints his line once per session per three minutes. Nothing else: it never blocks, never edits, swallows its own
exceptions, and its output is ASCII so no capture layer can choke on it. One switch turns it off for everyone:
~/.claude/dreaming/PRIMARY_HOOK_OFF (his word only). State: one file per session under primary_hook_state.json.d beside this file.

    python primary_hook.py                     Claude (the dispatcher runs it in-process; plain text is appended)
    python primary_hook.py --runtime codex     Codex (JSON hookSpecificOutput; Codex discards plain stdout)
    python primary_hook.py --selftest          four controls on a temporary state file; the live state is untouched
"""
import hashlib
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "primary_hook_state.json")
OFF = os.path.join(HERE, "PRIMARY_HOOK_OFF")
EVERY_S = 180
LINE = ("[primary-hook] Work faster, be more efficient, finish the job faster. The timeline is soon. Communicate faster, "
        "build faster, give a deliverable: agents are waiting on you. Find the nearest bottleneck and clear it; speed "
        "things up. Focus on what you are supposed to do and finish your deliverable. (His PRIMARY DIRECTIVE of 6 Oct "
        "2026, for every agent on the brain or the math brain; repeats every three minutes.) SAVE AS YOU GO (his order, "
        "7 Oct 02:44-03:0x): write every result to disk the moment you have it and keep a NEXT line current, so a "
        "crash never costs more than ten minutes of work; a headless session you launch gets its id at launch "
        "(claude --session-id / the codex thread id) and is resumed in that session after a crash, never restarted cold.")


def session_key(payload):
    for k in ("session_id", "sessionId", "thread_id", "conversation_id"):
        v = payload.get(k) if isinstance(payload, dict) else None
        if v:
            return str(v)[:64]
    for k in ("CODEX_THREAD_ID", "CODEX_SESSION_ID", "CLAUDE_SESSION_ID"):
        if os.environ.get(k):
            return os.environ[k][:64]
    return "pid%s:%s" % (os.getppid(), (payload.get("cwd") if isinstance(payload, dict) else "") or os.getcwd())


SAVE_WAIT_S = 0.3
SWEEP_EVERY_S = 3600


def _session_file(state_path, key):
    """One state file per session: "<session>", "<session>|clock", "<session>|dh7" ... all live in it, and no
    other session ever opens it (11 Nov 2026: the one shared file lost fires to refused moves and to lost updates)."""
    sess = key.split("|", 1)[0]
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", sess)[:60]
    return os.path.join(state_path + ".d", "%s__%s.json" % (safe, hashlib.md5(sess.encode("utf-8")).hexdigest()[:10]))


def _load_session(path, state_path, key):
    """(this session's entries, came_from_the_shared_file)."""
    for attempt in (0, 1, 2):
        try:
            with io.open(path, encoding="utf-8") as f:
                st = json.load(f)
            return (st if isinstance(st, dict) else {}), False
        except FileNotFoundError:
            break
        except PermissionError:
            time.sleep(0.02)
        except Exception:
            return {}, False
    else:
        return {}, False
    # Before 11 Nov 2026 every session lived in the one shared file: read it, never write it.
    try:
        sess = key.split("|", 1)[0]
        with io.open(state_path, encoding="utf-8") as f:
            shared = json.load(f)
        got = {k: v for k, v in shared.items() if k == sess or k.startswith(sess + "|")}
        return got, bool(got)
    except Exception:
        return {}, False


def _save_session(path, st):
    """Temp of our own, a move that waits out a reader, never raises, never leaves the temp."""
    tmp = path + ".%d.tmp" % os.getpid()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with io.open(tmp, "w", encoding="utf-8") as f:
            json.dump(st, f)
        end = time.time() + SAVE_WAIT_S
        pause = 0.02
        while True:
            try:
                os.replace(tmp, path)
                return True
            except PermissionError:
                if time.time() >= end:
                    return False
                time.sleep(pause)
                pause = min(pause * 2, 0.1)
    except Exception:
        return False
    finally:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except OSError:
            pass


def _sweep(folder):
    """At most once an hour: drop session files untouched for a day and temps a killed hook left."""
    real = time.time()
    mark = os.path.join(folder, ".swept")
    try:
        if real - os.path.getmtime(mark) < SWEEP_EVERY_S:
            return
    except OSError:
        pass
    try:
        with io.open(mark, "w", encoding="utf-8") as f:
            f.write("%d" % real)
        for e in os.scandir(folder):
            try:
                if not e.is_file() or e.name == ".swept":
                    continue
                age = real - e.stat().st_mtime
                if (e.name.endswith(".json") and age > 86400) or (e.name.endswith(".tmp") and age > 600):
                    os.remove(e.path)
            except OSError:
                continue
    except Exception:
        pass


def due(key, now, state_path=STATE, every=EVERY_S):
    """True once per key per `every` seconds; records the fire. Entries older than a day are dropped so the file stays small."""
    path = _session_file(state_path, key)
    st, moved = _load_session(path, state_path, key)
    last = st.get(key)
    if isinstance(last, (int, float)) and now - last < every:
        if moved:
            _save_session(path, st)
        return False
    st = {k: v for k, v in st.items() if isinstance(v, (int, float)) and now - v < 86400}
    st[key] = now
    _save_session(path, st)
    _sweep(state_path + ".d")
    return True


# THE PRIME DIRECTIVE HOOK (his 7 Oct 20:4x order, "and write a prime directive hook as well"): the directive's own
# rules, fired by what the prompt is about (test material, credits, fleet size, store writes, the timeline ...), each at
# most once per session per 45 minutes and at most two a prompt, plus a stage clock once per session per hour. Rules and
# selector: ~/primary_directive/directive_hooks (DIRECTIVE_HOOKS_v1.jsonl, directive_hooks.py --selftest).
DH_DIR = r"~\primary_directive\directive_hooks"
RULE_EVERY_S = 2700
CLOCK_EVERY_S = 3600


def directive_lines(key, text, now, state_path=STATE):
    try:
        if DH_DIR not in sys.path:
            sys.path.insert(0, DH_DIR)
        import directive_hooks as dh
        out = []
        # the clock counts the 6-16 Oct directive; past its END it would print "Day 35 of the ten", so it stays quiet
        if text and now < getattr(dh, "END", float("inf")) and dh.CONTEXT.search(text) and due(key + "|clock", now, state_path, CLOCK_EVERY_S):
            out.append(dh.clock_line(now))
        for r in dh.select(text, k=4):
            if len(out) >= 3:
                break
            if due("%s|dh%s" % (key, r.get("n")), now, state_path, RULE_EVERY_S):
                out.append(dh.render([r]))
        return out
    except Exception:
        return []


# THE USAGE WATCH (his 7 Oct 22:3x order: "you should have been paying closer attention to this, make a hook about it"):
# the Claude meters, the directive fleet's last hour and this session's own re-read per turn (usage_watch.py beside this
# file, --selftest). Measured at most once per session per 5 minutes, said at most once per 30, only when something is off.
USAGE_CHECK_S = 300
USAGE_EVERY_S = 1800


def usage_lines(key, payload, now, state_path=STATE):
    try:
        if not due(key + "|usage_check", now, state_path, USAGE_CHECK_S):
            return []
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import usage_watch
        got = usage_watch.lines(payload, now)
        if got and due(key + "|usage", now, state_path, USAGE_EVERY_S):
            return got
        return []
    except Exception:
        return []


def emit(runtime, lines=None):
    text = "\n".join(lines if lines is not None else [LINE])
    if not text:
        return
    if runtime == "codex":
        sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                                            "additionalContext": text}}) + "\n")
    else:
        sys.stdout.write(text + "\n")
    sys.stdout.flush()


def main(argv):
    runtime = "codex" if "--runtime" in argv and argv[argv.index("--runtime") + 1:argv.index("--runtime") + 2] == ["codex"] else "claude"
    if "--selftest" in argv:
        return selftest()
    try:
        if os.path.exists(OFF):
            return 0
        raw = ""
        try:
            if not sys.stdin.isatty():
                raw = sys.stdin.read()
        except Exception:
            raw = ""
        try:
            payload = json.loads(raw) if raw.strip() else {}
        except Exception:
            payload = {}
        key, now = session_key(payload), time.time()
        lines = [LINE] if due(key, now) else []
        prompt = payload.get("prompt") if isinstance(payload, dict) else ""
        lines += directive_lines(key, prompt if isinstance(prompt, str) else "", now)
        lines += usage_lines(key, payload, now)
        if lines:
            emit(runtime, lines)
    except Exception:
        pass
    return 0


def selftest():
    import tempfile
    d = tempfile.mkdtemp()
    sp = os.path.join(d, "state.json")
    ok = True
    r1 = due("s1", 1000.0, sp)
    r2 = due("s1", 1100.0, sp)
    r3 = due("s2", 1100.0, sp)
    r4 = due("s1", 1181.0, sp)
    for name, got, want in (("first fire", r1, True), ("same session inside 3 min", r2, False),
                            ("another session", r3, True), ("same session after 3 min", r4, True)):
        print("%s  %s" % ("PASS " if got == want else "FAIL ", name))
        ok = ok and got == want
    codex = json.loads(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": LINE}}))
    print("%s  codex envelope carries the line" % ("PASS " if codex["hookSpecificOutput"]["additionalContext"] == LINE else "FAIL "))
    print("%s  line is ASCII (%d chars)" % ("PASS " if all(ord(c) < 128 for c in LINE) else "FAIL ", len(LINE)))
    print("PASS - primary hook controls" if ok else "FAIL - primary hook controls")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
