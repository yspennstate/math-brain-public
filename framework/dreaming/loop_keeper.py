# -*- coding: utf-8 -*-
"""Loop keeper: a session's /loop must stay armed across compactions (owner, 11 Nov 2026 03:13: "keep working full time,
also sometimes after a compact the agent does not start working again like the loop gets stuck, fix it").

What stops a loop (measured on an agent, 11 Nov):
- A self-paced /loop lives only as long as each turn re-arms ScheduleWakeup. A turn that ends without re-arming (often the
  turn after an automatic compaction, which ends on a recap) leaves nothing to wake the session, forever.
- A manual /compact starts no turn and no Stop event, so keep_working_after_compact.py never runs; the session resumes only
  when a cron or wakeup fires. If none is alive (the loop ended at its clock, expired after 7 days, or died when the session
  restarted - crons and wakeups live in the process), it sits idle until he types.

Two events, Claude Code only (Codex has no cron or wakeup):
- Stop: if this session ran a loop (a cron or a ScheduleWakeup in its transcript) and now nothing is armed - no live cron,
  no wakeup still pending, no ScheduleWakeup stop - block once per lapse and tell it to re-arm (or stop the loop with
  ScheduleWakeup stop:true / say why). Also once when its loop ended while checklist entries under its id are still open.
- SessionStart: on startup/resume record the process start (older crons and wakeups are dead); on compact print one line
  with the loop's state, so the turn after the compaction knows whether it must re-arm.
State per session in ~/.claude/compact_hooks/loop_keeper/<sid>.json (incremental transcript offset). Fires logged to
~/.claude/brain_graph/compactions/loop_keeper_fires.jsonl. Silent on any error; never blocks while stop_hook_active twice
for the same lapse."""
import io
import json
import os
import re
import sys
import time
from datetime import datetime

HOME = os.path.expanduser("~")
STATE_DIR = os.environ.get("LOOP_KEEPER_STATE") or os.path.join(HOME, ".claude", "compact_hooks", "loop_keeper")
FIRES = os.environ.get("LOOP_KEEPER_FIRES") or os.path.join(HOME, ".claude", "brain_graph", "compactions",
                                                              "loop_keeper_fires.jsonl")
CHECKLIST = os.path.join(HOME, "brain-repo", "12_cognitive_architecture", "task_checklist", "state.json")
FIRST_TAIL = 40 * 1024 * 1024   # first sight of a session: scan its last 40 MB only
CRON_LIFE = 7 * 86400
LOOP_MEMORY = 24 * 3600          # a loop last armed more than a day ago is history, not a stalled loop
TS_RE = re.compile(rb'"timestamp":"([0-9T:\-\.]+)')
# Only CronCreate's own structured result carries this unescaped; a grep or a log that merely quotes the words
# "Scheduled recurring job <id>" (11 Nov: a deleted cron came back alive that way) is a JSON-escaped string.
JOB_RE = re.compile(rb'"toolUseResult":\{"id":"([0-9a-f]{6,12})","humanSchedule"')
DEL_RE = re.compile(rb'"name":"CronDelete","input":\{"id":"([0-9a-f]{6,12})"')
WAKE_RE = re.compile(rb'"name":"ScheduleWakeup","input":(\{.*?\})(?:,"caller"|\}\],|\},\{"type")')
CRON_IN_RE = re.compile(rb'"name":"CronCreate","input":\{"cron":"([^"]+)"')


def _ts(line):
    m = TS_RE.search(line)
    if not m:
        return None
    try:
        return datetime.fromisoformat(m.group(1).decode()[:19] + "+00:00").timestamp()
    except ValueError:
        return None


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


def scan(path, st):
    """Advance the state over the transcript bytes not read yet."""
    try:
        size = os.path.getsize(path)
    except OSError:
        return st
    off = st.get("offset")
    if off is None or off > size:
        off = max(0, size - FIRST_TAIL)
    crons = st.setdefault("crons", {})        # id -> [created_epoch, cron expr]
    with open(path, "rb") as fh:
        fh.seek(off)
        if off:
            fh.readline()                        # skip a partial line
        last_cron = None
        for line in fh:
            if b"Cron" not in line and b"ScheduleWakeup" not in line and b'"humanSchedule"' not in line:
                continue
            ts = _ts(line)
            if ts is None:
                continue
            m = CRON_IN_RE.search(line)
            if m:
                last_cron = m.group(1).decode("utf-8", "replace")
            for m in JOB_RE.finditer(line):
                crons[m.group(1).decode()] = [ts, last_cron or ""]
            for m in DEL_RE.finditer(line):
                crons.pop(m.group(1).decode(), None)   # created before the scanned tail still counts as ended
                st["ended_crons"] = (list(st.get("ended_crons") or []) + [[m.group(1).decode(), ts]])[-20:]
            for m in WAKE_RE.finditer(line):
                if b'"tool_use"' not in line:
                    continue
                try:
                    inp = json.loads(m.group(1).decode("utf-8", "replace"))
                except ValueError:
                    blob = m.group(1)
                    inp = {"stop": b'"stop":true' in blob}
                    d = re.search(rb'"delaySeconds":(\d+)', blob)
                    if d:
                        inp["delaySeconds"] = int(d.group(1))
                st["wake"] = {"at": ts, "stop": bool(inp.get("stop")), "delay": int(inp.get("delaySeconds") or 0),
                              "prompt": (inp.get("prompt") or st.get("wake", {}).get("prompt") or "")[:300]}
        st["offset"] = fh.tell()
    return st


