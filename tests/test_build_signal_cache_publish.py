"""The signal-cache builder publishes only whole caches, one temporary file per writer.

Interactive audit 20260929T154310Z, INT-R79-SIGNAL-CACHE-SHARED-TEMP-20260929: every build wrote through one fixed name,
so a second builder opening it truncated the first builder's finished file and the first published a zero-byte cache.
These tests run the builder's main() on a fake store in a temporary folder (nothing real is read or written).

    python tests/test_build_signal_cache_publish.py [--old OLD_build_signal_cache.py]

  P1 two builders whose writes overlap: both finish, the published cache loads whole, no temporary file is left
  P2 a build that fails while writing: the old cache is untouched, no temporary file is left
  P3 another writer's temporary file in the folder: left alone
  P4 a replace refused twice (a reader holding the file, as Windows does): retried, then published
With --old, the builder given must fail P1's overlap (N1): an exception or a published cache that does not load whole.
"""
import importlib.util
import os
import pickle
import sys
import tempfile
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "src"
sys.path.insert(0, str(SRC))
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


class Node:
    def __init__(self, i):
        self.title, self.body = "title %d" % i, "body text number %d" % i


class FakeStore:
    def __init__(self, path):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def iter_nodes(self):
        return [Node(i) for i in range(200)]


def load_builder(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.ResearchStore = FakeStore
    m._index_signals_uncached = lambda text: ("signals", text)
    return m


def setup(m, folder):
    m.STORE = Path(folder) / "brain.sqlite3"
    m.CACHE = Path(folder) / "brain_signal_cache.pkl"
    return m.CACHE


def loads_whole(p):
    try:
        with open(p, "rb") as fh:
            d = pickle.load(fh)
        return isinstance(d, dict) and len(d) == 200
    except Exception:
        return False


def overlap(path, tag):
    """Builder A finishes writing; builder B then opens its temporary file; only then does A publish; then B finishes."""
    folder = tempfile.mkdtemp(prefix="sigcache_%s_" % tag)
    a_written, b_opened = threading.Event(), threading.Event()
    real_dump = pickle.dump
    errors = {}
    ma, mb = load_builder(path, "bsc_a_" + tag), load_builder(path, "bsc_b_" + tag)
    for m in (ma, mb):
        setup(m, folder)

    class GatePickle:
        def __init__(self, role):
            self.role = role

        def dump(self, obj, fh, protocol=None):
            if self.role == "b":
                b_opened.set()                      # B's file is open (and, with a shared name, A's is truncated)
                time.sleep(0.5)                     # B keeps it open while A publishes: on Windows A's replace is then
                #                                     refused (PermissionError); on POSIX A publishes the truncated file
            real_dump(obj, fh, protocol=protocol)
            if self.role == "a":
                a_written.set()
                b_opened.wait(10)                   # A publishes only after B has opened its temporary file

        def load(self, fh):
            return pickle.load(fh)

        HIGHEST_PROTOCOL = pickle.HIGHEST_PROTOCOL
        UnpicklingError = pickle.UnpicklingError

    ma.pickle, mb.pickle = GatePickle("a"), GatePickle("b")

    def run(m, role):
        try:
            if role == "b":
                a_written.wait(10)
            m.main()
        except Exception as exc:                    # noqa: BLE001 - the outcome is what is checked
            errors[role] = repr(exc)
    ta, tb = threading.Thread(target=run, args=(ma, "a")), threading.Thread(target=run, args=(mb, "b"))
    ta.start()
    tb.start()
    ta.join(30)
    tb.join(30)
    left = [f for f in os.listdir(folder) if f.endswith(".tmp")]
    ok = loads_whole(ma.CACHE)
    return errors, ok, left


def main():
    new = HERE.parent / "src" / "math_brain" / "build_signal_cache.py"
    errors, ok, left = overlap(new, "new")
    check(not errors and ok and not left, "P1 two overlapping builders: errors %s, published cache whole %s, temporary files left %s"
          % (errors, ok, left))

    folder = tempfile.mkdtemp(prefix="sigcache_fail_")
    m = load_builder(new, "bsc_fail")
    cache = setup(m, folder)
    with open(cache, "wb") as fh:
        pickle.dump({"old": 1}, fh)
    before = cache.read_bytes()

    class Boom:
        HIGHEST_PROTOCOL = pickle.HIGHEST_PROTOCOL

        def dump(self, obj, fh, protocol=None):
            fh.write(b"partial")
            raise OSError("disk full")
    m.pickle = Boom()
    try:
        m.main()
        raised = False
    except OSError:
        raised = True
    left = [f for f in os.listdir(folder) if f.endswith(".tmp")]
    check(raised and cache.read_bytes() == before and not left,
          "P2 a build failing mid-write: raised %s, old cache untouched %s, temporary files left %s"
          % (raised, cache.read_bytes() == before, left))

    folder = tempfile.mkdtemp(prefix="sigcache_foreign_")
    m = load_builder(new, "bsc_foreign")
    cache = setup(m, folder)
    foreign = Path(folder) / (cache.name + ".someoneelse.tmp")
    foreign.write_bytes(b"another writer's work")
    m.main()
    check(foreign.exists() and loads_whole(cache), "P3 another writer's temporary file left alone: %s" % foreign.exists())

    folder = tempfile.mkdtemp(prefix="sigcache_retry_")
    m = load_builder(new, "bsc_retry")
    cache = setup(m, folder)
    refusals = {"n": 0}
    real_replace = os.replace

    def flaky(src, dst):
        if refusals["n"] < 2:
            refusals["n"] += 1
            raise PermissionError("the destination is open")
        return real_replace(src, dst)
    import math_brain.build_signal_cache  # noqa: F401  (the name must be importable; the patch goes on os below)
    os.replace = flaky
    try:
        m.main()
    finally:
        os.replace = real_replace
    check(refusals["n"] == 2 and loads_whole(cache), "P4 a replace refused twice, then published: %d refusals, whole %s"
          % (refusals["n"], loads_whole(cache)))

    if "--old" in sys.argv:
        old = Path(sys.argv[sys.argv.index("--old") + 1])
        errors, ok, left = overlap(old, "old")
        check(bool(errors) or not ok,
              "N1 the builder given fails the overlap: errors %s, published cache whole %s (the check can fail)" % (errors, ok))
    print("%s - %d cases, %d failed" % ("FAIL" if fails else "PASS", len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
