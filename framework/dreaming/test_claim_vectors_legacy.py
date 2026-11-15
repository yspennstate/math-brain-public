"""test_claim_vectors_legacy.py - a claim vector of unknown text is not bound to its claim (29 Sep 2026, an agent;
scheduled audits account04/B06 r76 and account04/B14 r8).

    python test_claim_vectors_legacy.py [--hook MATH_SENSE.py] [--vecs MATH_CLAIM_VECS.py] [--src MATH_BRAIN_SRC]
                                        [--old-hook OLD.py] [--old-vecs OLD.py] [--old-src OLD_SRC]

Fixture stores and vector files live in a temporary folder; the live store and its vectors are never opened.
 L1  a bound file with one legacy row: coverage counts it missing, status is not ok and names it, the hook names nobody
     and the vouch agrees with nothing (T-R76-LEGACY-CLOSES)
 L2  the same file with that row made from its text: the hook names its winner (T-R76-VERIFIED-OPENS)
 L3  one row made from its text and one legacy row: the whole channel stays closed (T-R76-MIXED)
 L4  a legacy row of a superseded claim closes it too (T-R76-SUPERSESSION)
 L5  rebuild(): the legacy row re-embedded from its current text, the other rows byte for byte, digest and source
     recorded; a second run writes nothing; the hook then names its winner (T-R76-REBUILD)
 L6  rebuild(out=...) writes the rebuilt file there and leaves the live one byte-identical
 L7  rebuild() leaves a file that does not record its row sources for migrate()
 L8  extend() re-embeds a legacy row as it re-embeds a row whose text changed
 L9  migrate() on an unbound file whose vector no text of its claim reproduces records the row legacy, and the hook
     refuses it (T-R76-DIGEST-COPY, at the writer: a current digest beside another vector does not make it bound)
 L10 the loader reads row_source into _sources, and refuses a value outside body/title/title body/legacy and a count
     that is not the file's (T-R76-LOADER)
With --old-hook and --old-vecs, the hook and the module before this change pass a file with a legacy row (N1, N2); with
--old-src, the loader before it does not read row_source (N3). Each shows its check can fail.
"""
import hashlib
import importlib.machinery
import importlib.util
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import types

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]


def _arg(flag, default=None):
    return os.path.abspath(ARGS[ARGS.index(flag) + 1]) if flag in ARGS else default


HOOK = _arg("--hook", os.path.join(HERE, "math_sense.py"))
VECS = _arg("--vecs", os.path.join(HERE, "math_claim_vecs.py"))
SRC = _arg("--src", r"~\math-brain-build\src")
OLD_HOOK, OLD_VECS, OLD_SRC = _arg("--old-hook"), _arg("--old-vecs"), _arg("--old-src")
DREAMING = os.path.join(os.path.expanduser("~"), ".claude", "dreaming")   # the hook's sibling modules
sys.path.insert(0, DREAMING)
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


OLD_CARD, SIDE = "claim_old_prime_order_is_cyclic", "claim_side_lagrange"
BODY = {OLD_CARD: "every group of prime order is cyclic", SIDE: "the order of a subgroup divides the order"}
EMB = {BODY[OLD_CARD]: [0.8, 0.6], BODY[SIDE]: [0.0, 1.0]}
UNKNOWN = [0.95, 0.31]          # a vector no text of OLD_CARD reproduces (cosine 0.95 with its body)
Q = [1.0, 0.0]


def node_digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]


def fake_embed(text):
    v = EMB.get(text)
    return None if v is None else np.asarray(v, dtype=np.float32)


def make_store(folder, claims, superseded=()):
    path = os.path.join(folder, "brain.sqlite3")
    if os.path.exists(path):
        os.remove(path)
    con = sqlite3.connect(path)
    con.executescript("create table nodes (id text primary key, kind text, title text, body text, digest text);"
                      "create table claims (id text primary key);"
                      "create table edges (kind text, source_id text, target_id text);")
    for c in claims:
        con.execute("insert into nodes values (?, 'claim', ?, ?, ?)", (c, c, BODY[c], node_digest(BODY[c])))
        con.execute("insert into claims values (?)", (c,))
    for old in superseded:
        con.execute("insert into edges values ('supersedes', ?, ?)", ("x_" + old, old))
    con.commit()
    con.close()
    return path


def make_vectors(folder, sources, name="claim_embeddings.npz", bound=True, vec_of=None):
    """A file of OLD_CARD and SIDE; a row whose source is legacy holds UNKNOWN, the others their body's vector; bound
    records each row's current store digest (as migrate() writes it, legacy rows included)."""
    ids = [OLD_CARD, SIDE]
    vec_of = vec_of or {}
    vecs = [vec_of.get(i, UNKNOWN if s == "legacy" else EMB[BODY[i]]) for i, s in zip(ids, sources)]
    fields = dict(slugs=np.array(ids), vecs=np.asarray(vecs, dtype=np.float32), model=np.array("BAAI/bge-small-en-v1.5"),
                  text_sha256=np.array("ext:0000"), built_at=np.array("fixture"), schema_version=np.array("2"))
    if bound:
        fields["node_digests"] = np.array([node_digest(BODY[i]) for i in ids])
        fields["row_source"] = np.array(sources)
        fields["row_body_cos"] = np.array([0.95 if s == "legacy" else 1.0 for s in sources], dtype=np.float32)
    path = os.path.join(folder, name)
    np.savez(path, **fields)
    return path


