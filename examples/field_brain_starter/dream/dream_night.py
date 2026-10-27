"""Run a night of dreams: one run_dream.py cycle after another until a deadline, with a rest between them.

    python dream/dream_night.py --agent-cmd "claude -p --permission-mode acceptEdits" --hours 5
    python dream/dream_night.py --agent-cmd "codex exec --full-auto -" --hours 3 --rest 15 --max-cycles 6
    python dream/dream_night.py --agent-cmd "claude -p --permission-mode acceptEdits" --stages file,connect

With --stages the cycles take the stages in turn (run_dream.py --stage): file, connect, file, connect, ... as a night
of sleep alternates slow-wave and REM. The filing pass comes first so the connecting pass links settled records.

One long dream is the wrong shape for a long night. A single agent session reads the agenda once, so the work it does
in its first hour never reaches the agenda it is still working from, and a session that runs for hours is more likely
to be cut off by a timeout with nothing written down. Short cycles fix both: each one starts from an agenda rebuilt
from what the last one wrote, and each leaves its own log and backup.

The night stops on the first of:
- the deadline (no cycle starts unless --min-cycle minutes remain);
- --max-cycles cycles;
- the file dream/STOP, read before every cycle and during every rest;
- --idle-stop cycles in a row that changed no file in memory/ (default 2). The count comes from the cycle's own log,
  not from the agent's exit status: an agent can exit cleanly having written nothing, and the reverse;
- another dream holding dream/.dream.lock.

Each cycle is an ordinary run_dream.py run, so the rules, the backup and the put-back of deleted records are the same
as for one dream. The night writes dream/logs/night_<stamp>.md: one row per cycle with its log, the files it changed
and the agenda counts after it. Standard library only.
"""
import argparse
import datetime as dt
import glob
import os
import re
import shlex
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(HERE, "logs")
STOP = os.path.join(HERE, "STOP")
RUN = os.path.join(HERE, "run_dream.py")


def cycle_log(since):
    """The dream log a cycle wrote: the newest dream_*.md modified after `since` (a time.time() value)."""
    new = [p for p in glob.glob(os.path.join(LOGS, "dream_*.md")) if os.path.getmtime(p) >= since]
    return max(new, key=os.path.getmtime) if new else None


def read_log(path):
    """(files changed, files put back, {section: count after}) from a run_dream.py log."""
    text = open(path, encoding="utf-8", errors="replace").read()
    after = {m.group(1): int(m.group(3)) for m in re.finditer(r"^\| (.+?) \| (\d+) \| (\d+) \|$", text, re.M)}

    def items(head):
        m = re.search(r"^## %s\n\n(.*?)(?:\n\n|\Z)" % re.escape(head), text, re.M | re.S)
        return [ln for ln in m.group(1).splitlines() if ln.startswith("- ") and ln != "- none"] if m else []

    return items("Files the agent changed"), items("Records the agent deleted, put back from the backup"), after


def rest(seconds):
    """Sleep in short steps so a STOP file written during the rest ends the night at once."""
    end = time.time() + seconds
    while time.time() < end:
        if os.path.exists(STOP):
            return False
        time.sleep(min(5.0, max(0.0, end - time.time())))
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--agent-cmd", required=True, help="agent CLI that reads the prompt on stdin, as for run_dream.py")
    ap.add_argument("--hours", type=float, default=5.0, help="length of the night (default 5)")
    ap.add_argument("--rest", type=float, default=10.0, help="minutes between cycles (default 10)")
    ap.add_argument("--max-cycles", type=int, default=8, help="hard cap on cycles (default 8)")
    ap.add_argument("--min-cycle", type=float, default=20.0,
                    help="minutes that must remain before a cycle starts (default 20)")
    ap.add_argument("--cycle-timeout", type=int, default=2700, help="seconds one cycle's agent may run (default 2700)")
    ap.add_argument("--idle-stop", type=int, default=2,
                    help="stop after this many cycles in a row that changed nothing (default 2; 0 never stops)")
    ap.add_argument("--stages", default="all",
                    help="comma-separated run_dream.py stages taken in turn, e.g. file,connect (default all)")
    a = ap.parse_args()
    stages = [s.strip() for s in a.stages.split(",") if s.strip()]
    bad = [s for s in stages if s not in ("all", "file", "connect")]
    if not stages or bad:
        ap.error("--stages takes all, file and connect, comma-separated (got %r)" % a.stages)

    start = dt.datetime.now()
    deadline = start + dt.timedelta(hours=a.hours)
    stamp = start.strftime("%Y%m%d_%H%M%S")
    os.makedirs(LOGS, exist_ok=True)
    night = os.path.join(LOGS, "night_%s.md" % stamp)
    rows, idle, why = [], 0, None

    def write():
        out = ["# Night %s" % stamp, "",
               "Agent: `%s`. Deadline %s, rest %g min, at most %d cycles, stages %s." % (
                   a.agent_cmd, deadline.strftime("%Y-%m-%d %H:%M"), a.rest, a.max_cycles, ", ".join(stages)), "",
               "| cycle | stage | started | exit | files changed | put back | log | agenda after |",
               "|---|---|---|---|---|---|---|---|"]
        out += ["| %d | %s | %s | %s | %d | %d | %s | %s |" % r for r in rows]
        out += ["", "Stopped: %s." % (why or "still running"), ""]
        open(night, "w", encoding="utf-8", newline="\n").write("\n".join(out))

    while True:
        n = len(rows) + 1
        left = (deadline - dt.datetime.now()).total_seconds() / 60.0
        if os.path.exists(STOP):
            why = "dream/STOP is present"
        elif n > a.max_cycles:
            why = "reached %d cycles" % a.max_cycles
        elif left < a.min_cycle:
            why = "%.0f minutes left, under the %g a cycle needs" % (max(left, 0.0), a.min_cycle)
        if why:
            break
        t0 = time.time()
        began = dt.datetime.now().strftime("%H:%M")
        timeout = int(min(a.cycle_timeout, max(60.0, left * 60.0)))
        stage = stages[(n - 1) % len(stages)]
        cmd = [sys.executable, RUN, "--agent-cmd", a.agent_cmd, "--timeout", str(timeout), "--stage", stage]
        res = subprocess.run(cmd, cwd=os.path.dirname(HERE), capture_output=True, text=True, encoding="utf-8",
                             errors="replace")
        if res.returncode == 3:
            why = "another dream holds dream/.dream.lock"
            break
        log = cycle_log(t0)
        if log is None:
            rows.append((n, stage, began, res.returncode, 0, 0, "(no log)", (res.stdout + res.stderr).strip()[-120:]))
            why = "cycle %d wrote no log" % n
            break
        changed, back, after = read_log(log)
        counts = ", ".join("%s %d" % kv for kv in after.items())
        rows.append((n, stage, began, res.returncode, len(changed), len(back), os.path.basename(log), counts))
        write()
        print("cycle %d (%s): exit %s, %d file(s) changed, %d put back (%s)"
              % (n, stage, res.returncode, len(changed), len(back), os.path.basename(log)), flush=True)
        idle = idle + 1 if not changed else 0
        if a.idle_stop and idle >= a.idle_stop:
            why = "%d cycle(s) in a row changed nothing" % idle
            break
        if (deadline - dt.datetime.now()).total_seconds() / 60.0 < a.rest + a.min_cycle:
            why = "no room for another cycle before the deadline"
            break
        if not rest(a.rest * 60.0):
            why = "dream/STOP is present"
            break
    write()
    print("night done: %d cycle(s); stopped because %s; log %s" % (len(rows), why, night))
    return 0


if __name__ == "__main__":
    sys.exit(main())
