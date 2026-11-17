"""test_attachment_freshness.py - an attachment-only change reaches the BM25 index at the next refresh, and brain.py's
live promotion of that attachment lasts until it does (28 Sep 2026).

    python test_attachment_freshness.py [BM25.py] [--brain BRAIN.py] [--old OLD_BM25.py]

Runs in a throwaway memory folder with a shadow index (BRAIN_MEM_DIR, BRAIN_BM25_INDEX; the live store is never read or
written). Eight memories are indexed; memory P then gets an attachment carrying words no memory holds; a minute's worth
of other work is stood in for by editing an unrelated memory and refreshing the index, as the 15-minute refresh would.
B02's invariant: at every moment P is either promoted by brain.py's attachment gate or its index entry holds the
attachment's words, never neither (neither is the rank-1-to-rank-9 drop B02 measured).
 F1 after the attachment is written, fresh_memories names P
 F2 after the unrelated refresh, P's index entry holds the attachment's words
 F3 the invariant holds after the attachment (promoted) and after the refresh (indexed)
 F4 brain.py's gate compares the attachment with bm25.scan_reference, not with the index file's mtime
With --old (the bm25.py before this change, judged with the gate brain.py had then), F1 and F3 must fail.
"""
import importlib.machinery
import importlib.util
import os
import shutil
import stat
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = [a for a in sys.argv[1:]]
BM = os.path.abspath(ARGS[0]) if ARGS and not ARGS[0].startswith("--") else os.path.join(HERE, "bm25.py")
BRAIN = os.path.abspath(ARGS[ARGS.index("--brain") + 1]) if "--brain" in ARGS else os.path.join(HERE, "brain.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
WORDS = "quokkazanzibar fjordwhistle"
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
    loader.exec_module(m)
    return m


def write_memory(mem, slug, body):
    with open(os.path.join(mem, slug + ".md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("---\nname: %s\ndescription: %s\nmetadata:\n  type: project\n---\n\n%s\n" % (slug, body[:60], body))


def scenario(bm_path, gate, tag):
    td = tempfile.mkdtemp(prefix="attach_fresh_")
    try:
        mem = os.path.join(td, "memory")
        os.makedirs(mem)
        os.environ["BRAIN_MEM_DIR"] = mem
        os.environ["BRAIN_BM25_INDEX"] = os.path.join(td, "bm25_index.json.gz")
        os.environ["BRAIN_DOC_EXPANSION"] = "0"
        sys.path.insert(0, HERE)
        import brain_node_documents as nd
        bm = load(bm_path, "bm25_under_test_%s" % tag)
        index = os.environ["BRAIN_BM25_INDEX"]
        topics = ["rebalance clock", "grid inventory", "voice narration", "reflex anchors", "mesh claims",
                  "secret scan", "quota parity", "attachment bundles"]
        slugs = ["m%d_fixture_memory_2026_09_28" % i for i in range(8)]
        old = time.time() - 7200    # written two hours before the build: outside the index's one-minute margin, so
        for s, t in zip(slugs, topics):   # only what changes after the build can look fresh
            write_memory(mem, s, "A note about %s and nothing else." % t)
            os.utime(os.path.join(mem, s + ".md"), (old, old))
        bm.build(mem, index)
        p, other = slugs[2], slugs[6]
        time.sleep(1.2)
        src = os.path.join(td, "notes.md")
        with open(src, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("Full notes: %s appear only here.\n" % WORDS)
        nd.attach(mem, p, src, name="notes.md", description="full notes")
        words = set(bm.tokens(WORDS))
        fresh1, _gone = bm.fresh_memories(mem, index)
        tf1 = bm._load_payload(index)["tf"].get(p, {})
        state1 = {"fresh_names_p": p in fresh1, "gate": gate(bm, nd, mem, index, p), "indexed": words <= set(tf1)}
        time.sleep(1.2)
        write_memory(mem, other, "A note about secret scan, edited later.")
        bm.refresh(mem, index, quiet=True)
        tf2 = bm._load_payload(index)["tf"].get(p, {})
        state2 = {"gate": gate(bm, nd, mem, index, p), "indexed": words <= set(tf2)}
        return state1, state2
    finally:
        sys.path.remove(HERE) if HERE in sys.path else None
        rmtree(td)


def new_gate(bm, nd, mem, index, slug):
    return nd.newest_attachment_mtime(mem, slug) >= bm.scan_reference(index)


def old_gate(bm, nd, mem, index, slug):
    return nd.newest_attachment_mtime(mem, slug) > os.path.getmtime(index)


def verdict(s1, s2):
    return (s1["gate"] or s1["indexed"]) and (s2["gate"] or s2["indexed"])


def main():
    s1, s2 = scenario(BM, new_gate, "new")
    check(s1["fresh_names_p"], "F1 the attachment written after the build: fresh_memories names its parent %s" % s1["fresh_names_p"])
    check(s2["indexed"], "F2 after an unrelated edit and refresh, the parent's index entry holds the attachment's words %s"
          % s2["indexed"])
    check(verdict(s1, s2), "F3 promoted or indexed at every moment: after the attachment gate %s / indexed %s; after the "
          "refresh gate %s / indexed %s" % (s1["gate"], s1["indexed"], s2["gate"], s2["indexed"]))
    src = open(BRAIN, encoding="utf-8").read()
    check("_bm25_scan_reference(_bm25_index_path)" in src and "newest_attachment_mtime(MEM, slug) >= _index_read" in src,
          "F4 brain.py's gate reads bm25.scan_reference")
    if OLD:
        o1, o2 = scenario(OLD, old_gate, "old")
        check(not o1["fresh_names_p"] and not verdict(o1, o2),
              "N1 the bm25 before this change, with the gate brain.py had then, fails F1 and F3 (the check can fail): "
              "fresh names the parent %s; after the refresh gate %s / indexed %s" % (
                  o1["fresh_names_p"], o2["gate"], o2["indexed"]))
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
