# -*- coding: utf-8 -*-
"""Loop rewake: wake an idle session whose /loop has nothing left to fire it (owner, 11 Nov 2026 07:07: "sometimes after
a compaction agents get stuck, and the loop does not start, make sure to fix this").

loop_keeper.py can only speak when a hook event happens: it blocks a Stop and prints a line after a compaction. It cannot
reach the three stalls that have no event at all:
- a manual /compact starts no turn and no Stop; with no cron and no wakeup pending the session sits until he types;
- a tick that dies before it ends (an API error, a limit, an interrupt) never re-arms ScheduleWakeup and fires no Stop;
- a wakeup that is recorded as pending but does not fire.

This script is wired as an asyncRewake hook (Claude Code runs it in the background and, when it exits with code 2, hands
its stderr to the model as a new turn) on SessionStart and Stop. One watcher lives per session. Every CYCLE seconds it
looks at the transcript; when the session has been quiet long enough for its last record (a finished turn or a
compaction: GRACE; a turn that looks unfinished: MIDTURN) it reads the loop's state with loop_keeper's own scanner and
wakes the model when
  lapsed   the last ScheduleWakeup's time passed OVERDUE seconds ago (it fired and the tick did not
           re-arm, or it never fired) and no cron is alive                                    (up to 3 wakes a lapse)
  none    the session ran a loop, none is armed (cron deleted or expired, process restarted)
           and checklist entries under its id stay open                                       (one wake per set)
  cron     a cron is alive but the session has been quiet for CRON_QUIET seconds              (one wake)
It never wakes a session that never ran a loop, one whose loop was stopped with ScheduleWakeup stop:true, or one whose
wakeup or cron is still to come. Its own state is ~/.claude/compact_hooks/loop_rewake/<sid>.json (loop_keeper's state
file is only read, for the process start). Wakes are logged to ~/.claude/brain_graph/compactions/loop_rewake_fires.jsonl.
A file <sid>.force holding a number of seconds makes the next watcher wake after that long (a test of the wake path).
Silent on any error; prints nothing on stdout."""
import io
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
HOME = os.path.expanduser("~")
STATE_DIR = os.environ.get("LOOP_REWAKE_STATE") or os.path.join(HOME, ".claude", "compact_hooks", "loop_rewake")
FIRES = os.environ.get("LOOP_REWAKE_FIRES") or os.path.join(HOME, ".claude", "brain_graph", "compactions",
                                                             "loop_rewake_fires.jsonl")


def _num(name, default):
    try:
        return float(os.environ.get(name, default))
    except ValueError:
        return float(default)


CYCLE = _num("LOOP_REWAKE_CYCLE", 20)            # seconds between looks
GRACE = _num("LOOP_REWAKE_GRACE", 180)           # quiet after a finished turn or a compaction before a wake
MIDTURN = _num("LOOP_REWAKE_MIDTURN", 1500)      # quiet after a record that looks mid-turn (a tool running, a reply due)
OVERDUE = _num("LOOP_REWAKE_OVERDUE", 300)       # a pending wakeup this late has not fired
CRON_QUIET = _num("LOOP_REWAKE_CRON_QUIET", 2700)
MAX_LIFE = _num("LOOP_REWAKE_MAX_LIFE", 6000)    # the hook's timeout in settings.json is 6300
BACKOFF = (0, 600, 1800)                         # wait before the 1st, 2nd, 3rd wake of one lapse, after the quiet time
TAIL = 3 * 1024 * 1024


def load(sid):
    try:
        with io.open(os.path.join(STATE_DIR, sid + ".json"), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def save(sid, st):
    os.makedirs(STATE_DIR, exist_ok=True)
    p = os.path.join(STATE_DIR, sid + ".json")
    tmp = "%s.%d.tmp" % (p, os.getpid())
    with io.open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(st))
    os.replace(tmp, p)


