"""Send a hook's standing text once per context, then only what changed (an agent, 4 Nov 2026).

Measured on 24 h of dispatcher overflow files (brain_improvement/hook_repeat_fb45/measure_overflow.py): most hook
text is the same paragraph re-sent on every prompt to a session that already has it - waste_sense 1,926 chars a
fire, 95 pct repeated. A context keeps what it was told until a compaction, so a standing paragraph needs to go
whole once per context (again after a compaction or after `resend` seconds) and otherwise not at all.

    from once_per_context import filter_lines
    out, whole, at = filter_lines(session_id, "waste_sense", lines, keep=lambda l: l.startswith("  - pid"))

Lines are keyed with their digits masked, so a census count that moved does not count as new text. `keep` names
lines that always go (the live part). Any doubt (no session, unreadable state or compaction index) sends it whole.
ONCE_PER_CONTEXT_OFF=1 turns it off for every hook.
"""
import datetime
import hashlib
import io
import json
import os
import re
import threading
import time

STATE = os.path.join(os.path.expanduser("~"), ".claude", "dreaming", "state", "once_per_context.json")
COMPACTION_INDEX = os.path.expanduser("~/.claude/brain_graph/compactions/INDEX.jsonl")


def last_compaction_at(sess):
    """Epoch of this session's newest compaction in the brain's compaction index (0 = none, None = unreadable)."""
    try:
        with open(COMPACTION_INDEX, "rb") as f:
            f.seek(0, 2)
            n = f.tell()
            f.seek(max(0, n - 262144))
            tail = f.read().decode("utf-8", "replace")
    except Exception:
        return None
    best = 0.0
    for line in tail.splitlines():
        if sess not in line:
            continue
        try:
            o = json.loads(line)
            if o.get("session_id") == sess:
                best = max(best, datetime.datetime.fromisoformat(o["at"]).timestamp())
        except Exception:
            continue
    return best


def _key(line):
    return hashlib.md5(re.sub(r"\d+", "#", line).encode("utf-8")).hexdigest()[:12]


STATE_DIR = os.path.join(os.path.dirname(STATE), "once_per_context")
SAVE_WAIT_S = 0.5
SWEEP_EVERY_S = 3600
KEEP_S = 86400


def _state_path(name, sess):
    """One file per (hook, session): no other hook or session ever opens it."""
    safe = lambda s, n: re.sub(r"[^A-Za-z0-9_.-]", "_", str(s))[:n]
    tag = hashlib.md5(("%s|%s" % (name, sess)).encode("utf-8")).hexdigest()[:10]
    return os.path.join(STATE_DIR, "%s__%s__%s.json" % (safe(name, 40), safe(sess, 60), tag))


def _load_prev(name, sess, now):
    """(entry or None, came_from_the_shared_file). An unreadable entry counts as none: the text goes whole."""
    try:
        with io.open(_state_path(name, sess), encoding="utf-8") as f:
            v = json.load(f)
        return (v if isinstance(v, dict) else None), False
    except FileNotFoundError:
        pass
    except Exception:
        return None, False
    # Before 11 Nov 2026 every key lived in the one shared file; read it, never write it, so the switch sends
    # nothing whole that this context already has.
    try:
        with io.open(STATE, encoding="utf-8") as f:
            v = json.load(f).get(name + "|" + sess)
        if isinstance(v, dict) and now - v.get("at", 0) < KEEP_S:
            return v, True
    except Exception:
        pass
    return None, False


def _save(path, entry):
    """Write the entry through a temp of our own and move it in. Never raises, never leaves the temp."""
    tmp = "%s.%d.%d.tmp" % (path, os.getpid(), threading.get_ident())
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with io.open(tmp, "w", encoding="utf-8") as f:
            json.dump(entry, f)
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


def _sweep(now):
    """At most once an hour: drop entries untouched for a day and temps a crash left behind."""
    mark = os.path.join(STATE_DIR, ".swept")
    try:
        if now - os.path.getmtime(mark) < SWEEP_EVERY_S:
            return
    except OSError:
        pass
    try:
        with io.open(mark, "w", encoding="utf-8") as f:
            f.write("%d" % now)
        for e in os.scandir(STATE_DIR):
            try:
                if not e.is_file() or e.name == ".swept":
                    continue
                age = now - e.stat().st_mtime
                if (e.name.endswith(".json") and age > KEEP_S) or (e.name.endswith(".tmp") and age > 600):
                    os.remove(e.path)
            except OSError:
                continue
    except Exception:
        pass


def filter_lines(sess, name, lines, keep=None, resend=3 * 3600):
    """Return (lines to send, sent_whole, epoch the whole text last went)."""
    now = time.time()
    if not sess or os.environ.get("ONCE_PER_CONTEXT_OFF"):
        return list(lines), True, now
    keys = [_key(l) for l in lines]
    prev, migrated = _load_prev(name, sess, now)
    comp = last_compaction_at(sess)
    whole = (not prev or comp is None or comp >= prev.get("at", 0) - 5 or now - prev.get("at", 0) > resend)
    if whole:
        entry = {"at": now, "keys": keys}
        out, at = list(lines), now
        dirty = True
    else:
        old = list(prev.get("keys", []))
        seen = set(old)
        out = [l for l, k in zip(lines, keys) if (keep and keep(l)) or (k not in seen and l.strip())]
        fresh = [k for k in dict.fromkeys(keys) if k not in seen]
        at = prev.get("at", now)
        entry = {"at": at, "keys": (old + fresh)[-4000:]}
        dirty = bool(fresh) or migrated
    if dirty:
        _save(_state_path(name, sess), entry)
    _sweep(now)
    return out, whole, at
