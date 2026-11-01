# -*- coding: utf-8 -*-
"""Cross-family check of the Codex-drafted nodes for our 13-14 Sep probability results (claude-322bc92e, 10 Oct 2026,
T-20261010-052). For each attempt record, one sealed Claude reader (claude_reader_s11.call: no tools, nothing saved)
reads the record and the entries drafted from it and says, per entry, whether the statement says exactly what the
record establishes (hypotheses, strength, the partial/reduced labels) and whether the proof text is faithful.
Writes audit/<group>.json (verdicts + the CLI's response record) and bundle_001.json filtered to FAITHFUL entries
(the drafted file is kept as bundle_001.json.drafted)."""
import concurrent.futures as cf
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INBOX = "~/math-brain-inbox/codex-prob1000-nodes-1010"
ATT = "~/<private-repo>/06_math_research/probability_1000_attempts_I_20260914/"
sys.path.insert(0, "~/pd_work/pilot_pair")
import claude_reader_s11 as R  # noqa: E402

GROUPS = {  # key prefix -> attempt record
    "janson-problem-18-39": "Probability_F0059_Janson_problem_18_39_reduction_2026-09-14.md",
    "janson-conjecture-20-1": "Probability_F0063_Janson_conjecture_20_1_level_widths_uniformly_integrable_2026-09-14.md",
    "janson-problem-20-": "Probability_F0064b_Janson_problems_20_3_20_4_20_11_2026-09-14.md",
    "shiozawa-wang": "Probability_H0013_H0014_random_drift_destroys_compactness_for_every_delta_2026-09-14.md",
    "stepanyants": "Probability_H0019_layer_distribution_of_random_recursive_trees_2026-09-14.md",
    "neri-pinto": "Probability_H0020_Neri_Pinto_urn_contractivity_fails_2026-09-14.md",
    "aldous-fill-problem-3-44": "Probability_I0024_relaxation_time_is_not_a_linear_program_2026-09-14.md",
    "aldous-fill-problem-7-31": "Probability_I0031_distance_regular_hitting_times_2026-09-14.md",
    "aldous-fill-problem-14-12": "Probability_I0033_coalescing_on_the_cycle_2026-09-14.md",
    "hasebe-ueda-problem-3-11": "Probability_I0082_free_strong_unimodality_cauchy_2026-09-14.md",
    "hasebe-ueda-problem-3-3": "Probability_I0086_free_brownian_unimodality_sharp_constant_2026-09-14.md",
    "bandeira-randomstrasse": "Probability_I0095_sign_matrix_discrepancy_exact_small_values_2026-09-14.md",
}
ASK = """You check math-brain nodes drafted by another model from a written research record. Below is the record, then
the draft entries made from it (JSON). For EACH entry decide:
FAITHFUL - the statement says exactly what the record establishes, with the record's hypotheses and at the record's
strength (a reduction stays a reduction, a numerical check stays numerical, a partial answer stays partial), the
problem is named correctly, and any proof text follows the record without invented steps;
FIX - a precise discrepancy; give the corrected statement in full;
DROP - the record does not establish it, or the record retracts it.
Answer with one JSON object only: {"<key>": {"verdict": "FAITHFUL|FIX|DROP", "why": "...", "statement": "<corrected
statement if FIX, else empty>"}, ...} covering every key."""


def group_of(key):
    for pre in GROUPS:
        if key.startswith(pre):
            return pre
    return None


def check(pre, entries):
    out = os.path.join(HERE, "audit", "%s.json" % pre.rstrip("-"))
    if os.path.exists(out):
        return pre, json.load(io.open(out, encoding="utf-8"))
    rec = io.open(ATT + GROUPS[pre], encoding="utf-8", errors="replace").read()
    R.OUT = os.path.join(HERE, "audit")
    j = R.call(ASK + "\n\n=== RECORD ===\n" + rec + "\n\n=== DRAFT ENTRIES ===\n" + json.dumps(entries, ensure_ascii=False, indent=1))
    txt = str(j.get("result") or "")
    m = re.search(r"\{.*\}", txt, re.S)
    try:
        verdicts = json.loads(m.group(0)) if m else {}
    except ValueError:
        verdicts = {}
    res = {"verdicts": verdicts, "served": sorted((j.get("modelUsage") or {}).keys()), "stop_reason": j.get("stop_reason"),
           "rc": j.get("_rc"), "cost_usd": j.get("total_cost_usd"), "raw": txt if not verdicts else ""}
    io.open(out, "w", encoding="utf-8", newline="\n").write(json.dumps(res, ensure_ascii=False, indent=1))
    return pre, res


def main():
    os.makedirs(os.path.join(HERE, "audit"), exist_ok=True)
    src = os.path.join(INBOX, "bundle_001.json.drafted")
    if not os.path.exists(src):
        os.replace(os.path.join(INBOX, "bundle_001.json"), src)    # the integrator must not take it before the check
    b = json.load(io.open(src, encoding="utf-8"))
    groups = {}
    for e in b["entries"]:
        groups.setdefault(group_of(e["key"]), []).append(e)
    if None in groups:
        print("entries with no record:", [e["key"] for e in groups.pop(None)])
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        results = dict(ex.map(lambda kv: check(*kv), groups.items()))
    keep, tally = [], {}
    for pre, entries in groups.items():
        v = results[pre]["verdicts"]
        for e in entries:
            d = v.get(e["key"]) or {}
            verdict = str(d.get("verdict") or "UNREAD").upper()
            tally[verdict] = tally.get(verdict, 0) + 1
            if verdict == "FAITHFUL":
                keep.append(e)
            elif verdict == "FIX" and d.get("statement"):
                e = dict(e)
                head = re.match(r"\[[^\]]*\]\s*", e["statement"])
                fixed = d["statement"] if d["statement"].startswith("[") else (head.group(0) if head else "") + d["statement"]
                e["statement"] = fixed
                if e.get("kind") in ("theorem", "lemma"):
                    e["kind"], e["proof_text"] = "concept", None     # the proof was written for the old statement
                keep.append(e)
    keys = {e["key"] for e in keep}
    b2 = dict(b, entries=keep, relations=[r for r in b.get("relations") or []
                                          if r.get("from_key") in keys and r.get("to_key") in keys])
    p = os.path.join(INBOX, "bundle_001.json")
    io.open(p + ".part", "w", encoding="utf-8", newline="\n").write(json.dumps(b2, ensure_ascii=False, indent=1))
    os.replace(p + ".part", p)
    print(json.dumps({"tally": tally, "kept": len(keep), "relations": len(b2["relations"]),
                      "cost_usd": round(sum(float(r.get("cost_usd") or 0) for r in results.values()), 2),
                      "served": sorted({m for r in results.values() for m in r["served"]})}))


if __name__ == "__main__":
    main()
