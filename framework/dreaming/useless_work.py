# -*- coding: utf-8 -*-
"""List the useless computation on this laptop (an agent, 7 Oct 2026, his order 03:1x).

Written at the author's request.

What counts as useless here: the same command line running more than once (duplicate watchers, supervisors, syncs a
scheduler stacked while the last one hung), helpers whose parent is long gone, and film computation on this laptop
(his 7 Oct orders: only script writing and image making here; narration, chunk cutting, assembly and upload run on
Kaggle). The scan reads command lines of interpreter and encoder processes only: reading all ~1,300 command lines on a
starved box is itself the kind of waste this hunts (41 copies of unthrottle_tree.py did exactly that every 20 s).

    python useless_work.py            report (never stops anything)
    python useless_work.py --json     the same as JSON

Stopping USELESS work is not shedding (it owns no progress). Real work is never shed (his 18 Sep law): report it.
"""
import collections
import json
import sys
import time

import psutil

NAMES = ("python.exe", "pythonw.exe", "powershell.exe", "pwsh.exe", "node.exe", "ffmpeg.exe", "wscript.exe",
         "cmd.exe", "blender.exe", "manim.exe")
# Film work that must not run on this laptop. Empty since 8 Oct 06:5x (an agent): the 7 Oct 03:1x list
# (narration, chunk cuts, render --audio/--video/--mux, declick) went stale the same day, when his 15:56 and 16:54 orders
# ("upload everything through here", "start narration from here as well, movie production is moving here") moved
# narration, cutting and uploads back here; this check went on calling every local cut useless for a day. unthrottle_tree.py
# stays useless on its own merits (7 Oct 03:1x: 41 copies scanning every command line) and is caught as a duplicate.
FILM_HERE = ()
# a duplicate of these is by design (pools of workers)
POOLS = ("codex", "claude.exe", "lean_worker", "picture_worker", "chrome", "msedgewebview2")


def scan():
    rows = []
    for p in psutil.process_iter(["name"]):
        n = (p.info.get("name") or "").lower()
        if n not in NAMES:
            continue
        try:
            with p.oneshot():
                cl = " ".join(str(x).replace("\\", "/") for x in p.cmdline())
                ct = p.cpu_times()
                rows.append(dict(pid=p.pid, name=n, cmd=cl, start=p.create_time(), cpu=ct.user + ct.system,
                                 parent_alive=psutil.pid_exists(p.ppid())))
        except psutil.Error:
            continue
    return rows


def report(rows):
    out = dict(duplicates=[], film_here=[], orphans=[])
    by = collections.defaultdict(list)
    for r in rows:
        if r["cmd"].strip():
            by[(r["name"], r["cmd"])].append(r)
    for (n, cmd), rs in by.items():
        if len(rs) > 1 and not any(k in cmd for k in POOLS) and "bash.exe" not in cmd and "-Command" not in cmd:
            out["duplicates"].append(dict(count=len(rs), cmd=cmd[:240], pids=[r["pid"] for r in rs],
                                          oldest=time.strftime("%m-%d %H:%M", time.localtime(min(r["start"] for r in rs))),
                                          cpu_s=round(sum(r["cpu"] for r in rs))))
    for r in rows:
        if any(k in r["cmd"] for k in FILM_HERE):    # the libx264 clause went with the 7 Oct list (8 Oct 06:5x)
            out["film_here"].append(dict(pid=r["pid"], cmd=r["cmd"][:200], cpu_s=round(r["cpu"])))
        if not r["parent_alive"] and time.time() - r["start"] > 6 * 3600 and r["cpu"] < 5:
            out["orphans"].append(dict(pid=r["pid"], cmd=r["cmd"][:200],
                                       since=time.strftime("%m-%d %H:%M", time.localtime(r["start"]))))
    out["duplicates"].sort(key=lambda d: -d["count"])
    return out


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    t0 = time.time()
    res = report(scan())
    if "--json" in sys.argv:
        print(json.dumps(res, indent=1))
        sys.exit(0)
    print("useless-work scan (%.0f s): %d duplicated command lines, %d film jobs on this laptop, %d idle orphans"
          % (time.time() - t0, len(res["duplicates"]), len(res["film_here"]), len(res["orphans"])))
    for d in res["duplicates"][:25]:
        print("  DUPLICATE x%d since %s, %d cpu-s: %s" % (d["count"], d["oldest"], d["cpu_s"], d["cmd"][:170]))
    for d in res["film_here"][:25]:
        print("  FILM WORK HERE (on the FILM_HERE list): pid %d, %d cpu-s: %s" % (d["pid"], d["cpu_s"], d["cmd"][:150]))
    for d in res["orphans"][:15]:
        print("  IDLE ORPHAN since %s: pid %d %s" % (d["since"], d["pid"], d["cmd"][:150]))
