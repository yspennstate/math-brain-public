"""A study hold set while a transport run is under way stops that run before its next write (29 Sep 2026).

    python test_math_transport_hold_race.py [TRANSPORT.py] [--old OLD_TRANSPORT.py]

Every write path of math_transport.run is replaced by a recorder in a scratch folder (the store is never opened), and the
hold is set at a chosen point of the run: during the scan (H1), between two memories (H2), before the index rebuild (H3).
H4: `hold` waits for a write in progress and lands after it. H5: with no hold the run writes everything (the positive
control). H6: a held run leaves the state file as it was, so the next run reads the same window again. H7: a manual
ingest refused when the hold arrives while it waits for the lock. N1 (with --old) runs H1 on the code before the fix
and shows the write made with the hold in force, which is the finding.
"""
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import threading
import time
import types

HERE = os.path.dirname(os.path.abspath(__file__))
FAILS = []


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" - " + detail) if detail else ""))
    if not ok:
        FAILS.append(name)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Rig:
    """One scratch folder, every write of the run recorded; nothing reaches the live store, ledger or index."""

    def __init__(self, mod, slugs=("m1", "m2")):
        self.mod = mod
        self.dir = tempfile.mkdtemp(prefix="mt_race_")
        self.events = []
        self.slugs = list(slugs)
        self.on_scan = None
        self.after_ingest = {}
        mod.HOLD = os.path.join(self.dir, "HOLD.json")
        mod.LEDGER = os.path.join(self.dir, "ledger.jsonl")
        mod.QUEUE = os.path.join(self.dir, "queue.jsonl")
        mod.STATE = os.path.join(self.dir, "state.json")
        mod.STORE = os.path.join(self.dir, "store.sqlite3")      # never opened: ingest and the index are recorders
        if hasattr(mod, "WRITE_LOCK"):
            mod.WRITE_LOCK = os.path.join(self.dir, "write.lock")
        rig = self

        def scan(verbose=True, since=None):
            if rig.on_scan:
                rig.on_scan()
            return {"AUTO": [(s, "test", "desc") for s in rig.slugs], "QUEUE": [], "SKIP": 0, "DONE": [], "UNREAD": 0}

        def ingest(slug, store=None, force=False, dry=False, rebuild=True):
            rig.events.append(("ingest", slug, rig.mod.hold_state()[0]))
            hook = rig.after_ingest.get(slug)
            if hook:
                hook()
            return True, "claim_" + slug

        mod.scan = scan
        mod.ingest = ingest
        mod.revisions = lambda since=None, store=None: []
        mod.stale_in_store = lambda store=None: []
        mod.rebuild_prefilter = lambda store=None: rig.events.append(("prefilter", "", rig.mod.hold_state()[0]))
        sys.modules["math_prefilter"] = types.SimpleNamespace(fresh_nodes=lambda store, limit=1: [])

        def extend(store):
            rig.events.append(("vectors", "", rig.mod.hold_state()[0]))
            return 0, 0, ""
        sys.modules["math_claim_vecs"] = types.SimpleNamespace(extend=extend)

    def set_hold(self):
        json.dump({"until": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time() + 3600)), "by": "test",
                   "why": "race control", "set_epoch": time.time()}, io.open(self.mod.HOLD, "w", encoding="utf-8"))

    def files(self):
        return sorted(f for f in ("ledger.jsonl", "queue.jsonl", "state.json") if os.path.exists(os.path.join(self.dir, f)))

    def ledger(self):
        p = self.mod.LEDGER
        return [json.loads(x) for x in io.open(p, encoding="utf-8")] if os.path.exists(p) else []

    def close(self):
        for m in ("math_prefilter", "math_claim_vecs"):
            sys.modules.pop(m, None)
        shutil.rmtree(self.dir, ignore_errors=True)


def quiet(fn, *a):
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fn(*a)
    return rc, buf.getvalue()


