"""test_recall_server_orphan.py - a served call that holds the lock past ORPHAN_S makes the server exit, so the next
caller is not declined busy behind an answer nobody is waiting for.

 O1 a call that never returns: the server process exits on its own, rc 0, while the call is still running
 O2 its log says why, and calls.jsonl carries one "orphaned" row
 O3 the endpoint is retired on the way out (endpoint.json -> endpoint.json.stopped)
 O4 a control: with BRS_ORPHAN_S=0 the same stuck call leaves the server up

The server runs in a child process with a stand-in Brain (its call sleeps on a "slow" argv) and its state folder in a
temp directory, so no live server, index or log is touched. About a minute: the watch loop looks every 15 s.

    python test_recall_server_orphan.py      (ALL PASS at the end)
"""
if __name__ == "__main__" and __import__("sys").argv[1:2] in (["-h"], ["--help"]):
    print((__doc__ or "").strip() or "run with no arguments")
    raise SystemExit(0)

import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
results = []
N_CHECKS = 5

DRIVER = r'''
import os, sys, time
sys.path.insert(0, sys.argv[1])
import brain_recall_server as BRS
st = sys.argv[2]
BRS.STATE_DIR, BRS.ENDPOINT = st, os.path.join(st, "endpoint.json")
BRS.LOG, BRS.CALL_LOG = os.path.join(st, "server.log"), os.path.join(st, "calls.jsonl")
BRS.ORPHAN_S = float(sys.argv[3])


class FakeBrain:
    def __init__(self):
        self.g, self.calls, self.resident = {}, 0, None
        self.stores, self.sigs, self.filled = [], {}, set()

    def code_changed(self):
        return None

    def call(self, argv, env, cwd):
        self.calls += 1
        if argv and argv[0] == "slow":
            time.sleep(600)
        return {"rc": 0, "out": "", "ms": 1}


BRS.Brain = FakeBrain
BRS.main()
'''


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


def start(st, orphan_s):
    env = {k: v for k, v in os.environ.items() if not k.startswith(("BRAIN_", "BRS_"))}
    env.update(BRS_WARMUP="0", BRS_CALL_LOG="1")
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    p = subprocess.Popen([sys.executable, "-s", "-c", DRIVER, HERE, st, str(orphan_s)], env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, creationflags=flags)
    ep = os.path.join(st, "endpoint.json")
    t0 = time.time()
    while time.time() - t0 < 60 and p.poll() is None:
        try:
            with open(ep, encoding="utf-8") as f:
                return p, json.load(f)
        except (OSError, ValueError):
            time.sleep(0.2)
    return p, None


def send_slow(ep):
    """Send a call that never returns and stop reading after 1 s, as a client past its read timeout would."""
    s = socket.create_connection(("127.0.0.1", int(ep["port"])), timeout=2)
    s.sendall((json.dumps({"token": ep["token"], "op": "call", "argv": ["slow"], "env": {}, "cwd": HERE}) + "\n").encode())
    s.settimeout(1)
    try:
        s.recv(100)
    except socket.timeout:
        pass
    s.close()


tmp = tempfile.mkdtemp(prefix="brs_orphan_")
procs = []
try:
    st = os.path.join(tmp, "on")
    os.makedirs(st)
    p, ep = start(st, 3)
    procs.append(p)
    if ep is None:
        check(False, "O1 server came up (stderr: %s)" % (p.stderr.read().decode(errors="replace")[-300:] if p.poll() is not None else "still loading"))
    else:
        send_slow(ep)
        t0 = time.time()
        try:
            rc = p.wait(timeout=60)
        except subprocess.TimeoutExpired:
            rc = None
        check(rc == 0, "O1 the server exits by itself (rc %s after %.0f s) while the call is still stuck" % (rc, time.time() - t0))
        log = open(os.path.join(st, "server.log"), encoding="utf-8").read() if os.path.exists(os.path.join(st, "server.log")) else ""
        check("past its client's read timeout" in log, "O2 the log names the reason")
        rows = [json.loads(x) for x in open(os.path.join(st, "calls.jsonl"), encoding="utf-8")] if os.path.exists(os.path.join(st, "calls.jsonl")) else []
        check(sum(1 for r in rows if r.get("op") == "orphaned") == 1, "O2 calls.jsonl has one orphaned row: %s" % rows)
        check(not os.path.exists(os.path.join(st, "endpoint.json")) and os.path.exists(os.path.join(st, "endpoint.json.stopped")),
              "O3 the endpoint is retired")

    st0 = os.path.join(tmp, "off")
    os.makedirs(st0)
    p0, ep0 = start(st0, 0)
    procs.append(p0)
    if ep0 is None:
        check(False, "O4 control server came up")
    else:
        send_slow(ep0)
        time.sleep(35)   # two watch ticks past the 3 s the first server was given
        check(p0.poll() is None, "O4 control: with BRS_ORPHAN_S=0 the server is still up after 35 s")
finally:
    for p in procs:
        if p.poll() is None:
            p.kill()
            p.wait()
    time.sleep(0.5)
    shutil.rmtree(tmp, ignore_errors=True)

ok = all(results) and len(results) == N_CHECKS
print("ALL PASS" if ok else "FAILED %d of %d" % (N_CHECKS - results.count(True), N_CHECKS))
sys.exit(0 if ok else 1)
