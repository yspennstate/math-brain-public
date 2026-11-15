"""test_refill_ab_symmetry.py - the refill A/B's two arms are recorded the same way whatever happens after the arm is
chosen, the bookkeeping after the context goes out says when it fails, and the precision table is read once per call
(29 Sep 2026, an agent; scheduled audits account04/B04 r6 and r5, account04/B16 r11).

    python test_refill_ab_symmetry.py [--module INSTINCT_PRIME.py] [--old OLD_INSTINCT_PRIME.py]

Each case loads the module afresh with every file it writes in a temporary folder, a test reflex in the A/B (REFILL_AB),
and a ranked list of two ordinary reflexes and the A/B one; the second ordinary reflex is in its session backoff, so its
slot goes to the refill. Two sessions are chosen so that the A/B reflex is held in one and shown in the other.
 S1 a normal call: one refill row in each arm; the shown one reaches the fire log, the held one does not
 S2 _render raises: one refill row in each arm (the arm was decided), and the shown one is not in the fire log
 S3 the write to stdout raises: the same
 S4 the fire log's append fails: the context still goes out and instinct_emit_errors.tsv names fire_log
 S5 the backoff write fails: the context goes out and instinct_emit_errors.tsv names backoff
 S6 the process dies right after the fire log (the commit raises): the fire is on record
 S7 the precision table is parsed once over twenty reads, and again after it changes
With --old, the module before this change must leave the arms unequal in S2 and S3 (a held row, no shown row) and must
lose the fire in S6 (the checks can fail).
"""
import importlib.machinery
import importlib.util
import io
import json
import os
import shutil
import stat
import sys
import tempfile
import time

if __name__ == "__main__" and ("-h" in sys.argv[1:] or "--help" in sys.argv[1:]):
    print(__doc__)
    sys.exit(0)

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.abspath(sys.argv[sys.argv.index("--module") + 1]) if "--module" in sys.argv else os.path.join(HERE, "instinct_prime.py")
OLD = os.path.abspath(sys.argv[sys.argv.index("--old") + 1]) if "--old" in sys.argv else None
AB = "test_refill_ab_reflex"
N1 = {"id": "test_refill_normal_one", "gut": "The first ordinary test reflex, shown every time.", "sting": "t",
      "source": "test", "mode": "fire", "charge": 0.9}
N2 = {"id": "test_refill_normal_two", "gut": "The second ordinary test reflex, kept in its backoff.", "sting": "t",
      "source": "test", "mode": "fire", "charge": 0.8}
ABR = {"id": AB, "gut": "The A/B test reflex that fills the freed slot.", "sting": "t", "source": "test", "mode": "fire",
       "charge": 0.7}
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def rmtree(path):
    def clear(func, name, _exc):
        os.chmod(name, stat.S_IWRITE)
        func(name)
    shutil.rmtree(path, onexc=clear)


def load(path, td):
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    name = "ip_ab_%d" % len(ran)
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    m.STATE = os.path.join(td, "state.json")
    m.STATE_DIR = os.path.join(td, "state_dir")
    m.FIRELOG = os.path.join(td, "fires.tsv")
    m.SUPPRESSED_LOG = os.path.join(td, "suppressed.tsv")
    m.REFILL_LOG = os.path.join(td, "refills.tsv")
    m.EMIT_ERRORS = os.path.join(td, "emit_errors.tsv")
    m.PRECISION_PATH = os.path.join(td, "no_precision.json")
    m.REFILL_AB = (AB,)
    m._load = lambda *a, **k: []

    def fake_fire(*a, **k):
        m._LAST_RANKED[:] = [dict(N1), dict(N2), dict(ABR)]
        return [dict(N1), dict(N2)]
    m._fire = fake_fire
    m._augment_graph = lambda text, data, instincts, fired: fired
    m._exact_clause_context = lambda *a, **k: ""
    return m


def session_for(m, arm):
    for i in range(1, 5000):
        s = "%08x-0000-4000-8000-%012x" % (0xab00 + i, i)
        if m._refill_arm(s, AB) == arm:
            return s
    raise RuntimeError("no session for %s" % arm)


def seed_backoff(m, session):
    os.makedirs(m.STATE_DIR, exist_ok=True)
    with open(os.path.join(m.STATE_DIR, session + ".json"), "w", encoding="utf-8") as fh:
        json.dump({session + "|" + N2["id"]: [time.time() - 60, 1]}, fh)


class Boom(io.StringIO):
    def write(self, s):
        raise OSError("stdout closed")


def call(m, session, stdout=None):
    payload = json.dumps({"hook_event_name": "UserPromptSubmit", "session_id": session,
                          "prompt": "please look at the three test reflexes of this refill check"})
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(payload)
    sys.stdout = stdout if stdout is not None else io.StringIO()
    try:
        m.main()
        return sys.stdout.getvalue() if not isinstance(sys.stdout, Boom) else ""
    finally:
        sys.stdin, sys.stdout = old_in, old_out


def rows(path, rid, session):
    if not os.path.exists(path):
        return 0
    return sum(1 for l in open(path, encoding="utf-8") if rid in l and session in l)


