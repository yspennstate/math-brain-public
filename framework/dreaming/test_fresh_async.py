"""Controls for the dedup-state writer thread in spread_recall (SPREAD_FRESH_ASYNC).

 F1 outside the resident server the state is written before _fresh returns
 F2 inside it (SPREAD_SERVER_CHILD=1) the dedup holds at once and the stamp lands after a flush
 F3 SPREAD_FRESH_ASYNC=0 inside the server writes before _fresh returns
 F4 a stamp another process wrote meanwhile is read in, and this process's own stamps are kept
 F5 the rate cap's held-back rows go through the writer and land after a flush

    python test_fresh_async.py      (a second or two; ALL PASS at the end)
Runs on a temporary state file, so nothing of the user's is read or written.
"""
import importlib
import io
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
TMP = tempfile.mkdtemp(prefix="fresh_async_")
results = []
SID = "0123abcd-1111-2222-3333-444455556666"


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


def load(child, async_on=True):
    for k in ("SPREAD_SERVER_CHILD", "SPREAD_FRESH_ASYNC"):
        os.environ.pop(k, None)
    if child:
        os.environ["SPREAD_SERVER_CHILD"] = "1"
    if not async_on:
        os.environ["SPREAD_FRESH_ASYNC"] = "0"
    import spread_recall
    m = importlib.reload(spread_recall)
    m.STATE = os.path.join(TMP, "state_%d.json" % len(results))
    m.DR = TMP
    return m


def state(m):
    try:
        return json.load(io.open(m.STATE, encoding="utf-8"))
    except Exception:
        return {}


try:
    m = load(child=False)
    check(m._fresh(SID, "alpha") and (SID + "|alpha") in state(m) and not m._fresh_async(),
          "F1 outside the server the state is on disk when _fresh returns")

    m = load(child=True)
    first, again = m._fresh(SID, "beta"), m._fresh(SID, "beta")
    landed = m._fresh_flush(5.0) and (SID + "|beta") in state(m)
    check(first and not again and landed, "F2 inside the server: dedup holds at once, the stamp lands after a flush")

    m = load(child=True, async_on=False)
    check(m._fresh(SID, "gamma") and (SID + "|gamma") in state(m) and not m._fresh_async(),
          "F3 SPREAD_FRESH_ASYNC=0 writes before _fresh returns")

    m = load(child=True)
    m._fresh(SID, "delta")
    m._fresh_flush(5.0)
    other = dict(state(m))
    other["9999eeee-0000-0000-0000-000000000000|epsilon"] = __import__("time").time()
    with io.open(m.STATE, "w", encoding="utf-8") as fh:
        json.dump(other, fh)
    os.utime(m.STATE, ns=(1, 1))
    m._fresh(SID, "zeta")
    m._fresh_flush(5.0)
    st = state(m)
    check(all((SID + "|" + k) in st for k in ("delta", "zeta")) and
          "9999eeee-0000-0000-0000-000000000000|epsilon" in st,
          "F4 another process's stamp is read in and this process's are kept")

    m = load(child=True)
    m._log_capped(SID, "eta", 9, 1.0, 60)
    m._fresh_flush(5.0)
    rows = io.open(os.path.join(TMP, "spread_capped.tsv"), encoding="utf-8").read() \
        if os.path.exists(os.path.join(TMP, "spread_capped.tsv")) else ""
    check("\teta\t" in rows, "F5 a held-back row lands through the writer")
except Exception as e:
    check(False, "raised %s: %s" % (type(e).__name__, e))
finally:
    for k in ("SPREAD_SERVER_CHILD", "SPREAD_FRESH_ASYNC"):
        os.environ.pop(k, None)
    shutil.rmtree(TMP, ignore_errors=True)
print("ALL PASS" if all(results) and len(results) == 5 else "FAILED %d of %d" % (5 - results.count(True), 5))
sys.exit(0 if all(results) and len(results) == 5 else 1)