def armed(st, now):
    """(state word, detail). word: cron | wake | stopped | lapsed | none."""
    born = st.get("proc_start") or 0
    live = {k: v for k, v in (st.get("crons") or {}).items() if v[0] >= born - 5 and now - v[0] < CRON_LIFE}
    if live:
        k = max(live, key=lambda k: live[k][0])
        return "cron", "cron %s (%s) alive" % (k, live[k][1] or "?")
    w = st.get("wake")
    if not w or w["at"] < born - 5:
        return "none", ""
    if w["stop"]:
        return "stopped", "loop stopped with ScheduleWakeup stop:true at %s" % time.strftime("%H:%M", time.localtime(w["at"]))
    due = w["at"] + w["delay"]
    if due > now - 90:                     # pending (90 s grace: the fire itself is this turn)
        return "wake", "wakeup pending, due %s" % time.strftime("%H:%M", time.localtime(due))
    if now - w["at"] > LOOP_MEMORY:
        return "none", ""
    return "lapsed", "last ScheduleWakeup fired at %s and was not re-armed" % time.strftime("%H:%M", time.localtime(due))


def had_loop(st, now):
    c = st.get("crons") or {}
    w = st.get("wake")
    ended = [e for e in (st.get("ended_crons") or []) if now - e[1] < LOOP_MEMORY]
    return bool(c or (w and now - w["at"] < LOOP_MEMORY) or ended)


def open_entries(sid):
    # 14 Nov 2026: a plain open held the 16.6 MB state.json without share-delete through the whole stdlib parse, on
    # every Stop of every looping session, and the checklist writer's rename failed while it did (hook.log: 191
    # 'replace gave up', each a lost checklist write). Read the bytes share-delete, close, then parse.
    try:
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from shared_read import open_shared
        except Exception:
            open_shared = lambda p, binary=False: io.open(p, "rb")
        with open_shared(CHECKLIST, binary=True) as fh:
            raw = fh.read()
        entries = json.loads(raw.decode("utf-8-sig")).get("entries") or {}
    except (OSError, ValueError, MemoryError):
        return []
    agent = "claude-" + sid[:8]
    rows = [e for e in (entries.values() if isinstance(entries, dict) else entries)
            if isinstance(e, dict) and e.get("agent") == agent and e.get("status") in ("open", "working")
            and sid.startswith(e.get("session") or sid[:8])]
    rows.sort(key=lambda e: e.get("asked_at") or "", reverse=True)
    return rows


def log(row):
    try:
        os.makedirs(os.path.dirname(FIRES), exist_ok=True)
        with io.open(FIRES, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(row) + "\n")
    except OSError:
        pass


def on_stop(data, sid, st, now):
    word, detail = armed(st, now)
    if word in ("cron", "wake", "stopped"):
        st.pop("blocked_for", None)
        return None
    if not had_loop(st, now):
        return None
    w = st.get("wake") or {}
    if word == "lapsed":
        key = "lapse:%s" % w.get("at")
        if st.get("blocked_for") == key:
            return None
        st["blocked_for"] = key
        prompt = w.get("prompt") or "(the same /loop prompt as before)"
        return ("[loop-keeper] Your /loop is no longer armed: %s, and no cron is alive, so nothing will wake this session "
                "again. Re-arm it now: ScheduleWakeup with the same prompt (%s), or a CronCreate at its cadence. If the "
                "loop's work or clock is finished, call ScheduleWakeup with stop:true and say so in one line." %
                (detail, prompt[:160]))
    # word == none: the session had a loop but none is armed (cron deleted or expired, or the process restarted)
    rows = open_entries(sid)
    if not rows:
        return None
    key = "none:%s" % ",".join(sorted(e.get("id", "") for e in rows))
    if st.get("blocked_for") == key:
        return None
    st["blocked_for"] = key
    listed = "; ".join("%s %s" % (e.get("id"), (e.get("working_on") or e.get("asked_words") or "")[:90]) for e in rows[:4])
    return ("[loop-keeper] This session ran a loop and none is armed now (its cron was deleted or expired, or the session "
            "restarted and lost it), yet these stay open under your id: %s. Nothing will wake you after a compaction or "
            "an idle stop. If his ask still runs, arm a loop now (CronCreate at the cadence he gave, re-running the tick) "
            "before you end the turn; if not, close or hand off those entries and say why in one line." % listed)


def main():
    raw = sys.stdin.buffer.read().decode("utf-8", "replace")
    data = json.loads(raw) if raw.strip() else {}
    ev = data.get("hook_event_name") or ""
    sid = data.get("session_id") or ""
    tpath = data.get("transcript_path") or ""
    if not sid:
        return
    now = time.time()
    st = load(sid)
    if ev == "SessionStart" and data.get("source") in ("startup", "resume", "clear"):
        st["proc_start"] = now                  # crons and wakeups from an earlier process are gone
        if tpath:
            scan(tpath, st)
        save(sid, st)
        return
    if not tpath:
        return
    scan(tpath, st)
    if ev == "SessionStart":                    # compact
        word, detail = armed(st, now)
        save(sid, st)
        if word == "cron" or word == "wake":
            sys.stdout.write("[loop-keeper] Your loop survived this compaction (%s). Do the next tick's step in this turn "
                             "if you have one; a recap is not a tick.\n" % detail)
        elif word == "lapsed" or (word == "none" and had_loop(st, now)):
            sys.stdout.write("[loop-keeper] This session ran a loop and NONE is armed now%s. Before this turn ends, re-arm "
                             "it (ScheduleWakeup with the same /loop prompt, or CronCreate at its cadence), or stop it on "
                             "purpose and say why.\n" % ((" (" + detail + ")") if detail else ""))
        return
    if ev == "Stop":
        reason = on_stop(data, sid, st, now)
        save(sid, st)
        if reason:
            log({"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "session_id": sid, "reason": reason[:200]})
            sys.stdout.write(json.dumps({"decision": "block", "reason": reason}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