def case(path, arm, mode):
    td = tempfile.mkdtemp(prefix="refill_ab_%s_%s_" % (arm, mode))
    try:
        m = load(path, td)
        s = session_for(m, arm)
        seed_backoff(m, s)
        if mode == "render":
            def bad(fired):
                raise RuntimeError("render failed")
            m._render = bad
            out = call(m, s)
        elif mode == "stdout":
            out = call(m, s, stdout=Boom())
        elif mode == "firelog":
            m._append_text = lambda *a, **k: False
            out = call(m, s)
        elif mode == "backoff":
            m._write_backoff = lambda *a, **k: False
            out = call(m, s)
        elif mode == "dies":
            def die(*a, **k):
                raise RuntimeError("the process died here")
            m._commit_backoff = die
            out = call(m, s)
        else:
            out = call(m, s)
        errs = open(m.EMIT_ERRORS, encoding="utf-8").read() if os.path.exists(m.EMIT_ERRORS) else ""
        return {"refill": rows(m.REFILL_LOG, AB, s), "fired_ab": rows(m.FIRELOG, AB, s), "fired_n1": rows(m.FIRELOG, N1["id"], s),
                "out": bool(out), "ab_in_out": ABR["gut"][:20] in out, "errs": errs}
    finally:
        rmtree(td)


def precision_reads(path):
    td = tempfile.mkdtemp(prefix="refill_prec_")
    try:
        m = load(path, td)
        m.PRECISION_PATH = os.path.join(td, "prec.json")
        with open(m.PRECISION_PATH, "w", encoding="utf-8") as fh:
            # built now: a table with no build stamp is ignored since 29 Sep (test_precision_gate.py)
            json.dump({"built": time.strftime("%Y-%m-%dT%H:%M:%S"),
                       "reflexes": {"x": {"n": 5, "on_domain": 4, "p": 0.7, "judged": True}}}, fh)
        count = [0]
        real = json.load

        def counting(fh, *a, **k):
            count[0] += 1
            return real(fh, *a, **k)
        m.json.load = counting
        try:
            got = [m._load_precision() for _ in range(20)]
            first = count[0]
            time.sleep(0.05)
            with open(m.PRECISION_PATH, "w", encoding="utf-8") as fh:
                json.dump({"built": time.strftime("%Y-%m-%dT%H:%M:%S"),
                           "reflexes": {"x": {"n": 6, "on_domain": 5, "p": 0.75, "judged": True}}}, fh)
            again = m._load_precision()
        finally:
            m.json.load = real
        return first, count[0], got[0].get("x", {}).get("n"), again.get("x", {}).get("n")
    finally:
        rmtree(td)


def main():
    s1h, s1s = case(MOD, "held", "normal"), case(MOD, "shown", "normal")
    check(s1h["refill"] == 1 and s1s["refill"] == 1 and s1s["fired_ab"] == 1 and s1h["fired_ab"] == 0 and s1s["ab_in_out"]
          and not s1h["ab_in_out"],
          "S1 normal call: refill rows held %d / shown %d; the shown one in the context %s and the fire log %d, the held "
          "one in neither (%s, %d)" % (s1h["refill"], s1s["refill"], s1s["ab_in_out"], s1s["fired_ab"], s1h["ab_in_out"],
                                       s1h["fired_ab"]))
    for mode, name in (("render", "S2 _render raises"), ("stdout", "S3 the write to stdout raises")):
        h, s = case(MOD, "held", mode), case(MOD, "shown", mode)
        check(h["refill"] == 1 and s["refill"] == 1 and s["fired_ab"] == 0,
              "%s: refill rows held %d / shown %d, the shown one in the fire log %d" % (name, h["refill"], s["refill"],
                                                                                      s["fired_ab"]))
    x = case(MOD, "shown", "firelog")
    check(x["out"] and x["fired_n1"] == 0 and "fire_log" in x["errs"],
          "S4 the fire log's append fails: context out %s, emit errors name fire_log (%r)" % (x["out"], x["errs"].strip()))
    x = case(MOD, "shown", "backoff")
    check(x["out"] and "backoff" in x["errs"] and x["fired_n1"] == 1,
          "S5 the backoff write fails: context out %s, fire rows %d, emit errors name backoff (%r)" % (
              x["out"], x["fired_n1"], x["errs"].strip()))
    x = case(MOD, "shown", "dies")
    check(x["fired_n1"] == 1 and x["fired_ab"] == 1,
          "S6 the process dies after the fire log: fires on record %d, %d" % (x["fired_n1"], x["fired_ab"]))
    first, total, n0, n1 = precision_reads(MOD)
    check(first == 1 and total == 2 and n0 == 5 and n1 == 6,
          "S7 precision table: parsed %d time(s) over 20 reads, %d after it changed (n %s -> %s)" % (first, total, n0, n1))
    if OLD:
        for mode, name in (("render", "N1 S2"), ("stdout", "N2 S3")):
            h, s = case(OLD, "held", mode), case(OLD, "shown", mode)
            check(h["refill"] != s["refill"],
                  "%s on the module before this change: refill rows held %d / shown %d (unequal; the check can fail)" % (
                      name, h["refill"], s["refill"]))
        x = case(OLD, "shown", "dies")
        check(x["fired_n1"] == 0,
              "N3 S6 on the module before this change: the fire is lost (%d rows; the check can fail)" % x["fired_n1"])
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
