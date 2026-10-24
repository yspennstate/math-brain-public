# -*- coding: utf-8 -*-
"""Breadth solvers on every open probability problem we hold (claude-322bc92e, 10 Oct 2026, his 07:3x ask
T-20261010-052). Takes rows of QUEUE_ALL_OPEN.jsonl in rank order; a row is taken by creating claims/<id>.lock first
(the pool and the Kaggle kernel can take rows the same way, so nothing is solved twice). Each row is one codex exec on
acc2 (gpt-6.1-sol, max reasoning, fast tier), windowless; the answer lands in results/<id>.txt for the cross-family
referee (pd_work/pilot_pair/wave_reader.py) before anything becomes a node.

    python breadth_runner.py LANES        STOP file beside this script ends every lane after its current problem
Gates before each launch: commit headroom >= 5 GB and RAM available >= 2 GB (claude-9bb7da02's 07:2x line), and the
acc2 meter below 101.
"""
import ctypes
import io
import json
import os
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
HOME = "~/.codex-img-acc2"
CLAIMS, RESULTS = os.path.join(HERE, "claims"), os.path.join(HERE, "results")
sys.path.insert(0, "~/pd_work/pilot_pair")
NO_SEARCH = ("1. Status first, from what you know (no web search, no browsing: his rule for Codex usage): name any paper "
             "you know that solves or refutes it, with authors and year; if you know it is solved, say so with the "
             "citation and stop with evidence_status=resolved_in_literature. A Claude reader checks the literature "
             "before any result is called new.")


class PERF(ctypes.Structure):
    _fields_ = [("cb", ctypes.c_ulong), ("CommitTotal", ctypes.c_size_t), ("CommitLimit", ctypes.c_size_t),
                ("CommitPeak", ctypes.c_size_t), ("PhysicalTotal", ctypes.c_size_t),
                ("PhysicalAvailable", ctypes.c_size_t), ("SystemCache", ctypes.c_size_t),
                ("KernelTotal", ctypes.c_size_t), ("KernelPaged", ctypes.c_size_t),
                ("KernelNonpaged", ctypes.c_size_t), ("PageSize", ctypes.c_size_t), ("HandleCount", ctypes.c_ulong),
                ("ProcessCount", ctypes.c_ulong), ("ThreadCount", ctypes.c_ulong)]


def headroom_gb():
    p = PERF()
    p.cb = ctypes.sizeof(PERF)
    ctypes.windll.psapi.GetPerformanceInfo(ctypes.byref(p), p.cb)
    return ((p.CommitLimit - p.CommitTotal) * p.PageSize / 1e9, p.PhysicalAvailable * p.PageSize / 1e9)


def log(msg):
    with io.open(os.path.join(HERE, "breadth_runner.log"), "a", encoding="utf-8") as fh:
        fh.write("%s %s\n" % (time.strftime("%H:%M:%S"), msg))


def take(rows):
    for r in rows:
        try:
            fd = os.open(os.path.join(CLAIMS, "%s.lock" % r["target_id"]), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            continue
        os.write(fd, ("claude-322bc92e breadth_runner %s" % time.strftime("%Y-%m-%d %H:%M:%S")).encode())
        os.close(fd)
        return r
    return None


def exe():
    import glob
    return (glob.glob(os.path.expanduser("~/AppData/Roaming/npm/node_modules/@openai/codex/**/"
                                         "x86_64-pc-windows-msvc/bin/codex.exe"), recursive=True) or ["codex.cmd"])[0]


def lane(n, rows, lock):
    from drive_pair import weekly_used
    while True:
        if os.path.exists(os.path.join(HERE, "STOP")):
            log("lane %d: STOP present, ending" % n)
            return
        commit, ram = headroom_gb()
        if commit < 5.0 or ram < 2.0:
            log("lane %d: holding (commit headroom %.1f GB, RAM %.1f GB)" % (n, commit, ram))
            time.sleep(120)
            continue
        used = weekly_used(HOME)
        if used is not None and used >= 101.0:
            log("lane %d: acc2 meter %s, ending" % (n, used))
            return
        with lock:
            r = take(rows)
        if r is None:
            log("lane %d: queue exhausted" % n)
            return
        pid = r["target_id"]
        prompt = r["prompt"]
        i, j = prompt.find("1. Status first"), prompt.find("\n2. Otherwise")
        if i >= 0 and j > i:
            prompt = prompt[:i] + NO_SEARCH + prompt[j:]
        wdir = os.path.join(RESULTS, pid)
        os.makedirs(wdir, exist_ok=True)
        cmd = [exe(), "exec", "--skip-git-repo-check", "-m", "gpt-6.1-sol", "-c", 'model_reasoning_effort="max"',
               "-c", 'service_tier="fast"', "-C", wdir, "--output-last-message", os.path.join(RESULTS, "%s.txt" % pid), "-"]
        t0 = time.time()
        with open(os.path.join(wdir, "codex.log"), "ab") as fh:
            try:
                rc = subprocess.run(cmd, input=prompt.encode("utf-8"), stdout=fh, stderr=subprocess.STDOUT, cwd=wdir,
                                    env=dict(os.environ, CODEX_HOME=HOME), timeout=5400,
                                    creationflags=0x08000000 | 0x00004000).returncode
            except subprocess.TimeoutExpired:
                rc = "timeout"
        log("lane %d: %s (rank %s) rc %s in %.0f s" % (n, pid, r.get("queue_rank"), rc, time.time() - t0))
        # 10 Oct 10:3x: acc2 ran out ("You've hit your usage limit") and every lane failed in 6 s, claiming 75 problems
        # it never worked; a usage-limit failure now releases its claim and ends the lane
        tail = open(os.path.join(wdir, "codex.log"), encoding="utf-8", errors="replace").read()[-3000:]
        if rc != 0 and "usage limit" in tail.lower():
            try:
                os.remove(os.path.join(CLAIMS, "%s.lock" % pid))
            except OSError:
                pass
            log("lane %d: account usage limit reached; claim on %s released, lane ends" % (n, pid))
            return


def main():
    lanes = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    os.makedirs(CLAIMS, exist_ok=True)
    os.makedirs(RESULTS, exist_ok=True)
    rows = [json.loads(l) for l in io.open(os.path.join(HERE, "QUEUE_ALL_OPEN.jsonl"), encoding="utf-8") if l.strip()]
    lock = threading.Lock()
    log("start: %d lanes, %d rows" % (lanes, len(rows)))
    ts = [threading.Thread(target=lane, args=(k, rows, lock)) for k in range(lanes)]
    for k, t in enumerate(ts):
        t.start()
        time.sleep(20)   # stagger the starts so commit rises one worker at a time
    for t in ts:
        t.join()
    log("all lanes ended")


if __name__ == "__main__":
    main()
