"""Singular/plural fold for recall's BM25 lane (an agent, 8 Nov 2026, brain loop T-20261107-016).

The index has no stemming, so a question that says 'settlement' never meets a memory that says 'settlements'
(the VIX settlements reference sat at BM25 rank 7 for "old VIX futures settlement files before 2012"). For each
query word t whose other number form o is in the vocabulary, t and o are scored as ONE term: f = f_t + f_o in
each document, df = the documents holding either, the same idf / K1 / B. Only rare words fold: min(df_t, df_o)
must be under CUT (200), because a common word's two forms often mean different things (data / datas aside,
'test' vs 'tests' carry no extra signal and folding them reshuffles the head).

Measured on 400 stored questions (200 tuning, 200 held out, disjoint; brainloop_c462/plural_probe2.py, 3.py):
as written top-1 146 -> 148, top-8 218 -> 217; with one word in the other number top-1 95 -> 118, top-8
159 -> 179. Ledger rows 34-35.

score(bm, query, topk, cut) returns None when no word folds, and the caller then uses bm.score unchanged, so a
query with nothing to fold is scored by exactly the old code. BRAIN_RECALL_PLURAL=0 turns the fold off;
BRAIN_RECALL_PLURAL_CUT sets CUT."""
import heapq
import math
import os
import struct
import zlib
from itertools import repeat
from operator import add, mul, neg, truediv

CUT = 200


def other(t):
    """The other number form of t by plain English rules, or None (not checked against the vocabulary)."""
    if not t.isalpha() or len(t) < 4:
        return None
    if t.endswith("ss") or t.endswith("us") or t.endswith("is"):
        return t + "es" if t.endswith("ss") else None
    if t.endswith("ies"):
        return t[:-3] + "y"
    if t.endswith("es") and t[:-2].endswith(("ch", "sh", "x", "ss")):
        return t[:-2]
    if t.endswith("s"):
        return t[:-1]
    if t.endswith("y") and t[-2] not in "aeiou":
        return t[:-1] + "ies"
    if t.endswith(("ch", "sh", "x")):
        return t + "es"
    return t + "s"


def units(toks, dfget, cut=CUT):
    """The query's scoring units in sorted order: ('t',) or ('t', 'o'); None when nothing folds."""
    have = sorted(set(t for t in toks if dfget(t, 0) > 0))
    out, folded, done = [], False, set()
    for t in have:
        if t in done:
            continue
        o = other(t)
        if o and o != t and dfget(o, 0) > 0 and min(dfget(t, 0), dfget(o, 0)) < cut:
            out.append((t, o))
            done.update((t, o))
            folded = True
        else:
            out.append((t,))
            done.add(t)
    return out if folded else None


class _Sidecar:
    def __init__(self, sc):
        self.con, self.n, self.avgdl = sc[0], sc[1], sc[2]

    def post(self, t):
        row = self.con.execute("select blob from p where term=?", (t,)).fetchone()
        m = {}
        if row:
            b = zlib.decompress(row[0])
            if len(b) % 12:
                raise ValueError("torn postings for %r" % t)
            for i in range(0, len(b), 12):
                pos, f, d = struct.unpack_from("<IiI", b, i)
                m[pos] = (f, d)
        return m

    def arrays(self, t):
        """(positions, f, dl) as arrays in posting order, decoded the way score_postings' fast loop does."""
        from array import array
        row = self.con.execute("select blob from p where term=?", (t,)).fetchone()
        if not row:
            return (), (), ()
        b = zlib.decompress(row[0])
        if len(b) % 12:
            raise ValueError("torn postings for %r" % t)
        w = array("I")
        w.frombytes(b)
        fs = array("i")
        fs.frombytes(b)
        return w[0::3], fs[1::3], w[2::3]

    def np_arrays(self, t):
        """arrays() as numpy views of the blob."""
        import numpy as np
        row = self.con.execute("select blob from p where term=?", (t,)).fetchone()
        b = zlib.decompress(row[0]) if row else b""
        if len(b) % 12:
            raise ValueError("torn postings for %r" % t)
        a = np.frombuffer(b, dtype=_np_dt())
        return a["p"], a["f"], a["d"]

    def slug(self, k):
        r = self.con.execute("select slug from d where pos=?", (k,)).fetchone()
        return r[0] if r else None

    def slugs(self, keys):
        """{pos: slug} for keys in one IN query a 500 (the first row per pos, as slug() and _score_pruned take it)."""
        out = {}
        keys = list(keys)
        for i in range(0, len(keys), 500):
            ch = keys[i:i + 500]
            for p, sl in self.con.execute("select pos, slug from d where pos in (%s)" % ",".join("?" * len(ch)), ch):
                out.setdefault(p, sl)
        return out


