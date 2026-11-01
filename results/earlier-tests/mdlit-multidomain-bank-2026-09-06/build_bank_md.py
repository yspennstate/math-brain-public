# -*- coding: utf-8 -*-
"""build_bank_md.py - the multi-domain literature proof bank (mdlit_v1): items in the analytical-bank-item/v1 shape
the earlier lanes and the probability bank share, keys sealed in a quarantine directory the solver and the notes
builder never read, a certificate on every item.

    python build_bank_md.py --proofs proofs.jsonl --target 6250 --clean-share 0.2 --seed 20260906

Population: accepted theorem/lemma/proposition/corollary proofs from the harvested arXiv sources (extract_proofs_md.py),
deduplicated by text digest, papers listed by the probability campaign EXCLUDED (the two banks stay disjoint). Each
proof contributes at most ONE item: a flawed item (one step changed at one place by mutate_md.py) or a clean item
(the proof as published), never both. Flawed proofs are drawn round-robin over the four domain groups, and the
operator per proof is balanced toward TARGET_SHARE so no mechanism dominates; a step that restates the claim is never a
site (the 2026-08-17 scar).

Items (items/mdlit.jsonl): item_id, schema, bank_version, claim, argument_steps, prompt, provenance (lane, date, release,
kind). No paper id, no domain, no operator, no step marker.
Keys (<HOME>/bank_multidomain_keys_quarantine/mdlit_keys.jsonl): truth, fault_step, family_id (= operator),
mechanism, taxonomy, tier, difficulty (+score), the provenance (arxiv id, kind, env, theorem label, published, domain
group, primary category, categories, title), the certificate hashes (proof_sha256 over statement + clean steps,
mutation_sha256 over the exact edit), before/after/removed/inserted and the clean step text.
"""
import argparse
import collections
import hashlib
import io
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mutate_md as mutate  # noqa: E402

ITEMS_OUT = os.path.join(HERE, "items", "mdlit.jsonl")
KEYS_DIR = "<HOME>/bank_multidomain_keys_quarantine"
KEYS_OUT = os.path.join(KEYS_DIR, "mdlit_keys.jsonl")
PEER_LISTING = "<HOME>/arxiv_mathpr_sources/listing.jsonl"
BANK_VERSION = "mdlit_v1"
LANE = "campaign-2026-09-06-multidomain-bank-f4"
PROMPT_TEXT = ("Audit the numbered mathematical argument. Return VALID if every step is valid. Otherwise identify "
               "the first invalid step, explain the exact error, and give the minimal corrected step.")
TARGET_SHARE = {
    "ineq_flip": 0.14, "ineq_to_eq": 0.04, "word_flip": 0.08, "quantifier_swap": 0.03, "quant_word": 0.04,
    # 2026-09-06 12:1x hand-read of 61 dry items: the symbolic operators run ~95 pct valid, the two hypothesis operators
    # ~75 pct even after the re-citation guards - their share is halved (0.09 -> 0.05 each) and const_change takes it.
    "sign_flip": 0.06, "hypothesis_drop": 0.05, "hypothesis_swap": 0.05, "const_change": 0.12, "limit_target": 0.03,
    "index_shift": 0.06, "sum_bound_shift": 0.04, "theorem_swap": 0.05, "ref_shift": 0.06, "limit_order": 0.03,
    "interchange": 0.03, "limop_swap": 0.04, "setop_swap": 0.02,
}


def item_id(paper, digest, op, step, start):
    h = hashlib.sha256(("%s|%s|%s|%s|%s" % (paper, digest, op, step, start)).encode("utf-8")).hexdigest()
    return "mdlit_" + h[:24]


def proof_sha(r):
    return hashlib.sha256((r["statement"] + "\n" + "\n".join(r["steps"])).encode("utf-8")).hexdigest()


def theorem_label(r):
    parts = [r.get("env", ""), r.get("stmt_opt", "")] + list(r.get("labels") or [])
    return " | ".join(p for p in parts if p)


def provenance():
    return {"author_lane": LANE, "authored_on": time.strftime("%Y-%m-%d"), "bank_release": BANK_VERSION,
            "kind": "mathematical_argument"}


