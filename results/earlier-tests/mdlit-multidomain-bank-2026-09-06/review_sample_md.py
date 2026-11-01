# -*- coding: utf-8 -*-
# Copied from the probability campaign's review_sample.py (2026-09-06) and re-pointed at the multi-domain bank; that lane's file is never edited from here.

"""review_sample_md.py - the hand-read validity sample of the bank: prints N flawed items stratified over operators,
each with the ORIGINAL step beside the CHANGED step and the statement, for a human judgement recorded in
VALIDITY_REVIEW.json ({item_id: {"valid": "yes"|"no"|"unsure", "note": ...}}). Reads keys (quarantine) and items;
writes only the review file when --record is given. Judge BEFORE opening any verdict (PROTOCOL_MDLIT.md).

    python review_sample_md.py --n 60 --seed 20260906 --list > logs/validity_sample.txt
    python review_sample_md.py --record reviews.json       # merge a judgements file into VALIDITY_REVIEW.json
    python review_sample_md.py --summary                    # per-tier / per-operator validity with 95 pct intervals
"""
import argparse
import collections
import io
import json
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = "<HOME>/bank_multidomain_keys_quarantine/mdlit_keys.jsonl"
ITEMS = os.path.join(HERE, "items", "mdlit.jsonl")
REVIEW = os.path.join(HERE, "VALIDITY_REVIEW.json")


def wilson(k, n, z=1.96):
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return [(c - h) / d, (c + h) / d]


def load_keys():
    return [json.loads(l) for l in io.open(KEYS, encoding="utf-8") if l.strip()]


def sample_ids(n, seed):
    keys = [k for k in load_keys() if k["truth"] == "flawed"]
    rng = random.Random(seed)
    by_op = collections.defaultdict(list)
    for k in keys:
        by_op[k["family_id"]].append(k)
    ops = sorted(by_op)
    per = max(1, n // len(ops))
    picked = []
    for o in ops:
        pool = by_op[o]
        picked += rng.sample(pool, min(per, len(pool)))
    rest = [k for k in keys if k not in picked]
    rng.shuffle(rest)
    picked += rest[: max(0, n - len(picked))]
    return picked[:n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=60)
    ap.add_argument("--seed", type=int, default=20260906)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--record", default="")
    ap.add_argument("--summary", action="store_true")
    a = ap.parse_args()
    if a.list:
        items = {}
        for ln in io.open(ITEMS, encoding="utf-8"):
            it = json.loads(ln)
            items[it["item_id"]] = it
        for k in sample_ids(a.n, a.seed):
            it = items[k["item_id"]]
            print("=" * 100)
            print("ITEM", k["item_id"], "| op", k["family_id"], "tier", k["tier"], "| step", k["fault_step"], "of", k["n_steps"],
                  "|", k["kind"], k["paper"], "| ext refs", k["external_refs"])
            print("STATEMENT:", it["claim"][:900].replace("\n", " "))
            for s in it["argument_steps"]:
                mark = ">>" if s["n"] == k["fault_step"] else "  "
                print("%s %d. %s" % (mark, s["n"], s["text"][:700].replace("\n", " ")))
            print("ORIGINAL STEP %d: %s" % (k["fault_step"], k["clean_step_text"][:700].replace("\n", " ")))
            print("REMOVED %r -> INSERTED %r" % (k["removed"], k["inserted"]))
        return
    if a.record:
        new = json.load(io.open(a.record, encoding="utf-8"))
        cur = json.load(io.open(REVIEW, encoding="utf-8")) if os.path.exists(REVIEW) else {}
        cur.update(new)
        with io.open(REVIEW, "w", encoding="utf-8") as f:
            json.dump(cur, f, indent=1, ensure_ascii=False)
        print("recorded", len(new), "total", len(cur))
        return
    if a.summary:
        cur = json.load(io.open(REVIEW, encoding="utf-8"))
        keys = {k["item_id"]: k for k in load_keys()}
        by = collections.defaultdict(lambda: [0, 0, 0])
        for iid, v in cur.items():
            k = keys.get(iid)
            if not k:
                continue
            for g in ("ALL", "tier " + k["tier"], k["family_id"]):
                by[g][2] += 1
                if v.get("valid") == "yes":
                    by[g][0] += 1
                elif v.get("valid") == "no":
                    by[g][1] += 1
        for g, (y, n, t) in sorted(by.items()):
            ci = wilson(y, t)
            print("%-18s valid %2d / not %2d / unsure %2d of %2d  valid rate %.2f  CI %s" % (
                g, y, n, t - y - n, t, y / t if t else 0, "-" if ci is None else "[%.2f, %.2f]" % tuple(ci)))


if __name__ == "__main__":
    main()