def read_fields(path):
    with open(path, "rb") as fh:
        d = np.load(fh, allow_pickle=False)
        return {k: d[k] for k in d.files}


def raw(path):
    with open(path, "rb") as fh:
        return fh.read()


def with_semantic(vec_path, fn):
    """fn() with `from math_brain import semantic` resolving to a stand-in holding this file's rows, digests and row
    sources the way the loader of this change reads them."""
    d = read_fields(vec_path)
    fake = types.ModuleType("math_brain.semantic")
    fake.QUERY_PREFIX = ""
    fake._vecs, fake._ids = np.asarray(d["vecs"], dtype=np.float32), np.asarray(d["slugs"])
    fake._digests = np.asarray(d["node_digests"]) if "node_digests" in d else None
    fake._sources = np.asarray(d["row_source"]) if "row_source" in d else None
    fake._load_artifact = lambda: None
    fake._query_encoder = lambda: types.SimpleNamespace(embed=lambda text: np.asarray(Q, dtype=np.float32))
    pkg = types.ModuleType("math_brain")
    pkg.semantic = fake
    saved = {k: sys.modules.get(k) for k in ("math_brain", "math_brain.semantic")}
    sys.modules["math_brain"], sys.modules["math_brain.semantic"] = pkg, fake
    try:
        return fn()
    finally:
        for k, v in saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v


class Hit:
    def __init__(self, nid):
        self.node = types.SimpleNamespace(id=nid)


def hook_top(m, store, vec_path):
    m.STORE_PATH = store

    def run():
        m._SEMTOP.clear()
        m._SEMTOP_WHY.clear()
        q = "which groups of prime order are cyclic"
        return m._semantic_top(q), m._vouch_agrees(q, [Hit(OLD_CARD)])
    top, vouch = with_semantic(vec_path, run)
    return top, vouch, "".join(m._SEMTOP_WHY.values())


def loader(src, vec_path):
    """The real loader of src, in a child process, on this file: (loaded, sources or None, error)."""
    code = ("import json, os, sys; sys.path.insert(0, %r); os.environ['MATH_BRAIN_CLAIM_VECS'] = %r\n"
            "from math_brain import semantic as S\n"
            "try:\n    S._load_artifact(); print(json.dumps([True, None if getattr(S, '_sources', None) is None "
            "else [str(s) for s in S._sources], '']))\n"
            "except Exception as exc:\n    print(json.dumps([False, None, str(exc)[:200]]))\n") % (src, vec_path)
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=120,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    try:
        return tuple(json.loads(p.stdout.strip().splitlines()[-1]))
    except Exception:
        return (False, None, (p.stderr or p.stdout)[-200:])


