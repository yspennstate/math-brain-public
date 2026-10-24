#!/usr/bin/env python3
"""run_bounded.py - run a command windowless with a hard wall-clock cap, killing its whole tree on expiry.

    python run_bounded.py <seconds> <log-path-or-'-'> <exe> [args...]

WHY (2026-09-14): a Task Scheduler "stop the task after N minutes" kills the task's launcher (wscript.exe) and
not the python the VBS started under it. Three brain jobs were found alive hours past their caps on 09-13/14 -
the 03:30 dream (18 h, holding dream.lock), the hourly project-memory runner (3 h 44 m at 2 pct CPU, holding
its lock so every later hourly run exited 1), the weekly heed report - each starved at BelowNormal under render
load, each blocking its successors. This supervisor is what the VBS launchers run instead of the child directly:
the child gets CREATE_NO_WINDOW (no console, no flash), and on expiry `taskkill /T /F` takes the tree.
Exit code: the child's, or 124 on the cap. A log path records start, exit and any kill.
"""
import io
import json
import os
import subprocess
import sys
import time

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    # Discovery is not execution: this file does its work at module scope, so the
    # guard must come before the first statement that runs.
    print(__doc__ or os.path.basename(__file__))
    raise SystemExit(0)



def owner_away(state_path=None):
    """The governor's own verdict from compute_state.json. Stale or unreadable state reads as PRESENT."""
    try:
        st = state_path or os.path.join(os.path.expanduser("~"), ".claude", "compute", "compute_state.json")
        if time.time() - os.path.getmtime(st) > 180:
            return False
        with io.open(st, encoding="utf-8") as fh:
            d = json.load(fh)
        return d.get("status") in ("ok", None) and d.get("mode") in ("owner_away_open", "open")
    except Exception:
        return False


def _log(path, msg):
    line = "%s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg)
    if path and path != "-":
        try:
            with io.open(path, "a", encoding="utf-8") as f:
                f.write(line)
            return
        except Exception:
            pass
    try:
        sys.stderr.write(line)
    except Exception:
        pass


def _tail(path, limit=1200, since=0):
    """The last `limit` characters the child wrote SINCE byte offset `since`, on one line.

    WHY `since` EXISTS (2026-09-16). The .child file is opened in APPEND mode and is never truncated,
    so a plain tail returns whatever the PREVIOUS run left behind. That is not theoretical: the
    project-memory hourly passes killed at their cap on 09-16 logged "its last output: <traceback>",
    and the traceback belonged to an EARLIER run that really had crashed - which read as four crashing
    passes when they had actually run silently to the cap. A supervisor that quotes the wrong run's
    output is worse than one that quotes none. `since` is the file's size at launch.
    """
    try:
        size = os.path.getsize(path)
        if size <= since:
            return "(the child wrote nothing this run)"
        with io.open(path, "rb") as f:
            f.seek(max(since, size - limit * 4))
            raw = f.read()
        text = raw.decode("utf-8", "replace")
        text = " | ".join(x.strip() for x in text.splitlines() if x.strip())
        return text[-limit:] if text else "(the child wrote nothing)"
    except Exception as exc:
        return "(child output unreadable: %s)" % type(exc).__name__


