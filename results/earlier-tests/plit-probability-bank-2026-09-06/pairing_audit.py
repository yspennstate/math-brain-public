# -*- coding: utf-8 -*-
"""pairing_audit.py - how the bank's items were paired (statement <-> proof), from the re-extraction that records
pair_rule / pair_gap_chars / stmt_named_elsewhere per row (extract_proofs.py, 2026-09-07 13:1x).

Joins logs/proofs_v3_pairrule.jsonl to the bank keys by digest (the digest is a function of statement + steps, so a
row and its bank item match exactly), prints the gap distribution for nearest-paired rows, and flags items whose proof
was paired by the nearest-preceding rule with a gap above THRESH characters (the mispairing class: a headless proof of
a different result following a statement whose own proof is elsewhere). Writes logs/pairing_flags_20260907.json and
prints a sample for the hand check. Keys are read for the join and the truth label only.
    python pairing_audit.py [--thresh 200]
"""
import argparse, collections, io, json, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = "<HOME>/bank_plit_keys_quarantine/plit_keys.jsonl"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--thresh", type=int, default=200); a = ap.parse_args()
    keys = {}
    for ln in io.open(KEYS, encoding="utf-8"):
        if ln.strip():
            k = json.loads(ln); keys[k["item_id"]] = k
    by_digest = {k["digest"]: iid for iid, k in keys.items()}
    rows = {}
    for ln in io.open(os.path.join(HERE, "logs", "proofs_v3_pairrule.jsonl"), encoding="utf-8"):
        if not ln.strip(): continue
        r = json.loads(ln)
        if r.get("digest") in by_digest and "pair_rule" in r:
            rows[by_digest[r["digest"]]] = r
    print("bank items joined to a re-extracted row: %d of %d" % (len(rows), len(keys)))
    rule = collections.Counter(r["pair_rule"] for r in rows.values()); print("pair_rule:", dict(rule))
    gaps = sorted(r["pair_gap_chars"] for r in rows.values() if r["pair_rule"] == "nearest")
    if gaps:
        q = lambda p: gaps[min(len(gaps) - 1, int(p * len(gaps)))]
        print("nearest-paired gap chars: median %d, p90 %d, p95 %d, p99 %d, max %d" % (q(.5), q(.9), q(.95), q(.99), gaps[-1]))
        for t in (50, 100, 200, 400, 800):
            print("   gap > %4d: %d items" % (t, sum(1 for g in gaps if g > t)))
    named = sum(1 for r in rows.values() if r["pair_rule"] == "nearest" and r["stmt_named_elsewhere"])
    print("nearest-paired items whose statement label is named by a 'Proof of' heading elsewhere:", named)
    flags = [{"item_id": iid, "pair_gap_chars": r["pair_gap_chars"], "stmt_named_elsewhere": r["stmt_named_elsewhere"],
              "n_steps": r["n_steps"], "kind": r["kind"], "paper": r["paper"], "truth": keys[iid]["truth"]}
             for iid, r in rows.items() if r["pair_rule"] == "nearest" and (r["pair_gap_chars"] > a.thresh or r["stmt_named_elsewhere"])]
    flags.sort(key=lambda f: -f["pair_gap_chars"])
    print("FLAGGED (nearest AND (gap > %d OR statement's proof is elsewhere)): %d" % (a.thresh, len(flags)))
    print("known mispaired item flagged:", [f for f in flags if f["item_id"] == "<item>"])
    json.dump(flags, io.open(os.path.join(HERE, "logs", "pairing_flags_20260907.json"), "w", encoding="utf-8"), indent=1)
    items = {}
    for ln in io.open(os.path.join(HERE, "items", "plit.jsonl"), encoding="utf-8"):
        it = json.loads(ln); items[it["item_id"]] = it
    random.seed(11)
    for f in random.sample(flags, min(10, len(flags))):
        it = items[f["item_id"]]
        print("--- %s gap %d named_elsewhere %s steps %d %s truth %s" % (f["item_id"][-8:], f["pair_gap_chars"], f["stmt_named_elsewhere"], f["n_steps"], f["kind"], f["truth"]))
        print("   S:", it["claim"][:130].replace("\n", " ")); print("   P:", it["argument_steps"][0]["text"][:130].replace("\n", " "))


if __name__ == "__main__":
    main()
