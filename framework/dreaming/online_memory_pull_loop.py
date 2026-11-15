"""Long-lived loop around the laptop online memory pull (dev copy, an agent, recall loop T-20261105-016).

Why: under load the scheduled task's runs start 16-271 s after their fire, because wscript + pythonw have to be
created, and IgnoreNew then drops any fire that lands while one is still starting. A single resident process pays
that start-up once, not every five minutes.

What it does: it imports the live online_memory_pull.py unchanged and calls its main() on a fixed grid (default
every 150 s). Like the live script, each run compares the remote head first and does a full listing hourly.
- One instance only: it holds <state>/run.lock, the same lock the single-run script takes, so a scheduled
  single run beside it exits at once.
- A second --loop start finds the lock held, logs how old the heartbeat is and exits. The hourly task can then
  launch it as its own watchdog: a dead loop releases the lock when the process ends.
- It stops when <state>/STOP exists, or after --minutes.
- Each tick is logged to <state>/loop_ticks.jsonl: grid time, start, jitter, duration and rc. Each start is
  logged to <state>/loop_starts.jsonl, so restarts per day can be counted.

Test (no live writes): --state <scratch dir> --dry-run. With --dry-run nothing reaches the memory folder, and
api_state goes to the scratch dir.
"""
import importlib.util
import json
import math
import os
import sys
import time

LIVE = os.path.join(os.path.expanduser("~"), ".claude", "dreaming", "online_memory_pull.py")


def arg(name, default=None):
    if name in sys.argv:
        i = sys.argv.index(name)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return default


def load(state):
    spec = importlib.util.spec_from_file_location("online_memory_pull_live", LIVE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    if state:
        m.STATE = state
        m.API_STATE = os.path.join(state, "api_state.json")
    return m


def jappend(path, rec):
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
    except OSError:
        pass


def main():
    state = arg("--state")
    interval = float(arg("--interval", "150"))
    minutes = float(arg("--minutes", "0"))
    dry = "--dry-run" in sys.argv
    m = load(state)
    # This loop drives the laptop's API fork (main(dry), unthrottle, log, STATE). The Mac's git fork of
    # online_memory_pull.py has main() with no argument and none of the others: refuse rather than crash
    # every 150 s on a computer whose pull is a different program.
    import inspect
    if not all(hasattr(m, n) for n in ("unthrottle", "log", "STATE", "API_STATE")) or \
            len(inspect.signature(m.main).parameters) < 1:
        try:
            with open(os.path.join(os.path.dirname(LIVE), "online_memory_pull_loop.refused"), "a",
                      encoding="utf-8") as f:
                f.write("%s this online_memory_pull.py is not the API fork; loop not started\n"
                        % time.strftime("%Y-%m-%d %H:%M:%S"))
        except OSError:
            pass
        return 2
    m.unthrottle()
    st = m.STATE
    os.makedirs(st, exist_ok=True)
    hb = os.path.join(st, "loop_heartbeat.json")
    import msvcrt
    lockf = open(os.path.join(st, "run.lock"), "a+")
    try:
        msvcrt.locking(lockf.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        try:
            age = time.time() - json.load(open(hb, encoding="utf-8"))["at"]
        except Exception:
            age = None
        m.log("loop: lock held (heartbeat %s s old); this start exits" % (None if age is None else round(age)))
        return 0
    jappend(os.path.join(st, "loop_starts.jsonl"), {"at": round(time.time()), "pid": os.getpid(), "dry": dry,
                                                     "interval": interval})
    m.log("loop: started pid %d, every %.0f s%s" % (os.getpid(), interval, ", dry run" if dry else ""))
    stop = os.path.join(st, "STOP")
    end = time.time() + minutes * 60 if minutes > 0 else None
    nxt = math.ceil(time.time() / interval) * interval
    ticks = 0
    try:
        live_mt = os.stat(LIVE).st_mtime_ns
    except OSError:
        live_mt = None
    while True:
        while time.time() < nxt:
            if os.path.exists(stop) or (end and time.time() > end):
                break
            time.sleep(min(5.0, max(0.05, nxt - time.time())))
        if os.path.exists(stop):
            m.log("loop: STOP file found after %d ticks; exiting" % ticks)
            break
        if end and time.time() > end:
            m.log("loop: test window over after %d ticks; exiting" % ticks)
            break
        # Reload the pull when its file changed: the module is loaded once, so before 7 Nov 23:5x a fix landed in
        # online_memory_pull.py reached this loop only at its next restart (the 20:54 edit pull never ran here).
        try:
            mt = os.stat(LIVE).st_mtime_ns
            if mt != live_mt:
                m2 = load(state)
                if all(hasattr(m2, n) for n in ("unthrottle", "log", "STATE", "API_STATE", "main")):
                    m = m2
                    m.log("loop: reloaded online_memory_pull.py (file changed)")
                live_mt = mt
        except Exception as e:
            m.log("loop: reload failed (%r); keeping the loaded copy" % (e,))
            live_mt = mt if "mt" in locals() else live_mt
        start = time.time()
        try:
            rc = m.main(dry)
        except Exception as e:
            import traceback
            m.log("loop: run crashed: %r %s" % (e, traceback.format_exc()[-400:].replace("\n", " | ")))
            rc = 1
        dur = time.time() - start
        ticks += 1
        missed = 0
        grid = nxt
        nxt += interval
        while nxt < time.time():
            nxt += interval
            missed += 1
        rec = {"grid": round(grid), "start": round(start, 2), "jitter": round(start - grid, 2),
               "dur": round(dur, 1), "rc": rc, "missed": missed}
        jappend(os.path.join(st, "loop_ticks.jsonl"), rec)
        try:
            with open(hb + ".tmp", "w", encoding="utf-8") as f:
                json.dump({"at": round(time.time()), "pid": os.getpid(), "ticks": ticks, "last": rec}, f)
            os.replace(hb + ".tmp", hb)
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    if sys.stdout is None:
        sys.stdout = sys.stderr = open(os.devnull, "w")
    sys.exit(main())