def main(argv):
    if len(argv) < 3:
        sys.stderr.write("usage: run_bounded.py <seconds> <log|-> <exe> [args...]\n")
        return 2
    try:
        seconds = float(argv[0])
    except ValueError:
        sys.stderr.write("seconds must be a number\n")
        return 2
    log, cmd = argv[1], argv[2:]
    flags = 0
    if os.name == "nt":
        flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    # RUN_BOUNDED_NORMAL_PRIORITY=1 starts the child at NORMAL instead of inheriting the caller's class.
    #
    # Why this exists (2026-09-14, measured): the dream runner sets itself BelowNormal at line 6 and every step
    # inherits it. On THIS box that is not politeness - it is a stall. The brain measured the mechanism on
    # 2026-09-13 at 135x (the same ffmpeg pass: 8.0 s at Normal, 1082.7 s at BelowNormal), and today four dream
    # steps in a row read as frozen: 3.28 seconds of CPU in 154 minutes for the graph rebuild, 1.30 s in 15
    # minutes for the salience refresh. The control that settles it: an IDENTICAL walk of the same 16,077 memory
    # files, started by hand at Normal priority, ran through 9,429 of them on 3.6 s of CPU at the same moment.
    # Same work, same files, same machine, same minute - only the priority class differs.
    # So the steps that walk the whole corpus get Normal; everything else the dream does stays BelowNormal, which
    # keeps the blast radius to the handful of steps that were actually starving.
    # Set explicitly on the running child rather than as a creation flag: a child of a BelowNormal parent came
    # back BelowNormal with NORMAL_PRIORITY_CLASS in creationflags (tested, both arms read BelowNormal), so the
    # flag is not doing what its name suggests here. SetPriorityClass on the handle is unambiguous and testable.
    # ...AND ONLY WHILE THE OWNER IS AWAY (2026-09-17). The variable is process-scoped, so the dream runner's one
    # setting reaches every step after it (59 raises in the 19:30 dream of 09-16, not three), and hour 19 measures
    # as the box's worst hour for him - cold opens 265 ms on both days while that dream walked the corpus at Normal
    # beside his browser. The compute doctrine already decides this case: owner_present_polite means BelowNormal,
    # owner_away_open means the work may take what is free. So the raise is honoured only while the governor says
    # he is away; at the keyboard the child keeps the caller's class and runs slower or caps, which the dream
    # tolerates (tiers stay at the previous generation). The 03:30 dream, run while he sleeps, gets Normal and
    # finishes. Which STEPS deserve the raise is still the owner's call (see run_dream.ps1); this only adds the gate.
    _want_normal = (os.name == "nt" and os.environ.get("RUN_BOUNDED_NORMAL_PRIORITY") == "1")
    if _want_normal and not owner_away():
        _want_normal = False
        _log(log, "run_bounded: owner present - the NORMAL raise is honoured only while he is away; the child keeps the caller's class")

    def _raise_to_normal(pid):
        try:
            import ctypes
            PROCESS_SET_INFORMATION = 0x0200
            NORMAL_PRIORITY_CLASS = 0x00000020
            k = ctypes.windll.kernel32
            h = k.OpenProcess(PROCESS_SET_INFORMATION, False, int(pid))
            if not h:
                return False
            ok = bool(k.SetPriorityClass(h, NORMAL_PRIORITY_CLASS))
            k.CloseHandle(h)
            return ok
        except Exception:
            return False
    # 2026-09-14: capture the child's streams. A pythonw child has no console, so its traceback went
    # NOWHERE - the hourly project-memory runner exited 1 every hour and the only record anywhere was
    # the scheduler's rc. The child writes to a file this supervisor owns, and the tail of it is copied
    # into the log on a non-zero exit; the file is never read while the child runs, so no pipe can fill
    # and deadlock it (the 09-12 scar: a piped stdout read only at exit hangs a long job).
    out_path = (log + ".child") if log and log != "-" else os.devnull
    try:
        out_fh = io.open(out_path, "ab")
    except Exception:
        out_fh = None
    # UNBUFFERED, OR A CAPPED CHILD TELLS YOU NOTHING (2026-09-15). The child's stdout is a FILE, not a
    # tty, so Python block-buffers it: a step that is killed at its cap dies with its whole log still in
    # a 8 KB buffer that is never flushed. Every capped step therefore reported "(the child wrote
    # nothing)" no matter how much it had printed - which is exactly what the dream logged when
    # build_brain_architecture hit its 2400 s cap, and why the project-memory hourly job's own .child log
    # had been frozen since 09:14 while the job was killed at 45 minutes every hour for seven hours. The
    # cap was diagnosable only by what the child managed to flush, which for a wedged job is nothing.
    # PYTHONUNBUFFERED costs a syscall per write and buys the reason it died.
    child_env = dict(os.environ)
    child_env["PYTHONUNBUFFERED"] = "1"
    try:
        p = subprocess.Popen(cmd, creationflags=flags, stdin=subprocess.DEVNULL, close_fds=True,
                             env=child_env,
                             stdout=(out_fh or subprocess.DEVNULL),
                             stderr=subprocess.STDOUT if out_fh else subprocess.DEVNULL)
        if _want_normal:
            _log(log, "run_bounded: pid %d raised to NORMAL priority (%s)"
                 % (p.pid, "ok" if _raise_to_normal(p.pid) else "REFUSED - it stays at the caller's class"))
    except Exception as exc:
        _log(log, "run_bounded: could not start %r: %s" % (cmd[:2], exc))
        if out_fh:
            out_fh.close()
        return 127
    _log(log, "run_bounded: started pid %d cap %.0fs: %s" % (p.pid, seconds, " ".join(cmd)[:200]))
    try:
        _start_off = os.path.getsize(out_path) if out_fh else 0
    except Exception:
        _start_off = 0
    try:
        rc = p.wait(timeout=seconds)
        _log(log, "run_bounded: pid %d exited %s" % (p.pid, rc))
        if rc:
            _log(log, "run_bounded: child said: %s" % _tail(out_path, since=_start_off))
        return rc
    except subprocess.TimeoutExpired:
        _log(log, "run_bounded: pid %d past its %.0fs cap - killing the tree; its last output: %s"
             % (p.pid, seconds, _tail(out_path, 600, since=_start_off)))
        # A KILL IS NOT DONE UNTIL THE PROCESS IS GONE (2026-09-14, found in this supervisor's own log):
        # `taskkill /T /F` walks the process tree, and on a starved disk that walk TIMED OUT at 30 s -
        # the log said "killing the tree", the orphan was still alive 8 minutes later, and the whole
        # point of the cap was lost. So: try the tree kill, then fall back to TerminateProcess on the
        # direct child (no enumeration, no disk), then VERIFY and say plainly which it was.
        killed_by = ""
        try:
            # IN-PROCESS FIRST (2026-09-17). taskkill walks the tree correctly but it is a PROCESS
            # SPAWN, fired exactly when the box is most contended - it hit its 30 s timeout at both
            # the 07:45 and 08:45 capped passes that day. psutil enumerates children in-process: no
            # spawn, no console, no filesystem walk. Measured on the same parent/child/grandchild
            # tree with all three confirmed dead: 0.08 s against taskkill's 1.42 s on a QUIET box,
            # and against 30 s-and-timeout on a stalled one. taskkill stays as the fallback so the
            # tree semantics survive if psutil is missing or refuses.
            import psutil
            root = psutil.Process(p.pid)
            procs = root.children(recursive=True) + [root]
            for q in procs:
                try:
                    q.kill()
                except Exception:
                    pass
            psutil.wait_procs(procs, timeout=10)
            killed_by = "psutil tree kill (%d process(es))" % len(procs)
        except Exception as exc:
            _log(log, "run_bounded: in-process tree kill unavailable (%s) - using taskkill" % exc)
            try:
                if os.name == "nt":
                    subprocess.run(["taskkill", "/PID", str(p.pid), "/T", "/F"], creationflags=flags,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
                else:
                    p.kill()
                killed_by = "taskkill"
            except Exception as exc2:
                _log(log, "run_bounded: tree kill failed (%s) - falling back to a direct kill" % exc2)
        if killed_by:
            _log(log, "run_bounded: tree taken by %s" % killed_by)
        alive = True
        try:
            p.wait(timeout=15)
            alive = False
        except Exception:
            pass
        if alive:
            try:
                p.kill()                       # TerminateProcess: no tree walk, no filesystem
                p.wait(timeout=15)
                alive = False
            except Exception:
                pass
        if alive:
            _log(log, "run_bounded: pid %d SURVIVED both kills - it still holds whatever it holds; "
                      "kill it by hand and find out why it will not die" % p.pid)
        else:
            _log(log, "run_bounded: pid %d confirmed gone" % p.pid)
        return 124


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