def main():
    args = sys.argv[1:]
    old = None
    if "--old" in args:
        i = args.index("--old")
        old = args[i + 1]
        del args[i:i + 2]
    path = args[0] if args else os.path.join(HERE, "math_transport.py")
    mod = load(path, "mt_under_test")
    print("transport under test: %s" % path)

    r = Rig(mod)
    try:
        r.on_scan = r.set_hold
        rc, out = quiet(mod.run)
        check("H1 a hold set during the scan: the run writes nothing",
              rc == 0 and not r.events and not r.files() and "HELD mid-run" in out,
              "rc %s, writes %s, files %s" % (rc, r.events, r.files()))
    finally:
        r.close()

    r = Rig(mod)
    try:
        r.after_ingest["m1"] = r.set_hold
        rc, out = quiet(mod.run)
        led = r.ledger()
        check("H2 a hold set between two memories: the first is written whole, nothing after it",
              [e[:2] for e in r.events] == [("ingest", "m1")] and [x["slug"] for x in led] == ["m1"]
              and not os.path.exists(mod.STATE),
              "writes %s, ledger %s, state %s" % (r.events, [x.get("slug") for x in led], os.path.exists(mod.STATE)))
    finally:
        r.close()

    r = Rig(mod, slugs=("m1",))
    try:
        r.after_ingest["m1"] = r.set_hold
        rc, out = quiet(mod.run)
        check("H3 a hold set before the index rebuild: no rebuild, no vectors, no state",
              [e[0] for e in r.events] == ["ingest"] and not os.path.exists(mod.STATE),
              "writes %s" % r.events)
    finally:
        r.close()

    if hasattr(mod, "_write_lock"):
        r = Rig(mod)
        try:
            released = {}
            started = threading.Event()

            def writer():
                with mod._write_lock():
                    started.set()
                    time.sleep(1.0)
                    released["t"] = time.time()
            t = threading.Thread(target=writer)
            t.start()
            started.wait(5)
            until = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time() + 3600))
            rc, out = quiet(mod.main, ["hold", until, "test", "a", "study"])
            landed = os.path.getmtime(mod.HOLD) if os.path.exists(mod.HOLD) else None
            t.join()
            check("H4 `hold` waits for a write in progress and lands after it",
                  rc == 0 and landed is not None and "t" in released and landed >= released["t"] - 0.05,
                  "rc %s, hold written %.3f s after the write ended" % (rc, (landed or 0) - released.get("t", 0)))
        finally:
            r.close()
    else:
        check("H4 `hold` waits for a write in progress and lands after it", False, "no write lock in this code")

    r = Rig(mod)
    try:
        rc, out = quiet(mod.run)
        kinds = [e[0] for e in r.events]
        check("H5 no hold: the run writes every memory, the index, the vectors and its state",
              rc == 0 and kinds == ["ingest", "ingest", "prefilter", "vectors"] and os.path.exists(mod.STATE),
              "writes %s, state %s" % (kinds, os.path.exists(mod.STATE)))
    finally:
        r.close()

    r = Rig(mod)
    try:
        before = {"last_run": "2026-09-29T10:00:00", "ingested": 0}
        json.dump(before, io.open(mod.STATE, "w", encoding="utf-8"))
        raw = io.open(mod.STATE, encoding="utf-8").read()
        r.after_ingest["m1"] = r.set_hold
        quiet(mod.run)
        check("H6 a held run leaves the state as it was, so the next run reads the same window again",
              io.open(mod.STATE, encoding="utf-8").read() == raw)
    finally:
        r.close()

    if hasattr(mod, "_write_lock"):
        r = Rig(mod)
        try:
            called = []
            mod.ingest = lambda slug, force=False, **k: (called.append(slug), (True, "claim_x"))[1]
            started = threading.Event()

            def writer():
                with mod._write_lock():
                    started.set()
                    time.sleep(0.6)
                    r.set_hold()
            t = threading.Thread(target=writer)
            t.start()
            started.wait(5)
            rc, out = quiet(mod.main, ["ingest", "m9"])
            t.join()
            check("H7 a manual ingest whose lock wait ends under a new hold is refused",
                  rc == 3 and not called and "HELD" in out, "rc %s, ingested %s" % (rc, called))
        finally:
            r.close()

    if old:
        omod = load(old, "mt_old")
        r = Rig(omod)
        try:
            r.on_scan = r.set_hold
            quiet(omod.run)
            wrote_held = [e for e in r.events if e[0] == "ingest" and e[2]]
            check("N1 the code before the fix writes with the hold in force (the finding)", bool(wrote_held),
                  "writes made while held: %s" % wrote_held)
        finally:
            r.close()
    print("%d failed" % len(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
