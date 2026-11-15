"""dream_health.py - one row per dream: did each part of it actually run?

    python dream_health.py              the last 14 dreams as a table, then the summary
    python dream_health.py --summary    the summary lines only (brain_status.py prints these)
    python dream_health.py --record     append a row for every finished dream not yet in dream_health.jsonl
    python dream_health.py --steps      every dream step: its last state, its seconds, when it last finished
    python dream_health.py --selftest

PRODUCER   this file, reading the dream's own logs (logs/dream_<stamp>.log), judged_nightly.jsonl,
           dream_methods_log.jsonl and dream_steps.jsonl (one row per step, written by RunPy in run_dream.ps1:
           stamp, step, seconds, exit, state ok / failed / capped / skipped_budget / skipped_stop / threw).
CONSUMER   brain_status.py (the DREAM block of the status page) and any agent asking whether the dream works.
FRESHNESS  rows are derived on demand from the logs; --record keeps a permanent row per dream in
           dream_health.jsonl (a dream is recorded once its log has been quiet for two hours).
FAILURE    a log that cannot be read gives a row with rem='unreadable'; an exception in the summary is caught
           by brain_status.py, which then prints its old one-line read.
TEST       --selftest builds three fixture logs (a clean night, a watchdog night with a stub journal, a night
           whose push was blocked) and checks every field.

A row: stamp, hours (start to 'dream cycle complete'), rem (ok / limit / watchdog / error / none), arm (the
model or login that finished the REM), journal (real / stub / missing / none), judged (rows written to
judged_nightly.jsonl during the dream), methods (candidates the methods section showed), persist (pushed /
local / aborted / blocked / deferred / none), commit, crashes (tracebacks in the log).
"""
import io
import json
import os
import re
import sys
import time

DR = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(DR, "logs")
OUT = os.path.join(DR, "dream_health.jsonl")
STEPS = os.path.join(DR, "dream_steps.jsonl")
STREAK_WARN = 3          # a step that did not finish this many runs in a row is named in the summary line
STAMP_RX = re.compile(r"^dream_(\d{8})_(\d{6})\.log$")
TIME_RX = re.compile(r"^(\d{2}):(\d{2}):(\d{2}) (.*)$")
LIMIT_RX = re.compile(r"usage limit|weekly limit|hit your limit|limit reached|out of extra usage|rate.?limit", re.I)


def _read(path, cap=40 * 1024 * 1024):
    try:
        with io.open(path, encoding="utf-8", errors="replace") as f:
            return f.read(cap)
    except Exception:
        return None


def stamp_epoch(stamp):
    return time.mktime(time.strptime(stamp, "%Y%m%d_%H%M%S"))


