"""test_claim_vectors_bound.py - the meaning channel's claim vectors must cover the store it serves, and each vector must
have been made from the text its claim holds now (29 Sep 2026).

    python test_claim_vectors_bound.py [--old HOOK_BEFORE_THE_ID_CHECK.py] [--old-ids HOOK_WITH_THE_ID_CHECK_ONLY.py]

Fixture stores and vector files live in a temporary folder; the live store and its vectors are never opened.
 C1-C6  the rule: covered, a new claim without a vector, a superseded claim without one, a vector naming no node, a
        vector made from text the store no longer holds, digests that do not line up with the rows;
        math_claim_vecs.coverage and the hook's own copy agree on every case
 H1-H7  the hook: a covered, bound store names its winner; a claim without a vector, a vector naming no node, an
        unreadable store, a vector made from other text, a file that records no digests, or a loader that does not
        read them names nobody, and the vouch agrees with nothing; _SEMTOP_WHY says why
 E1-E11 extend(): adds exactly the missing claim and keeps every old row byte for byte; a second run writes nothing; a
        file naming a node the store lacks, a full-build recipe, or a claim the encoder cannot embed is left as it was;
        a pickled field is refused before any of its code runs; after the extension the new claim can win; a row whose
        text changed is re-embedded in place; a file with no digests is left for migrate(); a file whose digests do not
        line up with its rows is left as it was; a second run waits for the first
 M1-M9  migrate(): rows their body reproduces are recorded as made from it, the file's vectors unchanged; a row the body
        does not reproduce keeps its vector and is recorded legacy with its cosine; status names the legacy rows and
        does not call the file bound (R76); extend() then re-embeds the legacy row and keeps row_source in step; a bound file, a full-build recipe or a missing encoder leaves the file
        as it was; a second run waits for the first; a claim with an empty body is compared with its title
 E12    extend() embeds a new claim with an empty body from its title instead of refusing every run
 S1-S5  status lines: math_claim_vecs.status for a gap, the transport's status once the gap is over an hour old, a file
        with no digests, and a row made from other text
With --old, the hook before the id check names the older claim over a store whose newest claim has no vector (N1). With
--old-ids, the hook that checks ids alone names a winner over a vector made from other text (N2) and over a file with no
digests (N3). Each shows its check can fail.
"""
import hashlib
import importlib.machinery
import importlib.util
import io
import os
import shutil
import sqlite3
import sys
import tempfile
import time
import types
import zipfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]


def _arg(flag):
    return os.path.abspath(ARGS[ARGS.index(flag) + 1]) if flag in ARGS else None


OLD, OLD_IDS = _arg("--old"), _arg("--old-ids")
sys.path.insert(0, HERE)
import math_claim_vecs as mcv  # noqa: E402

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


# claim ids, bodies and 2-D "embeddings": the question points at NEW; OLD_CARD is the best of the rest. CHANGED is
# OLD_CARD's text in a store that holds other text under the same id.
OLD_CARD, SIDE, NEW = "claim_old_prime_order_is_cyclic", "claim_side_lagrange", "claim_new_prime_order_result"
BODY = {OLD_CARD: "every group of prime order is cyclic", SIDE: "the order of a subgroup divides the order",
        NEW: "the new result about groups of prime order"}
CHANGED = "every group of prime order is cyclic and abelian"
EMB = {BODY[OLD_CARD]: [0.8, 0.6], BODY[SIDE]: [0.0, 1.0], BODY[NEW]: [1.0, 0.0], CHANGED: [0.6, 0.8]}
Q = [1.0, 0.0]


def node_digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]


def fake_embed(text):
    v = EMB.get(text)
    return None if v is None else np.asarray(v, dtype=np.float32)


