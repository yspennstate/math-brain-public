"""run_probe.py <ID>: start one small Codex worker in codex_probe/<ID>/, the way the laptop rig's run_one.py does
(same account home, model, effort, normal speed, memory gate and the rig's one-launch-per-ten-minutes slot), plus
any extra '-c key=value' lines found in codex_probe/<ID>/EXTRA_C. Windowless, BelowNormal. Log: <ID>/codex.log.
Not a ramp: one worker per call, used for harness measurements."""
import ctypes
import os
import subprocess
import sys
import time


class MS(ctypes.Structure):
    _fields_ = [("l", ctypes.c_ulong), ("ml", ctypes.c_ulong), ("tp", ctypes.c_ulonglong), ("ap", ctypes.c_ulonglong),
                ("tf", ctypes.c_ulonglong), ("af", ctypes.c_ulonglong), ("tv", ctypes.c_ulonglong), ("av", ctypes.c_ulonglong),
                ("x", ctypes.c_ulonglong)]


HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.environ.get("PROBE_RIG", os.path.expanduser("~/brain-repo/12_cognitive_architecture/codex_local_1108"))
bid = sys.argv[1]
D = os.path.join(HERE, bid)
log = open(os.path.join(D, "codex.log"), "a", encoding="utf-8")
# 15 Nov 02:2x: the slot had no order. Eighteen rig briefs and this probe polled it once a minute and whoever came first
# after the ten minutes won, so the AB4 probe waited 90 min, gave up, exited 0 and its driver logged the run as done.
# Now a waiter keeps a ticket in <RIG>/.slot_queue (its first-wait time, touched every minute) and only the oldest live
# ticket may take the slot; a ticket untouched for 3 min is a dead waiter and is ignored. Giving up exits 3.
Q = os.path.join(RIG, ".slot_queue")
os.makedirs(Q, exist_ok=True)
TK = os.path.join(Q, bid)
if not os.path.exists(TK):
    open(TK, "w").write("%.0f" % time.time())


def first_in_line():
    live = []
    for f in os.listdir(Q):
        p = os.path.join(Q, f)
        try:
            if time.time() - os.path.getmtime(p) < 180:
                live.append((float(open(p).read() or 0), f))
        except (OSError, ValueError):
            pass
    return not live or min(live)[1] == bid


for i in range(int(os.environ.get("RUN_PROBE_WAIT_MIN", "480"))):
    os.utime(TK)
    m = MS()
    m.l = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    avail, commit = m.ap // 2 ** 20, 1 - m.af / m.tf
    if avail >= 2500 and commit <= 0.92:
        if not first_in_line():
            log.write("%s held: an older ticket is waiting\n" % time.strftime("%H:%M"))
            log.flush()
            time.sleep(60)
            continue
        lk = os.path.join(RIG, ".launch_slot")
        try:
            if os.path.exists(lk) and time.time() - os.path.getmtime(lk) >= 600:
                os.remove(lk)
            os.close(os.open(lk, os.O_CREAT | os.O_EXCL))
            break
        except OSError:
            log.write("%s held: another brief launched under 10 min ago\n" % time.strftime("%H:%M"))
            log.flush()
            time.sleep(60)
            continue
    log.write("%s held: avail %d MB commit %.3f\n" % (time.strftime("%H:%M"), avail, commit))
    log.flush()
    time.sleep(60)
else:
    log.write("%s gave up: the gate never opened\n" % time.strftime("%H:%M"))
    log.flush()
    os.remove(TK)
    sys.exit(3)
os.remove(TK)
log.write("%s start (avail %d MB commit %.3f)\n" % (time.strftime("%H:%M:%S"), avail, commit))
log.flush()
extra = []
ex = os.path.join(D, "EXTRA_C")
if os.path.exists(ex):
    for ln in open(ex, encoding="utf-8").read().splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#"):
            extra += ["-c", ln]
for bad in ("fast", "priority", "ultrafast"):
    if any(bad in e and "false" not in e for e in extra):
        log.write("refused: EXTRA_C names a faster tier\n")
        sys.exit(1)
CODEX = os.environ.get("PROBE_CODEX", "codex")
env = dict(os.environ, CODEX_HOME=os.environ.get("PROBE_CODEX_HOME", os.path.expanduser("~/.codex")))
cmd = [CODEX, "exec", "--skip-git-repo-check", "-m", "gpt-6.1-sol", "-c", 'model_reasoning_effort="high"',
       "-c", 'service_tier="default"', "-c", "features.fast_mode=false", "-c", "features.ultrafast_mode=false",
       "-c", 'sandbox_mode="danger-full-access"'] + extra
if os.path.exists(os.path.join(D, "NOHOOKS")):
    cmd += ["-c", "features.hooks=false"]
cmd += ["-C", D, "-"]
log.write("extra flags: %s\n" % " ".join(extra))
log.flush()
p = subprocess.run(cmd, cwd=D, input=open(os.path.join(D, "PROMPT.md"), "rb").read(), stdout=log, stderr=subprocess.STDOUT,
                   env=env, creationflags=0x08000000 | 0x4000)
log.write("%s exit %s\n" % (time.strftime("%H:%M:%S"), p.returncode))