def parse_log(stamp, text):
    """One dream's row from its log text. Pure: no file access."""
    row = {"stamp": stamp, "hours": None, "rem": "none", "arm": "", "journal": "none", "persist": "none",
           "commit": "", "crashes": 0, "watchdog": 0, "rem_said": "", "capped": 0, "failed": 0, "budget_skips": 0,
           "v": 2}
    if text is None:
        row["rem"] = "unreadable"
        return row
    start = stamp_epoch(stamp)
    start_sod = int(stamp[9:11]) * 3600 + int(stamp[11:13]) * 60 + int(stamp[13:15])
    last_sod, day = start_sod, 0
    arm, completed, is_error, any_session, end = "", None, None, False, None
    said, skipped = "", False
    for line in text.splitlines():
        m = TIME_RX.match(line)
        if not m:
            continue
        sod = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
        if sod + 600 < last_sod:            # the clock went past midnight
            day += 1
        last_sod = sod
        msg = m.group(4)
        if msg.startswith("REM session starting on "):
            any_session = True
            arm = msg[len("REM session starting on "):].split(" ")[0]
            completed, is_error = None, None
        elif msg.startswith("rem arm "):     # the new runner names the login or the Codex arm it starts
            arm = msg[len("rem arm "):].split(" ")[0] or arm
        elif msg.startswith("REM session finished"):
            completed = "completed=True" in msg
        elif msg.startswith("result: is_error="):
            is_error = msg.startswith("result: is_error=True")
        elif msg.startswith("result text:"):
            said = msg[len("result text:"):].strip()[:160]
        elif msg.startswith("WATCHDOG:"):
            row["watchdog"] += 1
        elif msg.startswith("journal check:") and "journal(s) written" in msg:
            row["journal"] = "real"
        elif msg.startswith("wrote a PARTIAL stub journal"):
            row["journal"] = "stub"
        elif msg.startswith("JOURNAL MISSING") and row["journal"] == "none":
            row["journal"] = "missing"
        elif msg.startswith("persisted:"):
            row["persist"] = "pushed" if "pushed=True" in msg else "local"
            c = re.search(r"commit=([0-9a-f]{7,40})", msg)
            row["commit"] = c.group(1)[:12] if c else ""
        elif msg.startswith("PERSIST ABORTED"):
            row["persist"] = "aborted"
        elif msg.startswith("PUSH BLOCKED"):
            row["persist"] = "blocked"
        elif msg.startswith("persist commit deferred") and row["persist"] == "none":
            row["persist"] = "deferred"
        elif msg.startswith("dream cycle complete"):
            end = start + (day * 86400 + sod - start_sod)
        elif msg.startswith("STEP CAPPED:"):
            row["capped"] += 1
        elif msg.startswith("STEP FAILED:"):
            row["failed"] += 1
        elif msg.startswith("TAIL BUDGET:"):
            row["budget_skips"] += 1
        elif msg.startswith("another dream is in progress"):
            skipped = True
    row["crashes"] = text.count("Traceback (most recent call last)")
    row["arm"] = arm
    row["rem_said"] = said
    if skipped and not any_session:
        row["rem"] = "skipped"      # the scheduled start found the previous dream still holding the lock
    if any_session:
        if completed and is_error is not True:
            row["rem"] = "ok"
        elif said and LIMIT_RX.search(said):
            row["rem"] = "limit"
        elif row["watchdog"] and not completed:
            row["rem"] = "watchdog"
        else:
            row["rem"] = "error"
    if end is not None:
        row["hours"] = round((end - start) / 3600.0, 1)
        row["end"] = end
    return row


def _count_between(path, t0, t1, time_of):
    n = 0
    try:
        with io.open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    t = time_of(json.loads(line))
                except Exception:
                    continue
                if t is not None and t0 <= t <= t1:
                    n += 1
    except Exception:
        return None
    return n


def _judged_time(r):
    # a judged row carries no time of its own; its case id does: n<mmddHHMM>_<n> is the sheet the dream built
    m = re.match(r"^n(\d{2})(\d{2})(\d{2})(\d{2})_", str(r.get("case_id") or ""))
    if m:
        year = str(r.get("fired_at") or "")[:4]
        if not year.isdigit():
            year = time.strftime("%Y")
        try:
            return time.mktime(time.strptime("%s-%s-%s %s:%s:00" % ((year,) + m.groups()), "%Y-%m-%d %H:%M:%S"))
        except Exception:
            pass
    for k in ("judged_at", "ts", "written_at"):
        v = r.get(k)
        if isinstance(v, (int, float)):
            return float(v)
        if isinstance(v, str) and len(v) >= 19:
            try:
                return time.mktime(time.strptime(v[:19].replace("T", " "), "%Y-%m-%d %H:%M:%S"))
            except Exception:
                pass
    return None


def _methods_time(r):
    v = r.get("ts")
    try:
        return time.mktime(time.strptime(str(v)[:19], "%Y-%m-%dT%H:%M:%S"))
    except Exception:
        return None


def rows(limit=14, logs=LOGS, dr=DR):
    names = sorted(n for n in (os.listdir(logs) if os.path.isdir(logs) else []) if STAMP_RX.match(n))
    out = []
    for n in names[-limit:]:
        stamp = n[len("dream_"):-len(".log")]
        row = parse_log(stamp, _read(os.path.join(logs, n)))
        t0 = stamp_epoch(stamp)
        t1 = row.get("end") or (t0 + 12 * 3600)
        if row["rem"] == "skipped":          # it did nothing; rows in its window belong to the dream still running
            row["judged"], row["methods"] = 0, 0
        else:
            row["judged"] = _count_between(os.path.join(dr, "judged_nightly.jsonl"), t0, t1, _judged_time)
            row["methods"] = _count_between(os.path.join(dr, "dream_methods_log.jsonl"), t0, t1, _methods_time)
        try:
            row["log_quiet_h"] = round((time.time() - os.path.getmtime(os.path.join(logs, n))) / 3600.0, 1)
        except Exception:
            row["log_quiet_h"] = None
        out.append(row)
    return out