def last_shape(path):
    """What the newest meaningful transcript record looks like: ended | compacted | midturn."""
    try:
        size = os.path.getsize(path)
        with open(path, "rb") as fh:
            fh.seek(max(0, size - TAIL))
            blob = fh.read()
    except OSError:
        return "midturn"
    lines = blob.split(b"\n")
    if size > TAIL:
        lines = lines[1:]
    for line in reversed(lines):
        if not line.strip():
            continue
        head = line[:1500]
        if b'"subtype":"compact_boundary"' in line or b'"isCompactSummary":true' in head:
            return "compacted"
        if b'"type":"assistant"' in line and b'"role":"assistant"' in line:
            if b'"stop_reason":"end_turn"' in line or b'"stop_reason":"stop_sequence"' in line:
                return "ended"
            return "midturn"
        if b'"type":"user"' in head and b'"role":"user"' in line:
            if b"<local-command-" in line[:4000] or b"<command-name>" in line[:4000]:
                continue                       # a slash command he ran (/compact, /effort): no turn follows it
            return "midturn"
    return "midturn"


def wake_reason(K, sid, st, kst, quiet, shape, now):
    """(key, limit, text) when the session should be woken now, else None."""
    st["proc_start"] = kst.get("proc_start") or st.get("proc_start") or 0
    word, detail = K.armed(st, now)
    if word == "stopped":
        return None
    w = st.get("wake") or {}
    prompt = (w.get("prompt") or "the same /loop prompt as before")[:200]
    rearm = ("Re-arm the loop before this turn ends: ScheduleWakeup with the same prompt (%s), or CronCreate at its "
             "cadence; a recurring cron survives a compaction and a failed tick, a wakeup does not. If the loop is "
             "finished on purpose, call ScheduleWakeup with stop:true and say so in one line." % prompt)
    since = time.strftime("%H:%M", time.localtime(now - quiet))
    how = "was compacted and no turn followed" if shape == "compacted" else (
        "stopped part-way through a turn" if shape == "midturn" else "ended its turn")
    lead = "[loop-keeper wake] This session %s at %s and has been idle since" % (how, since)
    tail = " Pick the work up from your NEXT line and do the next step now. If you are in the middle of a turn, ignore this."
    if word == "cron":
        if quiet < CRON_QUIET:
            return None
        return ("cron:%s" % detail, 1, "%s, though %s. Check it with CronList; if it is gone, create it again.%s"
                % (lead, detail, tail))
    if word == "wake":
        return None                            # still to come (loop_keeper calls it lapsed 90 s after its time)
    if word == "lapsed":
        due = w["at"] + w["delay"]
        if now - due < OVERDUE:
            return None                        # the fire itself may be a little late
        return ("lapse:%s" % w.get("at"), 3, "%s: its last wakeup was due at %s, nothing has been armed since and no "
                "cron is alive, so nothing will wake it. %s%s"
                % (lead, time.strftime("%H:%M", time.localtime(due)), rearm, tail))
    if not K.had_loop(st, now):
        return None
    rows = K.open_entries(sid)
    if not rows:
        return None
    listed = "; ".join("%s %s" % (e.get("id"), (e.get("working_on") or e.get("asked_words") or "")[:90]) for e in rows[:4])
    return ("none:%s" % ",".join(sorted(e.get("id", "") for e in rows)), 1,
            "%s. It ran a loop and none is armed now (its cron was deleted or expired, or the session restarted and "
            "lost it), yet these stay open under your id: %s. If his ask still runs, arm a loop now (CronCreate at the "
            "cadence he gave); if not, close or hand off those entries and say why in one line.%s" % (lead, listed, tail))


def allowed(st, key, limit, quiet, need, now):
    """The wake budget of one lapse: at most `limit` wakes, each later one after a longer quiet time."""
    past = [t for k, t in (st.get("wakes") or []) if k == key]
    if len(past) >= limit:
        return False
    return quiet >= need + BACKOFF[min(len(past), len(BACKOFF) - 1)]