def load_peer_ids(path):
    ids = set()
    if os.path.exists(path):
        for ln in io.open(path, encoding="utf-8"):
            try:
                ids.add(json.loads(ln)["base_id"])
            except Exception:
                pass
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proofs", default=os.path.join(HERE, "proofs.jsonl"))
    ap.add_argument("--target", type=int, default=6250)
    ap.add_argument("--clean-share", type=float, default=0.2)
    ap.add_argument("--seed", type=int, default=20260906)
    ap.add_argument("--max-ext-refs", type=int, default=2)
    ap.add_argument("--max-steps", type=int, default=20)
    ap.add_argument("--exclude-listing", default=PEER_LISTING)
    ap.add_argument("--exclude-ids", default="<HOME>/arxiv_multidomain_sources/EXCLUDE_IDS.txt",
                    help="one arXiv base id per line, never in the bank (2026-09-06: papers reserved for another lane's calibration)")
    ap.add_argument("--items-out", default=ITEMS_OUT)
    ap.add_argument("--keys-out", default=KEYS_OUT)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    peer_ids = load_peer_ids(a.exclude_listing)
    if a.exclude_ids and os.path.exists(a.exclude_ids):
        peer_ids |= {ln.strip() for ln in io.open(a.exclude_ids, encoding="utf-8") if ln.strip() and not ln.startswith("#")}
    rows, seen, excluded_peer = [], set(), 0
    for ln in io.open(a.proofs, encoding="utf-8"):
        if not ln.strip():
            continue
        r = json.loads(ln)
        if not r.get("accept"):
            continue
        if r["external_refs"] > a.max_ext_refs or r["n_steps"] > a.max_steps:
            continue
        if r["digest"] in seen:
            continue
        if r["paper"] in peer_ids:
            excluded_peer += 1
            continue
        seen.add(r["digest"])
        rows.append(r)
    rng.shuffle(rows)
    n_clean_target = int(round(a.target * a.clean_share))
    n_flawed_target = a.target - n_clean_target
    # clean items from the tail (spread over groups), flawed from the head, disjoint proofs
    by_group = collections.defaultdict(list)
    for r in rows:
        by_group[r.get("domain_group") or "?"].append(r)
    groups = sorted(by_group)
    clean_rows, flawed_pool = [], []
    quota = {g: 0 for g in groups}
    k = 0
    while len(clean_rows) < n_clean_target and any(by_group[g] for g in groups):
        g = groups[k % len(groups)]
        k += 1
        if by_group[g]:
            clean_rows.append(by_group[g].pop())
    # round-robin order over groups for the flawed pool
    idx = {g: 0 for g in groups}
    while True:
        moved = False
        for g in groups:
            if idx[g] < len(by_group[g]):
                flawed_pool.append(by_group[g][idx[g]])
                idx[g] += 1
                moved = True
        if not moved:
            break
    items, keys = [], []
    op_count = collections.Counter()
    skipped = collections.Counter()
    for r in clean_rows:
        iid = item_id(r["paper"], r["digest"], "clean", 0, 0)
        items.append({"item_id": iid, "schema": "analytical-bank-item/v1", "bank_version": BANK_VERSION, "claim": r["statement"],
                      "argument_steps": [{"n": i + 1, "text": s} for i, s in enumerate(r["steps"])], "prompt": PROMPT_TEXT,
                      "provenance": provenance()})
        keys.append({"item_id": iid, "schema": "mdlit-key/v1", "truth": "clean", "fault_step": None, "family_id": "clean",
                     "mechanism": "none", "taxonomy": "none", "tier": "-", "difficulty": "-", "difficulty_score": None,
                     "ambiguity_stratum": "instance", "paper": r["paper"], "arxiv_id": r["paper"], "kind": r["kind"], "env": r.get("env"),
                     "theorem_label": theorem_label(r), "published": r["published"], "domain_group": r.get("domain_group"),
                     "primary_category": r.get("primary_category"), "categories": r.get("categories"), "n_steps": r["n_steps"],
                     "external_refs": r["external_refs"], "digest": r["digest"], "title": r["title"],
                     "proof_sha256": proof_sha(r), "mutation_sha256": None})
    n_flawed = 0
    for r in flawed_pool:
        if n_flawed >= n_flawed_target:
            break
        cands = mutate.candidates(r["steps"], r["statement"], domain_group=r.get("domain_group") or "")
        if not cands:
            skipped["no_candidates"] += 1
            continue
        by_op = collections.defaultdict(list)
        for c in cands:
            by_op[c[0]].append(c)
        total = sum(op_count.values()) + 1.0
        ops = sorted(by_op)
        weights = [TARGET_SHARE.get(o, 0.02) / (op_count[o] / total + 0.01) for o in ops]
        o = rng.choices(ops, weights=weights, k=1)[0]
        c = rng.choice(by_op[o])
        new_steps, info = mutate.apply(r["steps"], c)
        if new_steps == r["steps"] or new_steps[info["step"] - 1] in r["steps"]:
            skipped["no_op_or_duplicate"] += 1
            continue
        iid = item_id(r["paper"], r["digest"], info["op"], info["step"], c[2])
        items.append({"item_id": iid, "schema": "analytical-bank-item/v1", "bank_version": BANK_VERSION, "claim": r["statement"],
                      "argument_steps": [{"n": i + 1, "text": s} for i, s in enumerate(new_steps)], "prompt": PROMPT_TEXT,
                      "provenance": provenance()})
        keys.append({"item_id": iid, "schema": "mdlit-key/v1", "truth": "flawed", "fault_step": info["step"],
                     "family_id": info["op"], "mechanism": info["mechanism"], "taxonomy": info["taxonomy"], "tier": info["tier"],
                     "difficulty": info["difficulty"], "difficulty_score": info["difficulty_score"],
                     "ambiguity_stratum": "instance", "paper": r["paper"], "arxiv_id": r["paper"], "kind": r["kind"], "env": r.get("env"),
                     "theorem_label": theorem_label(r), "published": r["published"], "domain_group": r.get("domain_group"),
                     "primary_category": r.get("primary_category"), "categories": r.get("categories"), "n_steps": r["n_steps"],
                     "external_refs": r["external_refs"], "digest": r["digest"], "title": r["title"],
                     "proof_sha256": proof_sha(r), "mutation_sha256": info["mutation_sha256"],
                     "before": info["before"], "after": info["after"], "removed": info["removed"], "inserted": info["inserted"],
                     "start": info["start"], "end": info["end"], "clean_step_text": r["steps"][info["step"] - 1]})
        op_count[info["op"]] += 1
        n_flawed += 1
    rng.shuffle(items)
    order = {it["item_id"]: k for k, it in enumerate(items)}
    keys.sort(key=lambda k: order[k["item_id"]])
    os.makedirs(os.path.dirname(a.items_out), exist_ok=True)
    os.makedirs(os.path.dirname(a.keys_out), exist_ok=True)
    with io.open(a.items_out, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    with io.open(a.keys_out, "w", encoding="utf-8") as f:
        for k in keys:
            f.write(json.dumps(k, ensure_ascii=False) + "\n")
    leak = any(any(fld in it for fld in ("fault_step", "truth", "before", "paper", "arxiv_id", "domain_group", "taxonomy", "family_id"))
               for it in items)
    flawed_keys = [k for k in keys if k["truth"] == "flawed"]
    report = {
        "bank_version": BANK_VERSION, "seed": a.seed, "proofs_accepted_input": len(rows), "proofs_excluded_peer_listing": excluded_peer,
        "n_items": len(items), "n_clean": len(items) - len(flawed_keys), "n_flawed": len(flawed_keys),
        "skipped": dict(skipped),
        "by_operator": dict(op_count),
        "by_taxonomy": dict(collections.Counter(k["taxonomy"] for k in flawed_keys)),
        "by_tier": dict(collections.Counter(k["tier"] for k in flawed_keys)),
        "by_difficulty": dict(collections.Counter(k["difficulty"] for k in flawed_keys)),
        "by_domain_group": dict(collections.Counter(k["domain_group"] for k in keys)),
        "by_domain_group_flawed": dict(collections.Counter(k["domain_group"] for k in flawed_keys)),
        "by_primary_category": dict(collections.Counter(k["primary_category"] for k in keys)),
        "by_kind": dict(collections.Counter(k["kind"] for k in keys)),
        "by_year": dict(collections.Counter(str(k["published"])[:4] for k in keys)),
        "papers": len({k["paper"] for k in keys}), "distinct_proofs": len({k["digest"] for k in keys}),
        "external_refs_hist": dict(collections.Counter(k["external_refs"] for k in keys)),
        "steps_hist": dict(collections.Counter(min(k["n_steps"], 20) for k in keys)),
        "items_file": a.items_out, "keys_file": a.keys_out, "items_leak_check": "FAIL" if leak else "PASS",
        "items_sha256": hashlib.sha256(open(a.items_out, "rb").read()).hexdigest(),
        "keys_sha256": hashlib.sha256(open(a.keys_out, "rb").read()).hexdigest(),
        "built_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    with io.open(os.path.join(HERE, "BUILD_REPORT.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1)
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
