"""test_math_integrity_api_generations.py - the math hook asks each math_brain package for "a refused card refuses the
block" in that package's own form, and serves nothing when a package offers neither form (29 Sep 2026).

    python test_math_integrity_api_generations.py [MATH_SENSE.py] [--old OLD_MATH_SENSE.py]

The hook stays fixed and the package varies (B02's T7): three copies of math_brain in a temporary folder, alike except
selection_integrity.py - the current one (on_refusal, with "all"), the one of 7282e5a080 (strict) and the one before it
(neither). Each case runs in its own process, in shadow mode, on the live store (read-only), with the integrity read made
to refuse a chosen card.
 G1  current package: no card refused serves the block; a refused first or last card serves nothing (T1)
 G2  the 7282 package: the hook passes strict=True; a refused first or last card serves nothing; no refusal serves (T2)
 G3  the package with neither form: nothing is served and the silence says integrity_api_incompatible (T3)
 G4  with no card refused, the current and the 7282 packages serve the same block (T4)
 G5  the grace route (the first read runs out of time): a refused top card serves nothing under the current and 7282
     packages, and the package with neither stops before the read (T5)
 G6  --query: the current and 7282 packages print a block, the package with neither prints nothing (T6)
With --old, the hook before this change serves the runner-up over the 7282 package when the first card is refused (N1)
and serves over the package with neither form (N2): the defect B02 found.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
MS = os.path.abspath(ARGS[0]) if ARGS and not ARGS[0].startswith("--") else os.path.join(HERE, "math_sense.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
REPO = r"~\math-brain-build"
DREAMING = os.path.join(os.path.expanduser("~"), ".claude", "dreaming")
QUESTION = "Is every group of prime order cyclic, and how does Lagrange's theorem give that?"
# --query selects without the hook's prefilter, and over QUESTION it selects a card the integrity read refuses (one of the
# store's cards whose stored digest no longer matches), so the block is refused there by design; G6 asks this instead
QUERY_Q = ("What does the Banach fixed point theorem say about a contraction mapping on a complete metric space, and why is "
           "the fixed point unique?")
STRICT_REV, NEITHER_REV = "7282e5a080", "7282e5a080^"
fails, ran = [], []

CHILD = r'''
import functools, hashlib, importlib.machinery, importlib.util, io, json, os, sys
hook, pkg, dreaming, which, exhaust, route, question = sys.argv[1:8]
exhaust = exhaust == "1"
os.environ["MATHBRAIN_SHADOW"] = "1"
os.environ["MATHBRAIN_USE_LOG"] = "0"
# the live store, named: a copied package would otherwise look for its vectors beside its own folder
os.environ["MATHBRAIN_STORE"] = "~/math-brain-build/local/population/brain.sqlite3"
sys.path[:0] = [pkg, os.path.dirname(hook), dreaming]
import math_brain.selection_integrity as SI
from math_brain.current_note import NoteReadError, read_current_note
real = SI.consistent_hits
given = []

@functools.wraps(real)                      # keep the package's own signature: the hook reads it
def refusing(hits, database, **kw):
    hits = list(hits)
    given.append({"n": len(hits), "form": {k: v for k, v in kw.items() if k in ("strict", "on_refusal")}})
    if exhaust and len(given) == 1:
        raise SI.SelectionUnavailable("integrity_budget_exhausted")
    refused = set()
    if which == "first" and hits:
        refused = {hits[0].node.id}
    elif which == "last" and hits:
        refused = {hits[-1].node.id}
    def read(db, node_id, artifact_root=None):
        if node_id in refused:
            raise NoteReadError("stored_node_digest_mismatch")
        return read_current_note(db, node_id, artifact_root=artifact_root)
    return real(hits, database, reader=read, **kw)

SI.consistent_hits = refusing
loader = importlib.machinery.SourceFileLoader("ms_gen", hook)
spec = importlib.util.spec_from_file_location("ms_gen", hook, loader=loader)
m = importlib.util.module_from_spec(spec)
loader.exec_module(m)
m.BUILD_SRC = pkg
reasons = []
m._silence_note = lambda data, reason, harness_only=False: reasons.append(reason)
out = io.StringIO()
real_out = sys.stdout
sys.stdout = out
try:
    if route == "hook":
        sys.stdin = io.StringIO(json.dumps({"prompt": question, "session_id": "r78gen-" + which}))
        try:
            m.main()
        except SystemExit:
            pass
    else:
        m.cli_query(question)
finally:
    sys.stdout = real_out
text = out.getvalue()
print(json.dumps({"served": bool(text.strip()), "chars": len(text), "sha": hashlib.sha256(text.encode()).hexdigest()[:16],
                  "reasons": reasons, "given": given, "si": SI.__file__}))
'''


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def package(root, name, rev):
    """A copy of this checkout's math_brain whose selection_integrity.py is the one at rev (None: the current file)."""
    d = os.path.join(root, name)
    shutil.copytree(os.path.join(REPO, "src", "math_brain"), os.path.join(d, "math_brain"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.bak*", "*.CANDIDATE*", "*.LANDING*", "*.PRE_*"))
    if rev:
        src = subprocess.run(["git", "-C", REPO, "show", "%s:src/math_brain/selection_integrity.py" % rev],
                             capture_output=True, check=True).stdout
        with open(os.path.join(d, "math_brain", "selection_integrity.py"), "wb") as fh:
            fh.write(src)
    return d


def run(child, hook, pkg, which=None, exhaust=False, route="hook", question=QUESTION):
    r = subprocess.run([sys.executable, child, hook, pkg, DREAMING, which or "none", "1" if exhaust else "0", route,
                        question], capture_output=True, text=True, timeout=300,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    try:
        return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception:
        return {"served": None, "error": (r.stderr or r.stdout)[-400:], "reasons": [], "given": []}


def refused(res):
    return not res.get("served") and any("selected_card_refused" in x for x in res.get("reasons") or [])


def main():
    tmp = tempfile.mkdtemp(prefix="r78_generations_")
    try:
        child = os.path.join(tmp, "child.py")
        with open(child, "w", encoding="utf-8") as fh:
            fh.write(CHILD)
        cur = package(tmp, "current", None)
        strict = package(tmp, "strict", STRICT_REV)
        neither = package(tmp, "neither", NEITHER_REV)
        r_none, r_first, r_last = (run(child, MS, cur, w) for w in (None, "first", "last"))
        check(r_none.get("served") and r_none["given"] and r_none["given"][0]["form"] == {"on_refusal": "all"}
              and refused(r_first) and refused(r_last) and r_none.get("si", "").startswith(cur),
              "G1 current package (on_refusal=all): served with no refusal (%s chars), silent on a refused first %s and "
              "last %s" % (r_none.get("chars"), refused(r_first), refused(r_last)))
        s_none, s_first, s_last = (run(child, MS, strict, w) for w in (None, "first", "last"))
        check(s_none.get("served") and s_none["given"] and s_none["given"][0]["form"] == {"strict": True}
              and refused(s_first) and refused(s_last),
              "G2 the 7282 package: the hook passes %s; served with no refusal, silent on a refused first %s and last %s"
              % ((s_none.get("given") or [{}])[0].get("form"), refused(s_first), refused(s_last)))
        n_none = run(child, MS, neither)
        check(not n_none.get("served") and "integrity_api_incompatible" in (n_none.get("reasons") or [])
              and n_none.get("given") == [],
              "G3 the package with neither form: nothing served, silence %r, the read never called (%s)"
              % ((n_none.get("reasons") or [])[-1:], n_none.get("given")))
        check(r_none.get("sha") == s_none.get("sha") and r_none.get("served"),
              "G4 no card refused: the current and 7282 packages serve the same block (%s / %s)"
              % (r_none.get("sha"), s_none.get("sha")))
        g_cur = run(child, MS, cur, "first", exhaust=True)
        g_str = run(child, MS, strict, "first", exhaust=True)
        g_nei = run(child, MS, neither, "first", exhaust=True)
        check(refused(g_cur) and refused(g_str) and len(g_cur["given"]) == 2 and len(g_str["given"]) == 2
              and not g_nei.get("served") and "integrity_api_incompatible" in (g_nei.get("reasons") or []),
              "G5 the grace route with the top card refused: silent under current %s and 7282 %s; the package with "
              "neither stops first %s" % (refused(g_cur), refused(g_str),
                                          "integrity_api_incompatible" in (g_nei.get("reasons") or [])))
        q_cur, q_str, q_nei = (run(child, MS, p, None, route="cli", question=QUERY_Q) for p in (cur, strict, neither))
        check(q_cur.get("served") and q_str.get("served") and not q_nei.get("served") and q_nei.get("given") == [],
              "G6 --query: the current package prints %s chars, the 7282 package %s, the package with neither nothing "
              "(%s)" % (q_cur.get("chars"), q_str.get("chars"), q_nei.get("served")))
        if OLD:
            o_first = run(child, OLD, strict, "first")
            check(o_first.get("served") is True and (o_first.get("given") or [{}])[0].get("form") == {},
                  "N1 the hook before this change passes no form to the 7282 package and serves when the first card is "
                  "refused (%s chars)" % o_first.get("chars"))
            o_nei = run(child, OLD, neither)
            check(o_nei.get("served") is True,
                  "N2 the hook before this change serves over the package with neither form (%s chars)"
                  % o_nei.get("chars"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