def log(row):
    try:
        os.makedirs(os.path.dirname(FIRES), exist_ok=True)
        with io.open(FIRES, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(row) + "\n")
    except OSError:
        pass


def fire(sid, st, key, text):
    st["wakes"] = (list(st.get("wakes") or []) + [[key, time.time()]])[-40:]
    save(sid, st)
    log({"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "session_id": sid, "key": key, "text": text[:240]})
    sys.stderr.write(text + "\n")
    sys.stderr.flush()
    os._exit(2)


def headless(tpath):
    """True for a claude -p / SDK session (entrypoint sdk-cli, sdk-py, sdk-ts). Such a session has no /loop to keep alive,
    and its process does not exit while an async hook runs, so a watcher there only holds a finished worker open."""
    ep = os.environ.get("CLAUDE_CODE_ENTRYPOINT", "")
    if ep:
        return ep.startswith("sdk")          # desktop and IDE sessions carry their own values and can loop
    try:
        with io.open(tpath, encoding="utf-8", errors="replace") as fh:
            head = fh.read(65536)
    except OSError:
        return False
    return '"entrypoint":"sdk' in head.replace(" ", "")


def main():
    raw = sys.stdin.buffer.read().decode("utf-8", "replace")
    data = json.loads(raw) if raw.strip() else {}
    sid = data.get("session_id") or ""
    tpath = data.get("transcript_path") or ""
    if not sid or not tpath or data.get("hook_event_name") not in ("SessionStart", "Stop"):
        return
    if headless(tpath):
        return                    # claude -p waits for this watcher before it exits: a finished worker sat 100 min
    only = os.path.join(STATE_DIR, "ONLY_SESSIONS.txt")       # while it exists, only the sessions it lists are watched
    try:
        with io.open(only, encoding="utf-8") as fh:
            if sid not in fh.read():
                return
    except OSError:
        pass
    os.makedirs(STATE_DIR, exist_ok=True)
    alive = os.path.join(STATE_DIR, sid + ".alive")
    try:
        if time.time() - os.path.getmtime(alive) < max(75, 3 * CYCLE + 15):
            return                                            # this session's watcher is alive
    except OSError:
        pass
    me = str(os.getpid())
    with io.open(alive, "w", encoding="utf-8") as fh:
        fh.write(me)
    import loop_keeper as K
    born = time.time()
    st = load(sid)
    force = os.path.join(STATE_DIR, sid + ".force")
    try:
        with io.open(force, encoding="utf-8") as fh:
            wait = float(fh.read().strip() or 0)
        os.remove(force)
        time.sleep(max(0.0, wait))
        fire(sid, st, "forced:%d" % born, "[loop-keeper wake] Forced test wake, %d s after the %s event. Nothing is wrong; "
             "note the time it reached you and carry on." % (wait, data.get("hook_event_name")))
    except (OSError, ValueError):
        pass
    while time.time() - born < MAX_LIFE:
        time.sleep(CYCLE)
        try:
            with io.open(alive, encoding="utf-8") as fh:
                if fh.read().strip() != me:
                    return                                    # a newer watcher took this session
            os.utime(alive, None)
            quiet = time.time() - os.path.getmtime(tpath)
        except OSError:
            return
        if quiet < GRACE:
            continue
        shape = last_shape(tpath)
        need = MIDTURN if shape == "midturn" else GRACE
        if quiet < need:
            continue
        now = time.time()
        K.scan(tpath, st)
        why = wake_reason(K, sid, st, K.load(sid), quiet, shape, now)
        save(sid, st)
        if why and allowed(st, why[0], why[1], quiet, need, now):
            try:
                os.remove(alive)
            except OSError:
                pass
            fire(sid, st, why[0], why[2])
    try:
        os.remove(alive)
    except OSError:
        pass


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