def make_store(folder, claims, superseded=(), extra_nodes=(), body=None):
    text = dict(BODY, **(body or {}))
    path = os.path.join(folder, "brain.sqlite3")
    if os.path.exists(path):
        os.remove(path)
    con = sqlite3.connect(path)
    con.executescript("create table nodes (id text primary key, kind text, title text, body text, digest text);"
                      "create table claims (id text primary key);"
                      "create table edges (kind text, source_id text, target_id text);")
    for c in claims:
        t = text.get(c, c)
        con.execute("insert into nodes values (?, 'claim', ?, ?, ?)", (c, c, t, node_digest(t)))
        con.execute("insert into claims values (?)", (c,))
    for n in extra_nodes:
        con.execute("insert into nodes values (?, 'evidence', ?, ?, ?)", (n, n, n, node_digest(n)))
    for old in superseded:
        con.execute("insert into edges values ('supersedes', ?, ?)", ("x_" + old, old))
    con.commit()
    con.close()
    return path


def make_vectors(folder, ids, bound=True, **extra):
    """A vector file of these claims embedded from BODY; bound records each row's store digest of that text."""
    path = os.path.join(folder, "claim_embeddings.npz")
    fields = dict(slugs=np.array(ids), vecs=np.asarray([EMB[BODY[i]] for i in ids], dtype=np.float32),
                  model=np.array("BAAI/bge-small-en-v1.5"), text_sha256=np.array("ext:0000"),
                  built_at=np.array("fixture"), schema_version=np.array("2"))
    if bound:
        fields["node_digests"] = np.array([node_digest(BODY[i]) for i in ids])
    fields.update(extra)
    np.savez(path, **fields)
    # a file written here by hand is not a published one: a SHA-256 manifest an earlier writer call left beside this
    # path names other bytes, and the loader and status() would refuse the fixture for that (R77, 29 Sep)
    if os.path.exists(path + ".sha256"):
        os.remove(path + ".sha256")
    return path


def read_fields(path):
    with open(path, "rb") as fh:
        d = np.load(fh, allow_pickle=False)
        return {k: d[k] for k in d.files}


def with_semantic(vec_path, fn, reads_digests=True):
    """Run fn() with `from math_brain import semantic` resolving to a stand-in that holds this vector file's rows, and
    its store digests the way math_brain.semantic reads them (reads_digests=False: a loader that does not)."""
    d = read_fields(vec_path)
    fake = types.ModuleType("math_brain.semantic")
    fake.QUERY_PREFIX = ""
    fake._vecs, fake._ids = np.asarray(d["vecs"], dtype=np.float32), np.asarray(d["slugs"])
    if reads_digests:
        fake._digests = np.asarray(d["node_digests"]) if "node_digests" in d else None
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


def hook_top(m, store, vec_path, lead, reads_digests=True):
    m.STORE_PATH = store

    def run():
        m._SEMTOP.clear()
        getattr(m, "_SEMTOP_WHY", {}).clear()
        return m._semantic_top("which groups of prime order are cyclic"), m._vouch_agrees(
            "which groups of prime order are cyclic", [Hit(lead)])
    top, vouch = with_semantic(vec_path, run, reads_digests)
    return top, vouch, dict(getattr(m, "_SEMTOP_WHY", {}))


def raw(path):
    with open(path, "rb") as fh:
        return fh.read()


