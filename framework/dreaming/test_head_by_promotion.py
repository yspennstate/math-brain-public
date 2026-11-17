"""test_head_by_promotion.py - a boosted ordinary hit stays in recall's body and a fresh attachment keeps its place above it
(28 Sep 2026).

    python test_head_by_promotion.py [--brain BRAIN.py] [--old OLD_BRAIN.py]

Runs in a throwaway memory folder with a shadow index (BRAIN_MEM_DIR, BRAIN_BM25_INDEX); the live store is never read or
written. The fixture is the audit's: a memory whose NAME is the query (so the name- and question-coverage boosts
multiply its bm25 score well past the lexical peak), and another memory with a fresh attachment that matches the query
(promoted into the head at the peak plus at most one).
 H1 the change on: the attachment's memory is shown above the boosted one, and the recall log puts the boosted one in
    the body, not the head
 H2 BRAIN_RECALL_HEAD_STRUCT=0: the boosted memory is shown first and sits in the head (the order before this change)
 H3 boosts off (BRAIN_RECALL_NAME_COVERAGE=0, BRAIN_RECALL_QCOVER=0): the change on and off show the same rows
With --old, the brain before this change must show the boosted memory first (the check can fail).
"""
import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import shutil
import stat
import sys
import tempfile
import time

if __name__ == "__main__" and ("-h" in sys.argv[1:] or "--help" in sys.argv[1:]):
    print(__doc__)
    sys.exit(0)

