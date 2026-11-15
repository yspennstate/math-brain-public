"""test_unconscious_demotion.py - recall shows an unconscious-tier stub on its own lexical evidence, last, and nothing
else moves (28 Sep 2026, an agent; scheduled audit account03/B02 r67, B02-R1-UNCONSCIOUS-TIER-LEXICAL-SUPPRESSION-001).

    python test_unconscious_demotion.py [--old OLD_BRAIN.py] [--new NEW_BRAIN.py] [--probes 40] [--real 60] [--json OUT]

Both versions run recall(query, 60) on the live index with the recall logs off, and their displayed rows are compared on
three query sets: probes built from unconscious stubs' own names, the 56 owner-voice bank questions, and the newest
distinct queries in the live recall log (recorded by hash only). Counted per query: whether an unconscious stub is
among the BM25 top 60 (engagement), whether one is displayed in the first 8 and the first 60 rows, and whether the
displayed sequence of every other memory is identical between the versions. The contract the new version must meet:
 C1 a stub that is its query's best BM25 hit, with nothing else lifting it, is displayed (the old version never
    showed one on lexical evidence alone)
 C2 a displayed stub comes after every other displayed row
 C3 on every query the non-stub rows are displayed identically, in the same order, at 8 rows and at 60
 C4 BRAIN_RECALL_UNCONSCIOUS=gate reproduces the old display on the probes

NOT THE LIVE CONTRACT (13 Nov 2026, an agent): the demotion this test was written for did not land. brain.py keeps
the gate (see the comment at `if tier.get(slug) == "unconscious"` in recall): a stub found only by its words is not shown,
so C1 fails on today's brain.py by design (3 of 3 probes, 13 Nov). This is an A/B of two files, not a check to rerun
against the live code; with --old and --new the same file its own pass rule (`not old_c1`) cannot hold either.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import sys

DR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DR)
os.environ["BRAIN_RECALL_LOG"] = "0"
os.environ["RECALL_REWRITE_NO_LOG"] = "1"
ARGS = sys.argv[1:]


def arg(name, default=None):
    return ARGS[ARGS.index(name) + 1] if name in ARGS else default


OLD = arg("--old", os.path.join(DR, "brain.py"))
NEW = arg("--new", os.path.join(DR, "brain_r67_candidate.py"))
PLAIN = re.compile(r"^\s*\d\.\d\d\s+\[[^\]]*\]\s+(\S+)", re.M)
STOP = {"the", "a", "of", "and", "to", "in", "is", "on", "for"}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def shown(mod, q, n):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            mod.recall(q, n=n)
        except SystemExit:
            pass
    return PLAIN.findall(buf.getvalue())


def stubs():
    out = []
    for line in io.open(os.path.join(DR, "consciousness.tsv"), encoding="utf-8", errors="replace"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 2 and p[1] == "unconscious":
            out.append(p[0][:-3] if p[0].endswith(".md") else p[0])
    return sorted(out)


def probe(slug):
    words = [w for w in slug.split("_") if w and not re.fullmatch(r"20\d\d|\d\d", w) and w not in STOP]
    return " ".join(words)


def main():
    old, new = load(OLD, "brain_old_r67"), load(NEW, "brain_new_r67")
    tier = set(stubs())
    from bm25 import BM25, QueryNormalizer
    bm = BM25()
    qn = QueryNormalizer(bm.df)
    k = int(arg("--probes", "40"))
    sl = stubs()
    probes = [("probe", probe(s), s) for s in sl[::max(1, len(sl) // k)][:k]]
    import eval_brain_recall_fresh as fresh
    bank = [("bank", q, None) for q, _g in (fresh.BANK + fresh.BANK_V2_EXTRA)]
    real, seen = [], set()
    rl = os.path.join(os.path.expanduser("~"), ".claude", "brain_graph", "live", "recall_log.jsonl")
    try:
        lines = open(rl, "rb").read().decode("utf-8", "replace").splitlines()[-4000:]
    except OSError:
        lines = []
    for l in reversed(lines):
        try:
            q = json.loads(l).get("q")
        except ValueError:
            continue
        if q and q not in seen and len(q) < 400:
            seen.add(q)
            real.append(("real", q, None))
        if len(real) >= int(arg("--real", "60")):
            break
    rows, fails = [], []
    for kind, q, target in probes + bank + real:
        top60 = [s for s, _b in bm.score(qn.normalize(q), 60)]
        eng = [s for s in top60 if s in tier]
        r = {"kind": kind, "q_sha": hashlib.sha256(q.encode("utf-8")).hexdigest()[:16], "stub_in_bm25_top60": len(eng),
             "target_is_top_bm25": bool(target and top60 and top60[0] == target)}
        if kind != "real":
            r["q"] = q
        for n in (8, 60):
            a, b = shown(old, q, n), shown(new, q, n)
            r["old_%d" % n] = [s for s in a if s in tier]
            r["new_%d" % n] = [s for s in b if s in tier]
            r["others_same_%d" % n] = [s for s in a if s not in tier] == [s for s in b if s not in tier]
            first_stub = next((i for i, s in enumerate(b) if s in tier), None)
            r["stub_last_%d" % n] = first_stub is None or all(s in tier for s in b[first_stub:])
        if target:
            r["target_shown_old"], r["target_shown_new"] = target in r["old_60"], target in r["new_60"]
        rows.append(r)
    pr = [r for r in rows if r["kind"] == "probe"]
    clean = [r for r in pr if r["target_is_top_bm25"]]
    c1 = [r for r in clean if r["target_shown_new"]]
    old_c1 = [r for r in clean if r["target_shown_old"]]
    c2 = all(r["stub_last_8"] and r["stub_last_60"] for r in rows)
    c3 = all(r["others_same_8"] and r["others_same_60"] for r in rows)
    os.environ["BRAIN_RECALL_UNCONSCIOUS"] = "gate"
    gate_same = [shown(new, r["q"], 60) == shown(old, r["q"], 60) for r in pr[:10]]
    os.environ.pop("BRAIN_RECALL_UNCONSCIOUS")
    summary = {"queries": {k2: sum(1 for r in rows if r["kind"] == k2) for k2 in ("probe", "bank", "real")},
               "engagement_stub_in_bm25_top60": {k2: sum(1 for r in rows if r["kind"] == k2 and r["stub_in_bm25_top60"])
                                                 for k2 in ("probe", "bank", "real")},
               "stub_shown_at_8": {"old": sum(1 for r in rows if r["old_8"]), "new": sum(1 for r in rows if r["new_8"])},
               "stub_shown_at_60": {"old": sum(1 for r in rows if r["old_60"]), "new": sum(1 for r in rows if r["new_60"])},
               "C1": {"probes_whose_stub_is_the_top_bm25_hit": len(clean), "shown_new": len(c1), "shown_old": len(old_c1)},
               "C2_stubs_after_every_other_row": c2, "C3_other_rows_identical": c3,
               "C4_gate_reproduces_old_on_probes": "%d of %d" % (sum(gate_same), len(gate_same))}
    ok = len(clean) > 0 and len(c1) == len(clean) and not old_c1 and c2 and c3 and all(gate_same)
    print(json.dumps(summary, indent=1))
    print("PASS" if ok else "FAIL")
    out = arg("--json")
    if out:
        json.dump({"summary": summary, "pass": ok, "old_sha256": hashlib.sha256(open(OLD, "rb").read()).hexdigest(),
                   "new_sha256": hashlib.sha256(open(NEW, "rb").read()).hexdigest(), "rows": rows},
                  open(out, "w", encoding="utf-8"), indent=1)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