def main():
    tmp = tempfile.mkdtemp(prefix="claim_vecs_bound_")
    try:
        ms = load(os.path.join(HERE, "math_sense.py"), "ms_vecs_bound")

        # ---- the rule (each case builds its store when it runs: they share one fixture path)
        for label, ids, build, want in (
            ("C1 covered", [OLD_CARD, SIDE], lambda: make_store(tmp, [OLD_CARD, SIDE]), ([], [])),
            ("C2 a new claim without a vector", [OLD_CARD, SIDE], lambda: make_store(tmp, [OLD_CARD, SIDE, NEW]),
             ([NEW], [])),
            ("C3 a superseded claim without a vector", [SIDE, NEW],
             lambda: make_store(tmp, [OLD_CARD, SIDE, NEW], superseded=[OLD_CARD]), ([], [])),
            ("C4 a vector naming no node", [OLD_CARD, SIDE, NEW], lambda: make_store(tmp, [OLD_CARD, SIDE]),
             ([], [NEW])),
        ):
            st = build()
            dg = [node_digest(BODY[i]) for i in ids]
            a, b = mcv.coverage(ids, st, dg), ms._claim_vectors_cover_store(ids, st, dg)
            check(a == want and b == want, "%s: module %r, hook %r" % (label, a, b))
        ids = [OLD_CARD, SIDE]
        dg = [node_digest(BODY[i]) for i in ids]
        st = make_store(tmp, ids, body={OLD_CARD: CHANGED})
        a, b = mcv.coverage(ids, st, dg), ms._claim_vectors_cover_store(ids, st, dg)
        a0, b0 = mcv.coverage(ids, st), ms._claim_vectors_cover_store(ids, st)
        check(a == b == ([OLD_CARD], []) and a0 == b0 == ([], []),
              "C5 a vector made from text the store no longer holds counts as missing: module %r, hook %r (by ids "
              "alone both pass it: %r, %r)" % (a, b, a0, b0))
        errs = []
        for fn in (lambda: mcv.coverage(ids, st, dg[:1]), lambda: ms._claim_vectors_cover_store(ids, st, dg[:1])):
            try:
                fn()
                errs.append(None)
            except ValueError as exc:
                errs.append(str(exc))
        check(all(e and "2 vectors" in e for e in errs),
              "C6 digests that do not line up with the rows are refused, not truncated: %r" % (errs,))

        # ---- the hook
        vec2 = make_vectors(tmp, [OLD_CARD, SIDE])
        store = make_store(tmp, [OLD_CARD, SIDE])
        top, vouch, why = hook_top(ms, store, vec2, OLD_CARD)
        check(top == OLD_CARD and vouch is True and list(why.values()) == ["winner"],
              "H1 covered, bound store: first claim %r, vouch %r, why %r" % (top, vouch, why))
        store = make_store(tmp, [OLD_CARD, SIDE, NEW])
        top, vouch, why = hook_top(ms, store, vec2, OLD_CARD)
        check(top is None and vouch is False and "1 current claim(s) without a vector" in "".join(why.values()),
              "H2 a claim without a vector: first claim %r, vouch %r, why %r" % (top, vouch, why))
        vec3 = make_vectors(tmp, [OLD_CARD, SIDE, NEW])
        top, vouch, why = hook_top(ms, make_store(tmp, [OLD_CARD, SIDE]), vec3, NEW)
        check(top is None and vouch is False and "1 vector(s) naming no node" in "".join(why.values()),
              "H3 a vector naming no node: first claim %r, vouch %r, why %r" % (top, vouch, why))
        top, vouch, why = hook_top(ms, os.path.join(tmp, "no_such_dir", "brain.sqlite3"), vec3, NEW)
        check(top is None and vouch is False and "".join(why.values()).startswith("unavailable"),
              "H4 an unreadable store: first claim %r, vouch %r, why %r" % (top, vouch, why))
        vec2 = make_vectors(tmp, [OLD_CARD, SIDE])
        top, vouch, why = hook_top(ms, make_store(tmp, [OLD_CARD, SIDE], body={OLD_CARD: CHANGED}), vec2, OLD_CARD)
        check(top is None and vouch is False
              and "1 current claim(s) without a vector of their current text" in "".join(why.values()),
              "H5 a vector made from text the store no longer holds: first claim %r, vouch %r, why %r"
              % (top, vouch, why))
        store = make_store(tmp, [OLD_CARD, SIDE])
        top, vouch, why = hook_top(ms, store, make_vectors(tmp, [OLD_CARD, SIDE], bound=False), OLD_CARD)
        check(top is None and vouch is False and "carry no store digests" in "".join(why.values()),
              "H6 a file that records no digests: first claim %r, vouch %r, why %r" % (top, vouch, why))
        top, vouch, why = hook_top(ms, store, make_vectors(tmp, [OLD_CARD, SIDE]), OLD_CARD, reads_digests=False)
        check(top is None and vouch is False and "carry no store digests" in "".join(why.values()),
              "H7 a loader that does not read the digests: first claim %r, vouch %r, why %r" % (top, vouch, why))

        # ---- extend()
        store = make_store(tmp, [OLD_CARD, SIDE, NEW])
        vec = make_vectors(tmp, [OLD_CARD, SIDE])
        before = read_fields(vec)["vecs"].copy()
        added, total, note = mcv.extend(store, vec, embed=fake_embed)
        d = read_fields(vec)
        slugs, digs = [str(x) for x in d["slugs"]], [str(x) for x in d["node_digests"]]
        check((added, total, note) == (1, 3, "") and slugs == [OLD_CARD, SIDE, NEW]
              and np.array_equal(d["vecs"][:2], before)
              and np.array_equal(d["vecs"][2], np.asarray(EMB[BODY[NEW]], np.float32))
              and digs == [node_digest(BODY[i]) for i in slugs] and "+1 claims by body" in str(d["built_at"])
              and str(d["text_sha256"]) != "ext:0000" and mcv.coverage(slugs, store, digs) == ([], []),
              "E1 one claim added, old rows kept byte for byte, every row's digest recorded: %r, slugs %r, built_at %r"
              % ((added, total, note), slugs, str(d["built_at"])))
        once = raw(vec)
        again = mcv.extend(store, vec, embed=fake_embed)
        check(again == (0, 3, "") and raw(vec) == once, "E2 a second run writes nothing: %r" % (again,))
        vec = make_vectors(tmp, [OLD_CARD, SIDE, NEW])
        before_b = raw(vec)
        r = mcv.extend(make_store(tmp, [OLD_CARD, SIDE]), vec, embed=fake_embed)
        check(r[0] == 0 and "name no node" in r[2] and raw(vec) == before_b,
              "E3 a vector naming no node: not extended, file unchanged (%r)" % (r,))
        store = make_store(tmp, [OLD_CARD, SIDE, NEW])
        vec = make_vectors(tmp, [OLD_CARD, SIDE], text_rule=np.array("title + ' ' + body, current nodes only"))
        before_b = raw(vec)
        r = mcv.extend(store, vec, embed=fake_embed)
        check(r[0] == 0 and "not the claims-table one" in r[2] and raw(vec) == before_b,
              "E4 a full-build recipe: not extended, file unchanged (%r)" % (r,))
        vec = make_vectors(tmp, [OLD_CARD, SIDE])
        before_b = raw(vec)
        r = mcv.extend(store, vec, embed=lambda text: None)
        check(r[0] == 0 and "could not be embedded" in r[2] and raw(vec) == before_b,
              "E5 a claim the encoder cannot embed: nothing written (%r)" % (r,))
        marker = os.path.join(tmp, "pickle_ran.txt")

        class Opens:
            def __reduce__(self):
                return (open, (marker, "w"))
        buf = io.BytesIO()
        np.save(buf, np.array([Opens(), OLD_CARD], dtype=object), allow_pickle=True)
        vec = os.path.join(tmp, "claim_embeddings.npz")
        with zipfile.ZipFile(vec, "w") as z:
            z.writestr("slugs.npy", buf.getvalue())
            b2 = io.BytesIO()
            np.save(b2, np.zeros((2, 2), np.float32))
            z.writestr("vecs.npy", b2.getvalue())
        try:
            mcv.extend(store, vec, embed=fake_embed)
            refused = False
        except ValueError:
            refused = True
        check(refused and not os.path.exists(marker), "E6 a pickled field is refused before its code runs (refused %r, "
              "marker %r)" % (refused, os.path.exists(marker)))
        vec = make_vectors(tmp, [OLD_CARD, SIDE])
        mcv.extend(store, vec, embed=fake_embed)
        top, vouch, why = hook_top(ms, store, vec, NEW)
        check(top == NEW and vouch is True, "E7 after the extension the new claim wins: first claim %r, vouch %r, why %r"
              % (top, vouch, why))
        store = make_store(tmp, [OLD_CARD, SIDE], body={OLD_CARD: CHANGED})
        vec = make_vectors(tmp, [OLD_CARD, SIDE])
        before = read_fields(vec)["vecs"].copy()
        r = mcv.extend(store, vec, embed=fake_embed)
        d = read_fields(vec)
        top, vouch, why = hook_top(ms, store, vec, OLD_CARD)
        check(r == (1, 2, "") and [str(x) for x in d["slugs"]] == [OLD_CARD, SIDE]
              and np.array_equal(d["vecs"][0], np.asarray(EMB[CHANGED], np.float32))
              and np.array_equal(d["vecs"][1], before[1])
              and [str(x) for x in d["node_digests"]] == [node_digest(CHANGED), node_digest(BODY[SIDE])]
              and "1 re-embedded by body" in str(d["built_at"]) and list(why.values()) in (["winner"], ["no winner"]),
              "E8 a row whose text changed is re-embedded in place, the other kept, and the hook reads it again: %r, "
              "built_at %r, why %r" % (r, str(d["built_at"]), why))
        store = make_store(tmp, [OLD_CARD, SIDE, NEW])
        vec = make_vectors(tmp, [OLD_CARD, SIDE], bound=False)
        before_b = raw(vec)
        r = mcv.extend(store, vec, embed=fake_embed)
        check(r[0] == 0 and "migrate" in r[2] and raw(vec) == before_b,
              "E9 a file with no digests is not extended, even with a claim missing; the note names migrate (%r)" % (r,))
        vec = make_vectors(tmp, [OLD_CARD, SIDE], node_digests=np.array([node_digest(BODY[OLD_CARD])]))
        before_b = raw(vec)
        r = mcv.extend(store, vec, embed=fake_embed)
        check(r[0] == 0 and "1 store digests for 2 vectors" in r[2] and raw(vec) == before_b,
              "E10 digests that do not line up with the rows: not extended, file unchanged (%r)" % (r,))
        store = make_store(tmp, [OLD_CARD, SIDE, NEW])
        vec = make_vectors(tmp, [OLD_CARD, SIDE])
        before_b = raw(vec)
        held = mcv._take_lock(vec)
        try:
            r = mcv.extend(store, vec, embed=fake_embed)
            unchanged = raw(vec) == before_b
        finally:
            mcv._drop_lock(held)
        r2 = mcv.extend(store, vec, embed=fake_embed)
        check(held is not None and r[0] == 0 and "holds" in r[2] and unchanged and r2 == (1, 3, ""),
              "E11 while another extend() holds the lock, a second one writes nothing; after it is released the "
              "extension runs (%r, then %r)" % (r, r2))

        # ---- migrate()
        store = make_store(tmp, [OLD_CARD, SIDE])
        vec = make_vectors(tmp, [OLD_CARD, SIDE], bound=False)
        before = read_fields(vec)["vecs"].copy()
        r = mcv.migrate(store, vec, embed=fake_embed)
        d = read_fields(vec)
        once = raw(vec)
        r2 = mcv.extend(store, vec, embed=fake_embed)
        top, vouch, why = hook_top(ms, store, vec, OLD_CARD)
        check(r == (2, 0, 2, "") and np.array_equal(d["vecs"], before)
              and [str(x) for x in d["node_digests"]] == [node_digest(BODY[i]) for i in (OLD_CARD, SIDE)]
              and [str(x) for x in d["row_source"]] == ["body", "body"]
              and "store digests recorded" in str(d["built_at"]) and r2 == (0, 2, "") and raw(vec) == once
              and top == OLD_CARD and vouch is True,
              "M1 rows their body reproduces are recorded as made from it, no vector changes, extend() then has nothing "
              "to do, and the hook names its winner: %r, then %r, first claim %r" % (r, r2, top))
        store = make_store(tmp, [OLD_CARD, SIDE], body={OLD_CARD: CHANGED})
        vec = make_vectors(tmp, [OLD_CARD, SIDE], bound=False)
        before = read_fields(vec)["vecs"].copy()
        r = mcv.migrate(store, vec, embed=fake_embed)
        d = read_fields(vec)
        cos0 = float(d["row_body_cos"][0])
        check(r == (1, 1, 2, "") and np.array_equal(d["vecs"], before)
              and [str(x) for x in d["row_source"]] == ["legacy", "body"] and abs(cos0 - 0.96) < 1e-6
              and [str(x) for x in d["node_digests"]] == [node_digest(CHANGED), node_digest(BODY[SIDE])],
              "M2 a row its body does not reproduce keeps its vector and is recorded legacy with its cosine: %r, "
              "cosine %.4f" % (r, cos0))
        ok_l, line_l = mcv.status(store)
        check(ok_l is False and "1 vector(s) of unknown text (legacy, cosine 0.9600-0.9600 with their claim's text)" in line_l,
              "M3 status names the legacy rows and does not call the file bound (R76): %r" % line_l)
        store = make_store(tmp, [OLD_CARD, SIDE, NEW], body={OLD_CARD: CHANGED, SIDE: BODY[NEW]})
        r = mcv.extend(store, vec, embed=fake_embed)
        d = read_fields(vec)
        check(r == (3, 3, "") and [str(x) for x in d["slugs"]] == [OLD_CARD, SIDE, NEW]
              and [str(x) for x in d["row_source"]] == ["body", "body", "body"]
              and [round(float(c), 4) for c in d["row_body_cos"]] == [1.0, 1.0, 1.0]
              and np.array_equal(d["vecs"][0], np.asarray(EMB[CHANGED], np.float32)),
              "M4 extend() keeps row_source in step: the legacy row is re-embedded from its text (R76) with the row whose "
              "text changed, and the added one, all recorded as made from their body (%r, sources %r)"
              % (r, [str(x) for x in d["row_source"]]))
        vec = make_vectors(tmp, [OLD_CARD, SIDE])
        before_b = raw(vec)
        r = mcv.migrate(make_store(tmp, [OLD_CARD, SIDE]), vec, embed=fake_embed)
        check(r == (0, 0, 2, "") and raw(vec) == before_b, "M5 a bound file is left as it is: %r" % (r,))
        store = make_store(tmp, [OLD_CARD, SIDE])
        vec = make_vectors(tmp, [OLD_CARD, SIDE], bound=False,
                           text_rule=np.array("title + ' ' + body, current nodes only"))
        before_b = raw(vec)
        r = mcv.migrate(store, vec, embed=fake_embed)
        check(r[0] == 0 and "not the claims-table one" in r[3] and raw(vec) == before_b,
              "M6 a full-build recipe is not migrated, file unchanged (%r)" % (r,))
        vec = make_vectors(tmp, [OLD_CARD, SIDE], bound=False)
        before_b = raw(vec)
        r = mcv.migrate(store, vec, embed=lambda text: None)
        check(r[0] == 0 and "could not be embedded" in r[3] and raw(vec) == before_b,
              "M7 no encoder: nothing written (%r)" % (r,))
        held = mcv._take_lock(vec)
        try:
            r = mcv.migrate(store, vec, embed=fake_embed)
            unchanged = raw(vec) == before_b
        finally:
            mcv._drop_lock(held)
        check(r[0] == 0 and "holds" in r[3] and unchanged,
              "M8 while another run holds the lock, migrate() writes nothing (%r)" % (r,))
        TITLED = "claim_titled_only"            # a claim whose statement sits in its title, body empty
        BODY[TITLED], EMB[TITLED] = "", [0.28, 0.96]
        store = make_store(tmp, [OLD_CARD, SIDE])
        con = sqlite3.connect(store)
        con.execute("insert into nodes values (?, 'claim', ?, '', ?)", (TITLED, TITLED, node_digest("")))
        con.execute("insert into claims values (?)", (TITLED,))
        con.commit()
        con.close()
        vec = make_vectors(tmp, [OLD_CARD, SIDE], bound=False,
                           slugs=np.array([OLD_CARD, SIDE, TITLED]),
                           vecs=np.asarray([EMB[BODY[OLD_CARD]], EMB[BODY[SIDE]], EMB[TITLED]], dtype=np.float32))
        r = mcv.migrate(store, vec, embed=fake_embed)
        d = read_fields(vec)
        check(r == (3, 0, 3, "") and [str(x) for x in d["row_source"]] == ["body", "body", "title"],
              "M9 a claim with an empty body is compared with its title: %r, sources %r"
              % (r, [str(x) for x in d.get("row_source", [])]))
        vec = make_vectors(tmp, [OLD_CARD, SIDE])
        r = mcv.extend(store, vec, embed=fake_embed)
        d = read_fields(vec)
        check(r == (1, 3, "") and [str(x) for x in d["slugs"]][-1] == TITLED
              and np.array_equal(d["vecs"][-1], np.asarray(EMB[TITLED], np.float32)),
              "E12 extend() embeds a new claim with an empty body from its title (%r)" % (r,))
        del BODY[TITLED], EMB[TITLED]

        # ---- status lines
        vec = make_vectors(tmp, [OLD_CARD, SIDE])          # beside the store, where vector_path() looks
        store = make_store(tmp, [OLD_CARD, SIDE, NEW])
        ok_stale, line_stale = mcv.status(store)
        mcv.extend(store, vec, embed=fake_embed)
        ok_fresh, line_fresh = mcv.status(store)
        check(ok_stale is False and "1 current claim(s) have no vector" in line_stale and ok_fresh is True
              and "text bound" in line_fresh, "S1 status: %r / %r" % (line_stale, line_fresh))
        mt = load(os.path.join(HERE, "math_transport.py"), "mt_vecs_bound")
        side = os.path.join(tmp, "transport")
        os.makedirs(side)
        mt.STORE = store
        mt.STATE, mt.LEDGER, mt.QUEUE, mt.HOLD = (os.path.join(side, n) for n in ("state.json", "ledger.jsonl",
                                                                                   "queue.jsonl", "HOLD"))
        vec = make_vectors(tmp, [OLD_CARD, SIDE])

        def transport_line():
            out = io.StringIO()
            real = sys.stdout
            sys.stdout = out
            try:
                mt.status()
            finally:
                sys.stdout = real
            return out.getvalue()
        # the fixture transport never ran, so its fault list opens with NEVER RAN: a note sits before it, a fault after
        fresh_line = transport_line()
        old = time.time() - 2 * 3600
        os.utime(vec, (old, old))
        stale_line = transport_line()
        check("have no vector" in fresh_line and fresh_line.index("have no vector") < fresh_line.index("NEVER RAN"),
              "S2 transport status: a gap under an hour is a note (%r)" % fresh_line.strip()[-200:])
        check("have no vector" in stale_line and stale_line.index("have no vector") > stale_line.index("NEVER RAN"),
              "S3 transport status: a gap over an hour is a fault (%r)" % stale_line.strip()[-200:])
        store = make_store(tmp, [OLD_CARD, SIDE])
        make_vectors(tmp, [OLD_CARD, SIDE], bound=False)
        ok_unbound, line_unbound = mcv.status(store)
        check(ok_unbound is False and "records no store digests" in line_unbound
              and line_unbound.endswith("math_claim_vecs.py migrate"),
              "S4 status of a file with no digests: %r" % line_unbound)
        store = make_store(tmp, [OLD_CARD, SIDE], body={OLD_CARD: CHANGED})
        make_vectors(tmp, [OLD_CARD, SIDE])
        ok_drift, line_drift = mcv.status(store)
        check(ok_drift is False and "1 vector(s) were made from text the store no longer holds" in line_drift,
              "S5 status of a row made from other text: %r" % line_drift)

        if OLD:
            o = load(OLD, "ms_vecs_bound_old")
            store = make_store(tmp, [OLD_CARD, SIDE, NEW])
            top, vouch, _ = hook_top(o, store, make_vectors(tmp, [OLD_CARD, SIDE]), OLD_CARD)
            check(top == OLD_CARD and vouch is True,
                  "N1 the hook before the id check agrees on the older card while the newest claim has no vector "
                  "(first claim %r, vouch %r; the check can fail)" % (top, vouch))
        if OLD_IDS:
            o = load(OLD_IDS, "ms_vecs_bound_old_ids")
            store = make_store(tmp, [OLD_CARD, SIDE], body={OLD_CARD: CHANGED})
            top, vouch, _ = hook_top(o, store, make_vectors(tmp, [OLD_CARD, SIDE]), OLD_CARD)
            check(top == OLD_CARD and vouch is True,
                  "N2 the hook that checks ids alone vouches for a card whose vector was made from other text "
                  "(first claim %r, vouch %r; the digest check can fail)" % (top, vouch))
            store = make_store(tmp, [OLD_CARD, SIDE])
            top, vouch, _ = hook_top(o, store, make_vectors(tmp, [OLD_CARD, SIDE], bound=False), OLD_CARD)
            check(top == OLD_CARD and vouch is True,
                  "N3 the hook that checks ids alone vouches over a file with no digests (first claim %r, vouch %r)"
                  % (top, vouch))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