class _Overlay:
    def __init__(self, ov):
        self.ov, self.n, self.avgdl = ov, ov.n, ov.avgdl

    def post(self, t):
        ov, m = self.ov, {}
        b = ov._blob(t)
        dropped = ov._dropped
        for i in range(0, len(b), 12):
            pos, f, d = struct.unpack_from("<IiI", b, i)
            if pos not in dropped:
                m[pos] = (f, d)
        for j, (_s, tf, dl) in enumerate(ov._added):
            f = tf.get(t)
            if f:
                m[ov._base + j] = (f, dl)
        return m

    def arrays(self, t):
        """(positions, f, dl) of the merged postings - the triples post() returns - decoded by array.

        10 Nov 2026: this source had no arrays(), so score() took its slow branch for every term: one struct call a
        posting, a dict per term, and a second dict to merge a unit of one term with nothing. A 25,621-char pasted
        prompt has 1,606 distinct terms and recall scores it five times: 36 s (14.7 million struct calls). The base
        postings are sorted by position with no repeats (the overlay's own binary search relies on it), so dropping
        the re-read positions and appending the fresh documents gives post()'s triples exactly."""
        from array import array
        from itertools import compress
        ov = self.ov
        b = ov._blob(t)
        w = array("I")
        w.frombytes(b)
        g = array("i")
        g.frombytes(b)
        ps, fs, ds = w[0::3], g[1::3], w[2::3]
        dropped = ov._dropped
        if dropped and ps:
            hit = set(ps).intersection(dropped)
            if hit:
                keep = [p not in hit for p in ps]
                ps = array("I", compress(ps, keep))
                fs = array("i", compress(fs, keep))
                ds = array("I", compress(ds, keep))
        if ov._fresh_df.get(t):
            base = ov._base
            for j, (_s, tf, dl) in enumerate(ov._added):
                f = tf.get(t)
                if f:
                    ps.append(base + j)
                    fs.append(f)
                    ds.append(dl)
        return ps, fs, ds

    def np_arrays(self, t):
        """arrays() in numpy: the blob's triples less the re-read positions, then the fresh documents holding t."""
        import numpy as np
        ov = self.ov
        a = np.frombuffer(ov._blob(t), dtype=_np_dt())
        ps, fs, ds = a["p"], a["f"], a["d"]
        if ov._drop_sorted and len(ps):
            keep = ~np.isin(ps, np.asarray(ov._drop_sorted, dtype=np.int64))
            if not keep.all():
                ps, fs, ds = ps[keep], fs[keep], ds[keep]
        if ov._fresh_df.get(t):
            ex = [(ov._base + j, tf[t], dl) for j, (_s, tf, dl) in enumerate(ov._added) if tf.get(t)]
            if ex:
                ps = np.concatenate([ps.astype(np.int64), np.asarray([e[0] for e in ex], dtype=np.int64)])
                fs = np.concatenate([fs.astype(np.int64), np.asarray([e[1] for e in ex], dtype=np.int64)])
                ds = np.concatenate([ds.astype(np.int64), np.asarray([e[2] for e in ex], dtype=np.int64)])
        return ps, fs, ds

    def slug(self, k):
        ov = self.ov
        return ov._pos_slug[k] if k < ov._base else ov._added[k - ov._base][0]


class _Payload:
    def __init__(self, bm):
        self.bm, self.n, self.avgdl = bm, bm.n, bm.avgdl
        self.slugs = list(bm.tf.keys())

    def post(self, t):
        dl, m = self.bm.dl, {}
        for i, s in enumerate(self.slugs):
            f = self.bm.tf[s].get(t)
            if f:
                m[i] = (f, dl[s])
        return m

    def slug(self, k):
        return self.slugs[k]


def _source(bm):
    if type(bm).__name__ == "_FcOverlay":
        if bm._fallback is None:
            return _Overlay(bm)
        bm = bm._fallback
    sc = bm.__dict__.get("_sc")
    if sc is not None:
        return _Sidecar(sc)
    return _Payload(bm)


_DT = []


def _np_dt():
    if not _DT:
        import numpy as np
        _DT.append(np.dtype([("p", "<u4"), ("f", "<i4"), ("d", "<u4")]))
    return _DT[0]