def summary_lines(rs):
    if not rs:
        return ["  no dream logs found"]
    starts = len(rs)
    skipped = sum(1 for r in rs if r["rem"] == "skipped")
    rs = [r for r in rs if r["rem"] != "skipped"] or rs
    n = len(rs)
    ok = sum(1 for r in rs if r["rem"] == "ok")
    stubs = sum(1 for r in rs if r["journal"] in ("stub", "missing"))
    pushed = sum(1 for r in rs if r["persist"] == "pushed")
    judged = sum(1 for r in rs if (r.get("judged") or 0) > 0)
    why = {}
    for r in rs:
        if r["rem"] not in ("ok",):
            why[r["rem"]] = why.get(r["rem"], 0) + 1
    hrs = sorted(r["hours"] for r in rs if r["hours"] is not None)
    med = hrs[len(hrs) // 2] if hrs else None
    lines = []
    if skipped:
        lines.append("  last %d scheduled starts: %d skipped because the dream before was still running" % (starts, skipped))
    lines.append("  last %d dreams that ran: REM finished %d, journal stub or missing %d, judge rows written in %d, "
                 "pushed to GitHub %d" % (n, ok, stubs, judged, pushed))
    if why:
        lines.append("  REM not finished: " + ", ".join("%s %d" % (k, v) for k, v in sorted(why.items())))
    last_push = next((r for r in reversed(rs) if r["persist"] == "pushed"), None)
    lines.append("  last pushed dream: %s" % (last_push["stamp"] + " commit " + last_push["commit"] if last_push
                                                 else "none in these %d" % n))
    if med is not None:
        lines.append("  a dream takes %.1f h start to finish (median of %d)" % (med, len(hrs)))
    caps = sorted(r.get("capped", 0) for r in rs)
    if caps and caps[-1] > 0:
        lines.append("  steps killed at their time cap: median %d a dream, most %d (each one is up to 45 minutes "
                     "of a held lock)" % (caps[len(caps) // 2], caps[-1]))
    st = step_lines()
    if st:
        lines.append(st[0])
    last = rs[-1]
    lines.append("  newest %s: REM %s%s, journal %s, persist %s%s" % (
        last["stamp"], last["rem"], (" on " + last["arm"]) if last["arm"] else "", last["journal"], last["persist"],
        (" - " + last["rem_said"][:70]) if last["rem_said"] and last["rem"] != "ok" else ""))
    return lines


def step_rows(path=None):
    """Last row per step from dream_steps.jsonl (written by RunPy in run_dream.ps1), plus each step's last ok."""
    path = path or STEPS
    last, last_ok = {}, {}
    try:
        with io.open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    r = json.loads(line)
                    name = r["step"]
                except Exception:
                    continue
                last[name] = r
                if r.get("state") == "ok":
                    last_ok[name] = r
    except Exception:
        return {}, {}
    return last, last_ok


def step_streaks(path=None):
    """For each step whose last run did not finish: how many runs in a row, and when the run of failures began.

    A step the dream logs as nonfatal can fail every night and nobody reads the line: the mistake-graph watch did
    for 35 dreams (14 Oct - 10 Nov 2026). The count in a row is what tells a bad night from a dead component.
    """
    streak = {}
    try:
        with io.open(path or STEPS, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    r = json.loads(line)
                    name = r["step"]
                except Exception:
                    continue
                if r.get("state") == "ok":
                    streak.pop(name, None)
                else:
                    n, since = streak.get(name, (0, r.get("ts")))
                    streak[name] = (n + 1, since)
    except Exception:
        return {}
    return streak


def _age_h(ts):
    try:
        return (time.time() - time.mktime(time.strptime(str(ts)[:19], "%Y-%m-%dT%H:%M:%S"))) / 3600.0
    except Exception:
        return None


def step_lines(path=None, full=False):
    """One summary line (and with full=True one line per step): which dream steps did not finish on their last run."""
    last, last_ok = step_rows(path)
    if not last:
        return []
    bad = sorted(n for n, r in last.items() if r.get("state") != "ok")
    never = [n for n in bad if n not in last_ok]
    head = "  dream steps: %d known, %d did not finish on their last run%s%s" % (
        len(last), len(bad), (": " + ", ".join(bad[:6]) + (" ..." if len(bad) > 6 else "")) if bad else "",
        (" (%d have never finished since rows began)" % len(never)) if never else "")
    streaks = step_streaks(path)
    dead = sorted(((n, s) for n, s in streaks.items() if s[0] >= STREAK_WARN), key=lambda x: (-x[1][0], x[0]))
    if dead:
        head += "; NOT FINISHED %d+ RUNS IN A ROW: %s" % (STREAK_WARN, ", ".join(
            "%s (%d, since %s)" % (n, s[0], str(s[1])[:10]) for n, s in dead[:4])) + (" ..." if len(dead) > 4 else "")
    if not full:
        return [head]
    out = [head, "  %-48s %-14s %7s %-12s %s" % ("step", "last state", "seconds", "last ok", "in a row")]
    for n in sorted(last, key=lambda k: (last[k].get("state") == "ok", -streaks.get(k, (0, None))[0], k)):
        r = last[n]
        a = _age_h(last_ok[n]["ts"]) if n in last_ok else None
        out.append("  %-48s %-14s %7s %-12s %s" % (n[:48], r.get("state", "?"), r.get("seconds", "-"),
                                                 "never" if a is None else "%.1f h ago" % a,
                                                 streaks[n][0] if n in streaks else ""))
    return out


def table(rs):
    out = ["stamp            hours rem      journal persist  judged methods capped failed crashes arm"]
    for r in rs:
        out.append("%-16s %5s %-8s %-7s %-8s %6s %7s %6d %6d %7d %s" % (
            r["stamp"], "-" if r["hours"] is None else "%.1f" % r["hours"], r["rem"], r["journal"], r["persist"],
            "-" if r.get("judged") is None else r["judged"], "-" if r.get("methods") is None else r["methods"],
            r.get("capped", 0), r.get("failed", 0), r["crashes"], r["arm"][:28]))
    return out


def record(rs, out=OUT):
    # append-only: a stamp is written again only when the row format gained fields (v); readers take the last row
    have = set()
    try:
        with io.open(out, encoding="utf-8") as f:
            for line in f:
                try:
                    j = json.loads(line)
                    if int(j.get("v") or 1) >= 2:
                        have.add(j.get("stamp"))
                except Exception:
                    pass
    except Exception:
        pass
    new = [r for r in rs if r["stamp"] not in have and (r.get("log_quiet_h") or 0) >= 2.0]
    if new:
        with io.open(out, "a", encoding="utf-8", newline="\n") as f:
            for r in new:
                keep = {k: v for k, v in r.items() if k not in ("end", "log_quiet_h")}
                keep["recorded_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
                f.write(json.dumps(keep, ensure_ascii=True) + "\n")
    return len(new)


def selftest():
    fails = []
    ran = [0]

    def check(name, cond):
        ran[0] += 1
        print(("ok   " if cond else "FAIL ") + name)
        if not cond:
            fails.append(name)

    clean = "\n".join([
        "02:42:26 REM session starting on claude-fable-5-1[1m] (watchdog: 45 min)",
        "03:06:40 REM session finished in 1454s (completed=True)",
        "03:06:42 result: is_error=False turns=15 cost=5.87",
        "03:06:42 journal check: 1 journal(s) written this cycle - dream_2026_11_10.md",
        "05:20:00 persisted: staged=412 pushed=True commit=abcdef1234567890 (secret gates: clean)",
        "05:38:51 dream cycle complete"])
    r = parse_log("20261110_023034", clean)
    check("clean night: REM ok", r["rem"] == "ok")
    check("clean night: journal real", r["journal"] == "real")
    check("clean night: persist pushed with its commit", r["persist"] == "pushed" and r["commit"] == "abcdef123456")
    check("clean night: 3.1 hours", r["hours"] == 3.1)
    check("clean night: arm is the model", r["arm"] == "claude-fable-5-1[1m]")

    dog = "\n".join([
        "22:42:52 REM session starting on claude-fable-5-1[1m] (watchdog)",
        "23:29:24 WATCHDOG: dream reached its limit - killing process tree",
        "23:31:23 REM session finished in 2912s (completed=False)",
        "23:31:37 REM hit a transient error - retrying once on claude-opus-5[1m]",
        "23:32:09 REM session starting on claude-opus-5[1m] (watchdog)",
        "00:59:14 WATCHDOG: dream reached its limit - killing process tree",
        "01:02:36 REM session finished in 5426s (completed=False)",
        "01:02:52 JOURNAL MISSING: REM ran but wrote no journal",
        "01:03:50 wrote a PARTIAL stub journal naming 271 touched memor(y|ies): dream_x_partial.md",
        "Traceback (most recent call last)",
        "06:01:51 PERSIST ABORTED by secret gate (fail-closed): the scanner COULD NOT RUN",
        "06:04:17 dream cycle complete"])
    r = parse_log("20261109_223120", dog)
    check("watchdog night: REM watchdog", r["rem"] == "watchdog" and r["watchdog"] == 2)
    check("watchdog night: journal stub", r["journal"] == "stub")
    check("watchdog night: persist aborted", r["persist"] == "aborted")
    check("watchdog night: hours cross midnight (7.5)", r["hours"] == 7.5)
    check("watchdog night: one crash, last arm kept", r["crashes"] == 1 and r["arm"] == "claude-opus-5[1m]")

    lim = "\n".join([
        "10:42:52 REM session starting on claude-fable-5-1[1m] (watchdog)",
        "10:43:30 REM session finished in 38s (completed=True)",
        "10:43:31 result: is_error=True turns=1 cost=0",
        "10:43:31 result text: You have hit your weekly limit; resets 14 Nov",
        "10:44:00 rem arm codex:gpt-6.1-sol home acc4",
        "10:44:01 REM session starting on codex:gpt-6.1-sol",
        "11:10:00 REM session finished in 1559s (completed=True)",
        "11:10:01 result: is_error=False turns=22 cost=0",
        "11:10:02 journal check: 1 journal(s) written this cycle - dream_y.md",
        "13:00:00 PUSH BLOCKED by secret gate on server-bound exact range (exit=2)",
        "13:01:00 dream cycle complete"])
    r = parse_log("20261110_103000", lim)
    check("limit then Codex: REM ok on the Codex arm", r["rem"] == "ok" and r["arm"].startswith("codex:"))
    check("limit then Codex: push blocked", r["persist"] == "blocked")
    lim2 = "\n".join(lim.split("\n")[:4] + ["10:50:00 dream cycle complete"])
    r = parse_log("20261110_103000", lim2)
    check("limit only: REM limit, with what it said", r["rem"] == "limit" and "weekly limit" in r["rem_said"])
    check("limit only: no journal, no persist", r["journal"] == "none" and r["persist"] == "none")

    check("unreadable log gives a row, not an exception", parse_log("20261110_103000", None)["rem"] == "unreadable")
    check("no REM line at all reads as none", parse_log("20261110_103000", "10:31:00 dream cycle complete")["rem"] == "none")

    rs = [parse_log("20261110_023034", clean), parse_log("20261109_223120", dog), parse_log("20261110_103000", lim2)]
    for x in rs:
        x["judged"], x["methods"] = 0, 0
    rs[0]["judged"] = 12
    s = "\n".join(summary_lines(rs))
    check("summary counts: 1 finished, 1 stub, 1 with judge rows, 1 pushed",
          "REM finished 1, journal stub or missing 1, judge rows written in 1, pushed to GitHub 1" in s)
    check("summary names why REM did not finish", "limit 1" in s and "watchdog 1" in s)
    check("summary names the last pushed dream", "20261110_023034 commit abcdef123456" in s)
    check("summary of nothing is one line", summary_lines([]) == ["  no dream logs found"])

    import tempfile
    d = tempfile.mkdtemp(prefix="dh_")
    o = os.path.join(d, "dream_health.jsonl")
    for x in rs:
        x["log_quiet_h"] = 5.0
    rs[2]["log_quiet_h"] = 0.5
    check("record writes finished dreams only", record(rs, o) == 2)
    check("record is idempotent", record(rs, o) == 0)
    rs[2]["log_quiet_h"] = 3.0
    check("record picks the dream up once its log is quiet", record(rs, o) == 1)
    with io.open(o, encoding="utf-8") as f:
        got = [json.loads(x) for x in f]
    check("recorded rows carry no scratch fields", all("end" not in g and "log_quiet_h" not in g for g in got) and len(got) == 3)

    t = _judged_time({"judged_at": "2026-11-07 22:03:11"})
    check("judged row time parses", t is not None and time.strftime("%H:%M", time.localtime(t)) == "22:03")
    check("methods row time parses", _methods_time({"ts": "2026-11-10T04:10:49"}) is not None)
    t = _judged_time({"case_id": "n11071859_003", "fired_at": "2026-11-07 02:24:13"})
    check("a judged row is timed by its sheet (case id), not by the fire it judges",
          t is not None and time.strftime("%Y-%m-%d %H:%M", time.localtime(t)) == "2026-11-07 18:59")
    r = parse_log("20261108_103435", "10:34:41 power throttling: helper pid 1 keeps this tree opted out\n"
                                     "10:36:37 another dream is in progress - exiting")
    check("a start that found the lock held reads as skipped", r["rem"] == "skipped" and r["hours"] is None)
    capped = "\n".join([
        "18:42:52 REM session starting on claude-fable-5-1[1m] (watchdog)",
        "19:50:00 REM session finished in 4282s (completed=True)",
        "21:00:00 STEP CAPPED: heed_audit trend exceeded 2700s and was killed (output above)",
        "22:00:00 STEP CAPPED: ensure_index exceeded 2700s and was killed (output above)",
        "22:10:00 STEP FAILED: mistake_graph watch exited 1 (output above)",
        "03:30:00 TAIL BUDGET: 8.8 h since start exceeds 6 h - skipping bm25 build",
        "11:42:00 dream cycle complete"])
    r2 = parse_log("20261107_184245", capped)
    check("capped, failed and budget-skipped steps are counted",
          (r2["capped"], r2["failed"], r2["budget_skips"]) == (2, 1, 1) and r2["hours"] == 17.0)
    both = [r, r2]
    for x in both:
        x["judged"], x["methods"] = 0, 0
    s = "\n".join(summary_lines(both))
    check("summary separates skipped starts from dreams that ran",
          "last 2 scheduled starts: 1 skipped" in s and "last 1 dreams that ran: REM finished 1" in s)
    check("summary names the capped steps", "steps killed at their time cap: median 2 a dream, most 2" in s)

    sp = os.path.join(d, "dream_steps.jsonl")
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    with io.open(sp, "w", encoding="utf-8", newline="\n") as f:
        for step, state in (("bm25", "ok"), ("ensure_index", "ok"), ("ensure_index", "capped"),
                            ("heed_audit trend", "capped"), ("curiosity", "skipped_budget"), ("bm25", "ok")):
            f.write(json.dumps({"stamp": "x", "step": step, "seconds": 5, "exit": 0, "state": state, "ts": now}) + "\n")
        f.write("not json\n")
    sl = step_lines(sp, full=True)
    check("steps: last state per step, bad ones named", sl[0].startswith(
        "  dream steps: 4 known, 3 did not finish on their last run: curiosity, ensure_index, heed_audit trend"))
    check("steps: a step that never finished is counted", "(2 have never finished since rows began)" in sl[0])
    check("steps: full view lists every step, unfinished first", len(sl) == 6 and "bm25" in sl[-1] and "never" in sl[2])
    check("steps: no file gives no line", step_lines(os.path.join(d, "absent.jsonl")) == [])
    check("steps: one bad run is not called a dead component", "IN A ROW" not in sl[0])
    with io.open(sp, "a", encoding="utf-8", newline="\n") as f:
        for i, state in enumerate(("failed", "failed", "ok", "failed", "capped", "failed")):
            f.write(json.dumps({"stamp": "x", "step": "mistake_graph watch", "seconds": 5, "exit": 1, "state": state,
                                "ts": "2026-10-%02dT10:00:00" % (14 + i)}) + "\n")
    sl = step_lines(sp, full=True)
    check("steps: three runs in a row are named with the count and the day the run began",
          "NOT FINISHED 3+ RUNS IN A ROW: mistake_graph watch (3, since 2026-10-17)" in sl[0])
    check("steps: an ok run in between ends the count", step_streaks(sp)["mistake_graph watch"][0] == 3)
    check("steps: the dead component is listed first", "mistake_graph watch" in sl[2] and sl[2].rstrip().endswith("3"))

    o2 = os.path.join(d, "dh2.jsonl")
    with io.open(o2, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps({"stamp": "20261107_184245", "rem": "ok"}) + "\n")     # a row from before v2
    r2["log_quiet_h"] = 9.0
    check("record rewrites a stamp whose row predates the new fields, once", record([r2], o2) == 1 and record([r2], o2) == 0)
    print("PASS: %d checks, 0 failed" % ran[0] if not fails else "FAIL: %d failed" % len(fails))
    return 1 if fails else 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--steps" in argv:
        print("\n".join(step_lines(full=True) or ["  no dream_steps.jsonl yet (the runner writes it from the next dream on)"]))
        return 0
    rs = rows()
    if "--record" in argv:
        print("recorded %d new dream row(s) in %s" % (record(rs), OUT))
        return 0
    if "--summary" not in argv:
        print("\n".join(table(rs)))
    print("\n".join(summary_lines(rs)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
