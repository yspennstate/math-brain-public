#!/usr/bin/env python3
"""Check that your copy of the math brain behaves like the reference install.

    python conformance/verify_install.py            the quick check: 50 cases, a few minutes after the first search
    python conformance/verify_install.py --all      every case (about 1,100)
    python conformance/verify_install.py --kind hook,walk --report my_report.json

Run it from a checkout of math-brain-public after tools/import_store.py has built local/population/brain.sqlite3.
It needs Python 3.11 or newer and nothing else; it is the same on Linux, macOS and Windows. It reads the cases in
conformance/cases/, runs the same tool call in this checkout, and compares what is printed with what the reference
printed. Nothing is written to your home directory (usage logging is switched off for the run).

What passes
  search, fragment  the reference's top card is in your top 3 and at least 3 of its top 5 are in your top 5
  negative          WEAK MATCH printed exactly when it printed for the reference
  walk              the walked card has the same id and the same link targets
  hook              served or silent as the reference was, valid hook JSON, and half the served cards shared
  nav               the same first card ids
A STRICT column also counts exact equality (same ids in the same order). Strict differences with loose passes
usually mean a different Python or a missing optional package for the meaning channel; loose failures mean the
install differs: a different export, a store that did not import, a hook that cannot find src/.

The first search on a new install builds the prepared fast-recall state; on a busy laptop that took about ten
minutes once, then about ten seconds a search. The check says when it is in that step.
"""
import argparse
import json
import os
import platform
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _runner as R  # noqa: E402

KINDS = ["negative", "walk", "search", "fragment", "hook", "nav"]


def load(kinds):
    rows = []
    for k in kinds:
        p = os.path.join(HERE, "cases", k + ".jsonl")
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                rows += [json.loads(x) for x in fh if x.strip()]
    return rows


def judge(case):
    k = case["kind"]
    exp = case["expect"]
    if k in ("search", "fragment", "negative"):
        rc, out, err, sec = R.recall(case["argv"])
        got = R.parse_search(out)
        if k == "negative":
            ok = got["weak"] == exp["weak"]
            strict = ok and got["ids"] == exp["ids"]
        else:
            top_ok = (not exp["ids"]) or R.overlap(got["ids"], exp["ids"][:1], 3) == 1
            ok = top_ok and R.overlap(got["ids"], exp["ids"], 5) >= min(3, len(exp["ids"][:5]))
            strict = got["ids"] == exp["ids"]
        return ok, strict, sec, {"got_top3": got["ids"][:3], "want_top3": exp["ids"][:3], "rc": rc,
                                 "err": err.strip().splitlines()[-1:] if err.strip() else []}
    if k == "walk":
        rc, out, err, sec = R.recall(case["argv"])
        got = R.parse_walk(out)
        ok = got["id"] == exp["id"] and got["link_targets"] == exp["link_targets"]
        strict = ok and got["text_sha16"] == exp["text_sha16"]
        return ok, strict, sec, {"got_id": got["id"], "links_got": len(got["link_targets"]),
                                 "links_want": len(exp["link_targets"]), "rc": rc}
    if k == "hook":
        rc, out, err, sec, why = R.hook_with_reason(case["prompt"], case["session_id"] + "-verify-%d" % os.getpid())
        got = R.parse_hook(out)
        ok = got["served"] == exp["served"] and got["shape_ok"] and rc in (0, None)
        if ok and not exp["served"]:
            # A hook that is missing or crashes is silent too; silence counts only with the reason the reference gave.
            ok = sorted(why) == sorted(case.get("silence") or [])
        if ok and exp["served"] and exp["ids"]:
            ok = R.overlap(got["ids"], exp["ids"], len(exp["ids"])) * 2 >= len(exp["ids"])
        strict = ok and got["ids"] == exp["ids"]
        return ok, strict, sec, {"served": got["served"], "want_served": exp["served"],
                                 "n_ids": len(got["ids"]), "shape_ok": got["shape_ok"], "silence": why,
                                 "over_live_budget": sec > 30}
    if k == "nav":
        rc, out, err, sec = R.nav(case["argv"])
        got = R.parse_nav(out)
        ok = got["ids"][:3] == exp["ids"][:3]
        strict = ok and got["ids"] == exp["ids"]
        return ok, strict, sec, {"got": got["ids"][:3], "want": exp["ids"][:3]}
    return False, False, 0.0, {"error": "unknown kind %s" % k}