def _score_np(src, us, topk, n, avgdl, K1, B):
    """score()'s loop on a dense float64 array (13 Nov 2026, an agent). Served recall spent 2-4 s of a long
    prompt's lex.score here: every query of 200+ distinct words has a word to fold, so the overlay's own numpy scorer
    never ran and each posting went through Python dict updates (393 updates, 2.2 s in one profiled call). The same
    expression in the same operand order, units in the same sorted order, each document's sum starting from 0.0, ties by
    position, so the list is the loop's list. None (the caller runs the loop) when a unit's positions repeat."""
    import numpy as np
    k1p1, parts, top = K1 + 1, [], 0
    for u in us:
        if len(u) == 1:
            ps, fs, ds = src.np_arrays(u[0])
            if len(ps) > 1 and not bool((ps[1:] > ps[:-1]).all()):
                return None
        else:
            got = [src.np_arrays(t) for t in u]
            for gp, _gf, _gd in got:
                if len(gp) > 1 and not bool((gp[1:] > gp[:-1]).all()):
                    return None
            ps = np.concatenate([g[0].astype(np.int64) for g in got])
            fs = np.concatenate([g[1].astype(np.int64) for g in got])
            ds = np.concatenate([g[2].astype(np.int64) for g in got])
            if len(ps):
                up, inv = np.unique(ps, return_inverse=True)
                f2 = np.zeros(len(up), dtype=np.int64)
                np.add.at(f2, inv, fs)
                d2 = np.zeros(len(up), dtype=np.int64)
                d2[inv] = ds          # the loop keeps the last term's length; a document's length is the same in both
                ps, fs, ds = up, f2, d2
        if not len(ps):
            continue
        idf = math.log(1.0 + (n - len(ps) + 0.5) / (len(ps) + 0.5))
        parts.append((idf, ps, fs, ds))
        top = max(top, int(ps[-1]) + 1)
    if not parts:
        return []
    sc = np.zeros(top, dtype=np.float64)
    for idf, ps, fs, ds in parts:
        p = ps.astype(np.int64)
        f = fs.astype(np.float64)
        d = ds.astype(np.float64)
        sc[p] = sc[p] + ((idf * f) * k1p1) / (f + K1 * (1 - B + B * d / avgdl))
    nz = np.flatnonzero(sc > 0)
    vals = sc[nz]
    if len(nz) > topk:
        kth = np.partition(-vals, topk - 1)[topk - 1]
        keep = -vals <= kth
        nz, vals = nz[keep], vals[keep]
    return [(int(nz[i]), float(vals[i])) for i in np.lexsort((nz, -vals))[:topk]]


def score(bm, query, topk=20, cut=CUT):
    """Folded BM25 (slug, score) list, or None when no query word folds or anything is in doubt."""
    import bm25
    try:
        us = units(bm25.tokens(query), bm.df.get, cut)
        if us is None:
            return None
        src = _source(bm)
        K1, B, n, avgdl = bm25.K1, bm25.B, src.n, src.avgdl
        top = None
        if topk > 0 and hasattr(src, "np_arrays") and os.environ.get("BRAIN_FOLD_NUMPY", "1") != "0":
            try:
                top = _score_np(src, us, topk, n, avgdl, K1, B)
            except Exception:
                top = None
        if top is not None:
            names = src.slugs([k for k, _s in top]) if hasattr(src, "slugs") else None
            out = []
            for k, s in top:
                sl = names.get(k) if names is not None else src.slug(k)
                if sl:
                    out.append((sl, s))
            return out
        scores = {}
        get = scores.get
        norm = bm25._LengthNorm(avgdl).__getitem__
        k1p1 = K1 + 1
        fast = hasattr(src, "arrays")
        for u in us:
            if fast and len(u) == 1:
                ps, fs, ds = src.arrays(u[0])
            else:
                m = {}
                for t in u:
                    it = zip(*src.arrays(t)) if fast else ((k, f, d) for k, (f, d) in src.post(t).items())
                    for k, f, d in it:
                        g = m.get(k)
                        m[k] = (g[0] + f, d) if g else (f, d)
                ps = list(m)
                fs = [v[0] for v in m.values()]
                ds = [v[1] for v in m.values()]
            if not len(ps):
                continue
            idf = math.log(1.0 + (n - len(ps) + 0.5) / (len(ps) + 0.5))
            # scores[k] += ((idf * f) * (K1 + 1)) / (f + K1 * (1 - B + B * d / avgdl)), posting by posting, as score_postings
            vs = map(truediv, map(mul, map(mul, repeat(idf), fs), repeat(k1p1)), map(add, fs, map(norm, ds)))
            scores.update(zip(ps, map(add, map(get, ps, repeat(0.0)), vs)))
        # (-v, k) tuples compare in C in the order the old key=lambda kv: (-kv[1], kv[0]) gave; every positive score sorts
        # before any non-positive one, so cutting the non-positive after the top-k returns the same rows; -(-v) == v.
        top = [(k, -nv) for nv, k in heapq.nsmallest(topk, zip(map(neg, scores.values()), scores.keys())) if nv < 0]
        names = src.slugs([k for k, _s in top]) if hasattr(src, "slugs") else None
        out = []
        for k, s in top:
            sl = names.get(k) if names is not None else src.slug(k)
            if sl:
                out.append((sl, s))
        return out
    except Exception:
        return None


def scorer(bm, cut=CUT):
    """bm.score with the fold: same signature, falls back to bm.score whenever score() returns None."""
    def _s(query, topk=20):
        r = score(bm, query, topk, cut)
        return r if r is not None else bm.score(query, topk)
    return _s