def main():
    tmp = tempfile.mkdtemp(prefix="claim_vecs_legacy_")
    try:
        ms, mcv = load(HOOK, "ms_legacy"), load(VECS, "mcv_legacy")
        store = make_store(tmp, [OLD_CARD, SIDE])
        leg = make_vectors(tmp, ["legacy", "body"])
        d = read_fields(leg)
        ids, dg, src = [str(x) for x in d["slugs"]], [str(x) for x in d["node_digests"]], [str(x) for x in d["row_source"]]
        cov = mcv.coverage(ids, store, dg, src)
        os.environ["MATH_BRAIN_CLAIM_VECS"] = leg
        ok, line = mcv.status(store)
        top, vouch, why = hook_top(ms, store, leg)
        check(cov == ([OLD_CARD], []) and ok is False and "1 vector(s) of unknown text" in line
              and top is None and vouch is False and "without a vector of their current text" in why,
              "L1 one legacy row: coverage %r, status %r, first claim %r, vouch %r" % (cov, line[:90], top, vouch))
        good = make_vectors(tmp, ["body", "body"], name="good.npz")
        top, vouch, why = hook_top(ms, store, good)
        check(top == OLD_CARD and vouch is True and why == "winner",
              "L2 the row made from its text: first claim %r, vouch %r, why %r" % (top, vouch, why))
        mixed = make_vectors(tmp, ["body", "legacy"], name="mixed.npz", vec_of={SIDE: [0.2, 0.98]})
        top, vouch, why = hook_top(ms, store, mixed)
        check(top is None and vouch is False, "L3 one row from its text and one legacy row: the channel stays closed "
              "(first claim %r, vouch %r)" % (top, vouch))
        sup_dir = os.path.join(tmp, "sup")
        os.makedirs(sup_dir)
        sup_store = make_store(sup_dir, [OLD_CARD, SIDE], superseded=[SIDE])
        sup = make_vectors(sup_dir, ["body", "legacy"], vec_of={SIDE: [0.2, 0.98]})
        top, vouch, why = hook_top(ms, sup_store, sup)
        check(top is None and vouch is False, "L4 a legacy row of a superseded claim closes it too (first claim %r)" % top)

        live = make_vectors(tmp, ["legacy", "body"], name="rebuild_me.npz")
        before = read_fields(live)
        rebuilt, total, note = mcv.rebuild(store, live, embed=fake_embed)
        after = read_fields(live)
        bytes1 = raw(live)
        again = mcv.rebuild(store, live, embed=fake_embed)
        top, vouch, why = hook_top(ms, store, live)
        check((rebuilt, total, note) == (1, 2, "") and np.array_equal(after["vecs"][0], np.asarray(EMB[BODY[OLD_CARD]],
                                                                                                  np.float32))
              and np.array_equal(after["vecs"][1], before["vecs"][1])
              and [str(s) for s in after["row_source"]] == ["body", "body"]
              and [str(x) for x in after["node_digests"]] == [node_digest(BODY[OLD_CARD]), node_digest(BODY[SIDE])]
              and again == (0, 2, "") and raw(live) == bytes1 and top == OLD_CARD and vouch is True,
              "L5 rebuild: %r, row 1 kept, sources %r, second run %r (file unchanged %s), then first claim %r"
              % ((rebuilt, total, note), [str(s) for s in after["row_source"]], again, raw(live) == bytes1, top))
        live2 = make_vectors(tmp, ["legacy", "body"], name="leave_me.npz")
        b0 = raw(live2)
        out = os.path.join(tmp, "rebuilt_elsewhere.npz")
        r = mcv.rebuild(store, live2, embed=fake_embed, out=out)
        check(r == (1, 2, "") and raw(live2) == b0 and [str(s) for s in read_fields(out)["row_source"]] == ["body", "body"],
              "L6 rebuild(out=...): %r, the live file byte-identical %s" % (r, raw(live2) == b0))
        unb = make_vectors(tmp, ["legacy", "body"], name="unbound.npz", bound=False)
        b0 = raw(unb)
        r = mcv.rebuild(store, unb, embed=fake_embed)
        check(r[0] == 0 and "migrate" in r[2] and raw(unb) == b0, "L7 a file without row sources is left for migrate(): %r"
              % (r,))
        ext = make_vectors(tmp, ["legacy", "body"], name="extend_me.npz")
        r = mcv.extend(store, ext, embed=fake_embed)
        e = read_fields(ext)
        check(r[0] == 1 and r[2] == "" and [str(s) for s in e["row_source"]] == ["body", "body"]
              and np.array_equal(e["vecs"][0], np.asarray(EMB[BODY[OLD_CARD]], np.float32)),
              "L8 extend() re-embeds the legacy row: %r, sources %r" % (r, [str(s) for s in e["row_source"]]))
        copied = make_vectors(tmp, ["legacy", "body"], name="copied_digest.npz", bound=False)
        r = mcv.migrate(store, copied, embed=fake_embed)
        c = read_fields(copied)
        top, vouch, why = hook_top(ms, store, copied)
        check(r[:3] == (1, 1, 2) and [str(s) for s in c["row_source"]] == ["legacy", "body"]
              and str(c["node_digests"][0]) == node_digest(BODY[OLD_CARD]) and top is None and vouch is False,
              "L9 migrate() records a vector no text reproduces as legacy though it writes the current digest %r; the "
              "hook refuses it (first claim %r)" % (r, top))

        okf = make_vectors(tmp, ["title body", "legacy"], name="loader_ok.npz")
        badv = make_vectors(tmp, ["verified", "body"], name="loader_badvalue.npz")
        badn = os.path.join(tmp, "loader_badcount.npz")
        f = read_fields(okf)
        f["row_source"] = np.array(["body"])
        np.savez(badn, **f)
        lo, lv, ln = loader(SRC, okf), loader(SRC, badv), loader(SRC, badn)
        check(lo[0] is True and lo[1] == ["title body", "legacy"] and lv[0] is False and "row sources" in lv[2]
              and ln[0] is False and "row sources" in ln[2],
              "L10 the loader: sources %r; a value outside the set refused %r; a count that is not the file's refused %r"
              % (lo[1], lv[2][:60], ln[2][:60]))

        if OLD_HOOK:
            om = load(OLD_HOOK, "ms_legacy_old")
            top, vouch, why = hook_top(om, store, leg)
            check(top == OLD_CARD and vouch is True, "N1 the hook before this change names its winner over a legacy row "
                  "(%r, vouch %r): the defect B06 and B14 found" % (top, vouch))
        if OLD_VECS:
            ov = load(OLD_VECS, "mcv_legacy_old")
            ok_old, line_old = ov.status(store)
            check(ok_old is True, "N2 the module before this change calls a file with a legacy row covered: %r" % line_old[:100])
        if OLD_SRC:
            lo_old = loader(OLD_SRC, okf)
            lv_old = loader(OLD_SRC, badv)
            check(lo_old[0] is True and lo_old[1] is None and lv_old[0] is True,
                  "N3 the loader before this change does not read row_source (sources %r) and loads a file with a value "
                  "outside the set (%r)" % (lo_old[1], lv_old[0]))
    finally:
        os.environ.pop("MATH_BRAIN_CLAIM_VECS", None)
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