def preflight():
    problems = []
    if sys.version_info < (3, 11):
        problems.append("Python %s is too old: install 3.11 or newer (macOS's /usr/bin/python3 is 3.9)"
                        % platform.python_version())
    store = os.environ.get("MATHBRAIN_STORE", os.path.join(R.ROOT, "local", "population", "brain.sqlite3"))
    if not os.path.exists(store):
        problems.append("no store at %s: run python tools/import_store.py --out local/population/brain.sqlite3"
                        % store)
    if not os.path.isdir(os.path.join(R.ROOT, "src", "math_brain")):
        problems.append("src/math_brain is missing: add src to the sparse checkout (git sparse-checkout add src)")
    return store, problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="run every case")
    ap.add_argument("--n", type=int, default=50, help="cases in the quick check (default 50)")
    ap.add_argument("--kind", default="", help="comma list of kinds: " + ",".join(KINDS))
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--report", default="", help="write a JSON report here")
    ap.add_argument("--show-fail", type=int, default=10, help="print the first N failures in full")
    a = ap.parse_args(argv)

    store, problems = preflight()
    print("math brain install check: python %s on %s (%s), store %s"
          % (platform.python_version(), platform.system(), platform.machine(), store))
    if problems:
        for p in problems:
            print("  FIX FIRST:", p)
        return 2
    kinds = [k for k in a.kind.split(",") if k] or KINDS
    rows = load(kinds)
    if not rows:
        print("no cases found under", os.path.join(HERE, "cases"))
        return 2
    ref = rows[0].get("ref", {})
    print("cases: %d from the reference made %s (export manifest %s)"
          % (len(rows), ref.get("made"), ref.get("export_manifest_sha16")))
    if not a.all:
        by = {}
        for r in rows:
            by.setdefault(r["kind"], []).append(r)
        rng = random.Random(a.seed)
        pick = []
        per = max(1, a.n // len(by))
        for k in kinds:
            if k == "hook" and k in by:
                # half served, half silent, so a hook that never serves cannot pass the quick check
                srv = [r for r in by[k] if r["expect"]["served"]]
                sil = [r for r in by[k] if not r["expect"]["served"]]
                pick += rng.sample(srv, min(per - per // 2, len(srv))) + rng.sample(sil, min(per // 2, len(sil)))
            elif k in by:
                pick += rng.sample(by[k], min(per, len(by[k])))
        rows = pick
    print("running %d cases; the first search may spend several minutes building the fast-recall state" % len(rows))

    results, t0 = [], time.time()
    tally = {}
    for i, case in enumerate(rows, 1):
        try:
            ok, strict, sec, info = judge(case)
        except Exception as e:   # one broken case is a failure, not the end of the check
            ok, strict, sec, info = False, False, 0.0, {"exception": "%s: %s" % (type(e).__name__, e)}
        t = tally.setdefault(case["kind"], [0, 0, 0])
        t[0] += 1
        t[1] += ok
        t[2] += strict
        results.append({"case": case["case"], "kind": case["kind"], "ok": ok, "strict": strict, "seconds": sec,
                        "info": info})
        if i % 10 == 0 or i == len(rows):
            print("  %d/%d done, %d passing, %.0f s" % (i, len(rows), sum(r["ok"] for r in results),
                                                         time.time() - t0), flush=True)

    print("\n%-10s %6s %6s %6s" % ("kind", "cases", "pass", "strict"))
    for k in kinds:
        if k in tally:
            n, ok, st = tally[k]
            print("%-10s %6d %6d %6d" % (k, n, ok, st))
    fails = [r for r in results if not r["ok"]]
    for r in fails[:a.show_fail]:
        print("FAIL", r["case"], json.dumps(r["info"], ensure_ascii=False)[:400])
    slow = [r for r in results if r["info"].get("over_live_budget") and r["info"].get("want_served")]
    if slow:
        print("NOTE: %d served hook case(s) took over 30 s here. The check lifts the hook's time limit; in a live session "
              "the hook stops at MATHBRAIN_TIME_BUDGET_S (30 s by default) and stays silent. Raise it as the README "
              "says, or expect silence on this machine." % len(slow))
    total_ok = sum(r["ok"] for r in results)
    verdict = "PASS" if total_ok >= 0.95 * len(results) else "FAIL"
    print("\n%s: %d of %d cases pass (%.1f%%); %d strict"
          % (verdict, total_ok, len(results), 100.0 * total_ok / len(results), sum(r["strict"] for r in results)))
    if verdict == "FAIL":
        print("Read conformance/README.md, section 'When it fails', for what each kind of failure means.")
    if a.report:
        with open(a.report, "w", encoding="utf-8") as fh:
            json.dump({"verdict": verdict, "python": platform.python_version(), "system": platform.system(),
                       "machine": platform.machine(), "tally": tally, "results": results}, fh, indent=1)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
