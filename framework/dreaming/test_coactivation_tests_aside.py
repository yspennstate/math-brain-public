"""Controls for coactivation_end.py's test-worker filter (27 Sep, an agent). Temporary folders only.

    python test_coactivation_tests_aside.py
"""
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import time

DR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.expanduser("~"), ".claude", "brain_graph", "bin"))
import session_kinds as sk  # noqa: E402

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


def transcript(path, entry, first):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"type": "system", "entrypoint": entry}) + "\n")
        fh.write(json.dumps({"type": "user", "entrypoint": entry, "message": {"role": "user", "content": first}}) + "\n")


def load_copy(tmp, logdir, tsv, foldlog):
    """A copy of the hook pointed at temporary files. fold_targets takes its table and audit paths as DEFAULT
    arguments, bound when the module loads, so reassigning the module's constants afterwards does not move them: the
    first version of this test did exactly that and folded two fake pairs into the live table (27 Sep 06:39, removed
    by hand). The paths are therefore passed explicitly, and the live table's stamp is compared before and after."""
    import functools
    shutil.copy(os.path.join(DR, "coactivation_end.py"), os.path.join(tmp, "coactivation_end.py"))
    spec = importlib.util.spec_from_file_location("coact_copy_%d" % len(os.listdir(tmp)),
                                                  os.path.join(tmp, "coactivation_end.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.LOGDIR, m.TSV, m.LOCK, m.FOLDLOG, m.TEST_ARCHIVE = logdir, tsv, tsv + ".lock", foldlog, logdir + "_tests"
    m.fold_targets = functools.partial(m.fold_targets, tsv=tsv, foldlog=foldlog)
    return m


def _live_stamp():
    live = os.path.join(DR, "coactivation.tsv")
    try:
        st = os.stat(live)
        return (st.st_size, st.st_mtime_ns)
    except OSError:
        return None


def main():
    before = _live_stamp()
    tmp = tempfile.mkdtemp(prefix="coact_test_")
    live_sk = (sk.PROJECTS, sk.CODEX, sk.CACHE)
    try:
        proj = os.path.join(tmp, "projects", "C--work")
        os.makedirs(proj)
        his = "a" * 8 + "-aaaa-4aaa-8aaa-000000000000"
        test = "b" * 8 + "-aaaa-4aaa-8aaa-000000000000"
        orphan_test = "c" * 8 + "-aaaa-4aaa-8aaa-000000000000"
        transcript(os.path.join(proj, his + ".jsonl"), "cli", "prove the lemma")
        transcript(os.path.join(proj, test + ".jsonl"), "sdk-cli", "[headless-worker] QUESTION rec_01_02")
        transcript(os.path.join(proj, orphan_test + ".jsonl"), "sdk-cli", "[headless-worker] QUESTION rec_03_04")
        sk.PROJECTS, sk.CODEX, sk.CACHE = os.path.join(tmp, "projects"), os.path.join(tmp, "codex"), os.path.join(tmp, "k.json")
        sk.reset()
        logdir = os.path.join(tmp, "coactivation_session")
        os.makedirs(logdir)
        m = load_copy(tmp, logdir, os.path.join(tmp, "coactivation.tsv"), os.path.join(tmp, "folds.log"))
        for sid, slugs in ((his, ["mem_a", "mem_b"]), (test, ["gold_x", "gold_y"]), (orphan_test, ["gold_p", "gold_q"])):
            with open(os.path.join(logdir, sid + ".log"), "w", encoding="utf-8") as fh:
                fh.write("\n".join(slugs) + "\n")
        old = time.time() - 7 * 3600
        os.utime(os.path.join(logdir, orphan_test + ".log"), (old, old))
        # the test worker's own Stop: its log is set aside, nothing folds, the table is untouched
        sys.stdin = io.StringIO(json.dumps({"session_id": test}))
        m.main()
        check("1 a test worker's own Stop folds nothing", not os.path.exists(m.TSV))
        check("2 its log is kept whole in the archive, not deleted",
              os.path.exists(os.path.join(m.TEST_ARCHIVE, test + ".log"))
              and open(os.path.join(m.TEST_ARCHIVE, test + ".log"), encoding="utf-8").read().split() == ["gold_x", "gold_y"])
        # his Stop: his log folds, the old orphan worker log is set aside, not folded
        sys.stdin = io.StringIO(json.dumps({"session_id": his}))
        m.main()
        rows = [l.rstrip("\n").split("\t") for l in open(m.TSV, encoding="utf-8")] if os.path.exists(m.TSV) else []
        pairs = {(r[0], r[1]) for r in rows[1:] if r and not r[0].startswith("#")}
        check("3 his co-read folds", ("mem_a", "mem_b") in pairs, str(pairs))
        check("4 no worker pair enters the table", not any("gold" in a or "gold" in b for a, b in pairs), str(pairs))
        check("5 an orphaned worker log is set aside too",
              os.path.exists(os.path.join(m.TEST_ARCHIVE, orphan_test + ".log"))
              and not os.path.exists(os.path.join(logdir, orphan_test + ".log")))
        check("6 his log is consumed as before", not os.path.exists(os.path.join(logdir, his + ".log")))
        # fail-open: if the classifier cannot be imported, the fold behaves exactly as before
        m2 = load_copy(tmp, logdir, os.path.join(tmp, "coactivation2.tsv"), os.path.join(tmp, "folds2.log"))
        m2._is_test_session = lambda sid: False
        with open(os.path.join(logdir, test + ".log"), "w", encoding="utf-8") as fh:
            fh.write("gold_x\ngold_y\n")
        sys.stdin = io.StringIO(json.dumps({"session_id": test}))
        m2.main()
        rows2 = [l.rstrip("\n").split("\t") for l in open(m2.TSV, encoding="utf-8")] if os.path.exists(m2.TSV) else []
        check("7 without the classifier the old behaviour holds (the pair folds)",
              any(r[:2] == ["gold_x", "gold_y"] for r in rows2), str(rows2))
    finally:
        sys.stdin = sys.__stdin__
        sk.PROJECTS, sk.CODEX, sk.CACHE = live_sk
        sk.reset()
        shutil.rmtree(tmp, ignore_errors=True)
    check("8 the live table was not touched", _live_stamp() == before)
    print("%d of 8 controls pass" % (8 - len(FAILS)))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