HERE = os.path.dirname(os.path.abspath(__file__))
_PLACEHOLDER = os.path.join(tempfile.gettempdir(), "head_promo_placeholder_never_created")
os.environ["BRAIN_MEM_DIR"] = os.path.join(_PLACEHOLDER, "memory")
os.environ["BRAIN_BM25_INDEX"] = os.path.join(_PLACEHOLDER, "bm25_index.json.gz")
ARGS = sys.argv[1:]
BRAIN = os.path.abspath(ARGS[ARGS.index("--brain") + 1]) if "--brain" in ARGS else os.path.join(HERE, "brain.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
PLAIN = re.compile(r"^\s*\d\.\d\d\s+\[[^\]]*\]\s+(\S+)", re.M)
Q = "quarterly granite ledger reconciliation"
NAMED = "quarterly_granite_ledger_reconciliation_2026_09_28"
ATTACHED = "project_notes_alpha_2026_09_28"
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


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    loader.exec_module(m)
    return m


class Store:
    def __init__(self):
        self.td = tempfile.mkdtemp(prefix="head_promo_")
        self.mem = os.path.join(self.td, "memory")
        os.makedirs(self.mem)
        os.environ.update(BRAIN_MEM_DIR=self.mem, BRAIN_BM25_INDEX=os.path.join(self.td, "bm25_index.json.gz"),
                          BRAIN_DOC_EXPANSION="0", BRAIN_RECALL_REFRESH="0", RECALL_REWRITE_NO_LOG="1",
                          BRAIN_RECALL_LOG="1", BRAIN_RECALL_LOG_FULL="1", BRAIN_GRAPH_LAMBDA="0.1",
                          BRAIN_RECALL_LOG_PATH=os.path.join(self.td, "recall_log.jsonl"))
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        self.nd = load(os.path.join(HERE, "brain_node_documents.py"), "brain_node_documents")
        self.bm25 = load(os.path.join(HERE, "bm25.py"), "bm25")
        assert os.path.abspath(self.bm25.MEM) == os.path.abspath(self.mem), self.bm25.MEM

    def memory(self, slug, body):
        with open(os.path.join(self.mem, slug + ".md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("---\nname: %s\ndescription: %s\nmetadata:\n  type: project\n---\n\n%s\n" % (slug, body[:60], body))
        old = time.time() - 7200
        os.utime(os.path.join(self.mem, slug + ".md"), (old, old))
        idx = os.path.join(self.mem, "MEMORY.md")
        lines = open(idx, encoding="utf-8").read().splitlines() if os.path.exists(idx) else ["# Memory Index"]
        lines = [l for l in lines if "(%s.md)" % slug not in l] + ["- [%s.md](%s.md) - %s" % (slug, slug, body[:120])]
        with open(idx, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines) + "\n")

    def close(self):
        rmtree(self.td)


def build_fixture():
    st = Store()
    fillers = ["harbor", "violet", "tundra", "cobalt", "meadow", "falcon", "saffron", "glacier", "orchid", "canyon",
               "lantern", "pebble", "thistle", "willow", "ember", "quartz", "mosaic", "nectar", "prairie", "zephyr"]
    for i, w in enumerate(fillers):
        st.memory("filler_%s_note_%02d_2026_09_28" % (w, i), "A note about %s and %s gardens, unrelated to accounts." % (w, w))
    st.memory(NAMED, "One line: the quarterly granite ledger reconciliation ran once in March.")
    st.memory(ATTACHED, "Alpha project notes, kept for the team, on several unrelated topics.")
    st.bm25.build(st.mem, os.environ["BRAIN_BM25_INDEX"])
    time.sleep(1.1)                                  # the attachment must be newer than the index's scan
    src = os.path.join(st.td, "alpha_full_notes.md")
    with open(src, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(("The quarterly granite ledger reconciliation: every step of the quarterly granite ledger "
                  "reconciliation, its inputs, its checks and its sign-off.\n") * 12)
    st.nd.attach(st.mem, ATTACHED, src, name="alpha_full_notes.md", description="full notes")
    return st


def recall(brain_path, tag, env):
    saved = {k: os.environ.get(k) for k in env}
    for k, v in env.items():
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v
    try:
        b = load(brain_path, "brain_head_%s" % tag)
        live = os.path.join(os.path.expanduser("~"), ".claude")
        for where in (b.MEM, sys.modules["bm25"].MEM, sys.modules["bm25"].INDEX):
            if os.path.abspath(where).lower().startswith(os.path.abspath(live).lower()):
                raise SystemExit("REFUSED: the recall under test would read the live store (%s)" % where)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                b.recall(Q, n=8)
            except SystemExit:
                pass
        shown = PLAIN.findall(buf.getvalue())
        log = os.environ["BRAIN_RECALL_LOG_PATH"]
        rec = [json.loads(l) for l in open(log, encoding="utf-8") if l.strip()][-1] if os.path.exists(log) else {}
        return shown, rec
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def pos(shown, slug):
    return shown.index(slug) if slug in shown else 99


def main():
    st = build_fixture()
    try:
        on, rec_on = recall(BRAIN, "on", {"BRAIN_RECALL_HEAD_STRUCT": "1"})
        body_on = [s for s, _ in rec_on.get("body") or []]
        check(pos(on, ATTACHED) < pos(on, NAMED) and NAMED in body_on,
              "H1 on: attachment at %d, boosted memory at %d; boosted memory in the logged body %s (crossed %s)" % (
                  pos(on, ATTACHED), pos(on, NAMED), NAMED in body_on, rec_on.get("crossed")))
        off, rec_off = recall(BRAIN, "off", {"BRAIN_RECALL_HEAD_STRUCT": "0"})
        body_off = [s for s, _ in rec_off.get("body") or []]
        check(pos(off, NAMED) < pos(off, ATTACHED) and NAMED not in body_off,
              "H2 off (the score line): boosted memory at %d, attachment at %d; boosted memory in the body %s" % (
                  pos(off, NAMED), pos(off, ATTACHED), NAMED in body_off))
        nb = {"BRAIN_RECALL_NAME_COVERAGE": "0", "BRAIN_RECALL_QCOVER": "0"}
        a, _ = recall(BRAIN, "nb_on", dict(nb, BRAIN_RECALL_HEAD_STRUCT="1"))
        b, _ = recall(BRAIN, "nb_off", dict(nb, BRAIN_RECALL_HEAD_STRUCT="0"))
        check(a == b and bool(a), "H3 boosts off: the change on and off show the same %d rows" % len(a))
        if OLD:
            old, _ = recall(OLD, "old", {"BRAIN_RECALL_HEAD_STRUCT": None})
            check(pos(old, NAMED) < pos(old, ATTACHED),
                  "N1 the brain before this change shows the boosted memory first (at %d, attachment at %d): the "
                  "crossing B01 found" % (pos(old, NAMED), pos(old, ATTACHED)))
    finally:
        st.close()
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
