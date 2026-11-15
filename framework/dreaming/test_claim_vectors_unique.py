"""test_claim_vectors_unique.py - one claim, one vector row (29 Sep 2026, an agent; scheduled audit account04/B06
r75, B06-R75-DUPLICATE-CLAIM-ROWS-PASS-BINDING-20260929).

    python test_claim_vectors_unique.py [--hook MATH_SENSE.py] [--vecs MATH_CLAIM_VECS.py] [--src MATH_BRAIN_SRC]
                                        [--old-hook OLD.py] [--old-vecs OLD.py]

Fixture stores and vector files live in a temporary folder; the live store and its vectors are never opened. Each id of
a vector file must name one row: the meaning channel's winner is a row, so a second row under the same id is a second
voice for the claim that no check has read.
 U1 ids A, A, B with current digests and different A vectors: status fails naming A, the hook names nobody, and the
    loader refuses the file
 U2 the same with identical A vectors: still refused (equal vectors do not make one identity)
 U3 a duplicated superseded id: refused too, not excused by the superseded exception
 U4 unique ids: healthy, and the hook names its winner as before
 U5 an id array that is not 1-D, and vectors that do not line up with the ids: the loader refuses both
 U6 extend, migrate and rebuild on a duplicated file: each refuses, the file byte-identical, no temporary file left
 U7 two extends at once: one writes and the other backs off; afterwards every current claim has exactly one row
With --old-hook and --old-vecs, the hook and the module before this change pass a file with a duplicated id (N1, N2),
and extend reports nothing wrong with it (N3): the checks can fail.
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
import threading
import types

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]


def _arg(flag, default=None):
    return os.path.abspath(ARGS[ARGS.index(flag) + 1]) if flag in ARGS else default


HOOK = _arg("--hook", os.path.join(HERE, "math_sense.py"))
VECS = _arg("--vecs", os.path.join(HERE, "math_claim_vecs.py"))
SRC = _arg("--src", r"~\math-brain-build\src")
OLD_HOOK, OLD_VECS = _arg("--old-hook"), _arg("--old-vecs")
DREAMING = os.path.join(os.path.expanduser("~"), ".claude", "dreaming")
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


A, B, C = "claim_a_prime_order_is_cyclic", "claim_b_lagrange", "claim_c_new"
BODY = {A: "every group of prime order is cyclic", B: "the order of a subgroup divides the order",
        C: "a new result about groups"}
EMB = {BODY[A]: [0.8, 0.6], BODY[B]: [0.0, 1.0], BODY[C]: [0.6, 0.8]}
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


def make_vectors(folder, ids, name="claim_embeddings.npz", vecs=None, bound=True, raw_ids=None):
    vecs = vecs if vecs is not None else [EMB[BODY[i]] for i in ids]
    fields = dict(slugs=raw_ids if raw_ids is not None else np.array(ids), vecs=np.asarray(vecs, dtype=np.float32),
                  model=np.array("BAAI/bge-small-en-v1.5"), text_sha256=np.array("ext:0000"),
                  built_at=np.array("fixture"), schema_version=np.array("2"))
    if bound:
        fields["node_digests"] = np.array([node_digest(BODY[i]) for i in ids])
        fields["row_source"] = np.array(["body"] * len(ids))
        fields["row_body_cos"] = np.array([1.0] * len(ids), dtype=np.float32)
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


def hook_top(m, store, vec_path, lead=A):
    m.STORE_PATH = store

    def run():
        m._SEMTOP.clear()
        m._SEMTOP_WHY.clear()
        q = "which groups of prime order are cyclic"
        return m._semantic_top(q), m._vouch_agrees(q, [Hit(lead)])
    top, vouch = with_semantic(vec_path, run)
    return top, vouch, "".join(m._SEMTOP_WHY.values())


def loader(src, vec_path):
    code = ("import json, os, sys; sys.path.insert(0, %r); os.environ['MATH_BRAIN_CLAIM_VECS'] = %r\n"
            "from math_brain import semantic as S\n"
            "try:\n    S._load_artifact(); print(json.dumps([True, '']))\n"
            "except Exception as exc:\n    print(json.dumps([False, str(exc)[:200]]))\n") % (src, vec_path)
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=120,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    try:
        return tuple(json.loads(p.stdout.strip().splitlines()[-1]))
    except Exception:
        return (False, (p.stderr or p.stdout)[-200:])


def main():
    tmp = tempfile.mkdtemp(prefix="claim_vecs_unique_")
    try:
        ms, mcv = load(HOOK, "ms_unique"), load(VECS, "mcv_unique")
        store = make_store(tmp, [A, B])
        dup = make_vectors(tmp, [A, A, B], name="dup.npz", vecs=[[0.8, 0.6], [1.0, 0.0], [0.0, 1.0]])
        os.environ["MATH_BRAIN_CLAIM_VECS"] = dup
        ok, line = mcv.status(store)
        c = mcv.check([A, A, B], [node_digest(BODY[i]) for i in (A, A, B)], store, ["body"] * 3)
        top, vouch, why = hook_top(ms, store, dup)
        lo = loader(SRC, dup)
        check(ok is False and c["duplicates"] == [A] and "name more than one row" in line and top is None
              and vouch is False and lo[0] is False and "not unique" in lo[1],
              "U1 ids A, A, B: status %r, duplicates %r, first claim %r, loader %r" % (line[:80], c["duplicates"], top, lo))
        same = make_vectors(tmp, [A, A, B], name="dup_same.npz", vecs=[[0.8, 0.6], [0.8, 0.6], [0.0, 1.0]])
        os.environ["MATH_BRAIN_CLAIM_VECS"] = same
        ok2, _l2 = mcv.status(store)
        top2, _v2, _w2 = hook_top(ms, store, same)
        check(ok2 is False and top2 is None, "U2 identical vectors under a repeated id: status ok %r, first claim %r"
              % (ok2, top2))
        sup_dir = os.path.join(tmp, "sup")
        os.makedirs(sup_dir)
        sup_store = make_store(sup_dir, [A, B], superseded=[B])
        sup = make_vectors(sup_dir, [A, B, B], vecs=[[0.8, 0.6], [0.0, 1.0], [0.1, 0.99]])
        os.environ["MATH_BRAIN_CLAIM_VECS"] = sup
        ok3, line3 = mcv.status(sup_store)
        top3, _v3, _w3 = hook_top(ms, sup_store, sup)
        check(ok3 is False and top3 is None, "U3 a duplicated superseded id: status %r, first claim %r" % (line3[:70], top3))
        uniq = make_vectors(tmp, [A, B], name="uniq.npz")
        os.environ["MATH_BRAIN_CLAIM_VECS"] = uniq
        ok4, _l4 = mcv.status(store)
        top4, vouch4, why4 = hook_top(ms, store, uniq)
        check(ok4 is True and top4 == A and vouch4 is True and loader(SRC, uniq)[0] is True,
              "U4 unique ids: status ok, first claim %r, vouch %r" % (top4, vouch4))
        twod = make_vectors(tmp, [A, B], name="twod.npz", raw_ids=np.array([[A], [B]]))
        short = make_vectors(tmp, [A, B], name="short.npz", vecs=[[0.8, 0.6], [0.0, 1.0], [1.0, 0.0]])
        l5a, l5b = loader(SRC, twod), loader(SRC, short)
        check(l5a[0] is False and "1-D" in l5a[1] and l5b[0] is False and "mismatch" in l5b[1],
              "U5 a 2-D id array refused %r; vectors not lining up with ids refused %r" % (l5a[1][:60], l5b[1][:60]))
        results = []
        u6 = os.path.join(tmp, "u6")
        os.makedirs(u6)
        u6_store = make_store(u6, [A, B, C])       # its own folder: the other cases read the store of A and B
        for label, fn in (("extend", lambda p: mcv.extend(u6_store, p, embed=fake_embed)),
                          ("rebuild", lambda p: mcv.rebuild(store, p, embed=fake_embed)),
                          ("migrate", lambda p: mcv.migrate(store, p, embed=fake_embed))):
            p = make_vectors(tmp, [A, A, B], name="dup_%s.npz" % label, vecs=[[0.8, 0.6], [1.0, 0.0], [0.0, 1.0]],
                             bound=(label != "migrate"))
            b0 = raw(p)
            r = fn(p)
            left = [f for f in os.listdir(tmp) if f.startswith("dup_%s.npz.tmp" % label)]
            results.append((label, r[-1], raw(p) == b0, left))
        check(all("more than one row" in note and same_bytes and not left for _l, note, same_bytes, left in results),
              "U6 extend, rebuild and migrate refuse a duplicated file, byte-identical, no temporary file: %r"
              % [(lab, n[:40], s) for lab, n, s, _x in results])
        cc = os.path.join(tmp, "cc")
        os.makedirs(cc)
        cstore = make_store(cc, [A, B, C])
        cvec = make_vectors(cc, [A, B])
        out = []
        threads = [threading.Thread(target=lambda: out.append(mcv.extend(cstore, cvec, embed=fake_embed))) for _ in range(2)]
        for th in threads:
            th.start()
        for th in threads:
            th.join()
        final = mcv.extend(cstore, cvec, embed=fake_embed)
        ids = [str(x) for x in read_fields(cvec)["slugs"]]
        check(len(ids) == len(set(ids)) and sorted(ids) == sorted([A, B, C]) and final == (0, 3, ""),
              "U7 two extends at once %r, then %r: ids %r" % (out, final, ids))
        if OLD_HOOK:
            om = load(OLD_HOOK, "ms_unique_old")
            topn, vouchn, _wn = hook_top(om, store, dup)
            check(topn is not None and vouchn is True, "N1 the hook before this change names a winner over ids A, A, B "
                  "(%r, vouch %r): the defect B06 found" % (topn, vouchn))
        if OLD_VECS:
            ov = load(OLD_VECS, "mcv_unique_old")
            os.environ["MATH_BRAIN_CLAIM_VECS"] = dup
            okn, linen = ov.status(store)
            check(okn is True, "N2 the module before this change calls ids A, A, B covered: %r" % linen[:90])
            p = make_vectors(tmp, [A, A, B], name="dup_old_extend.npz", vecs=[[0.8, 0.6], [1.0, 0.0], [0.0, 1.0]])
            rn = ov.extend(store, p, embed=fake_embed)
            check(rn[-1] == "", "N3 the module before this change extends a duplicated file without a word: %r" % (rn,))
    finally:
        os.environ.pop("MATH_BRAIN_CLAIM_VECS", None)
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
