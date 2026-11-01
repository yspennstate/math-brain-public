# -*- coding: utf-8 -*-
# Copied from the probability campaign's run_plit_wrapper.py (2026-09-06) and re-pointed at the multi-domain bank; that lane's file is never edited from here.

"""run_md_wrapper.py - the probability-literature bank (plit_v1) on the inherited sterile runner.

Same machinery as the B12/B13 wrappers (run_bank10k.py: fingerprint guards, sterile serving, served-model
census, transcript receipts, per-item resume) with the paths, seed and sampler fixed by PROTOCOL_MDLIT.md:
items/plit.jsonl, keys in <HOME>/bank_plit_keys_quarantine/, every artifact under run_md/ (or the
directory MDLIT_RUN_DIR names), the solver from BANK_MODEL, and NO TOOLS for the solver (an audit must come from
reading the argument, never from a shell).

    set BANK_MODEL=claude-opus-5
    python run_md_wrapper.py sample --n 80 [--stage 0]      # pilot: 60 flawed + 20 clean, stratified by operator
    python md_notes_bm25.py --run run_md                  # brain + placebo notes
    python run_md_wrapper.py serve --arm none --concurrency 1
    python grade_md.py --run run_md
"""
import collections
import glob
import hashlib
import io
import json
import os
import random
import sys
from validity_gate import ValidityError, read_review, validate_sample

HERE = os.path.dirname(os.path.abspath(__file__))
BANK10K = os.path.join(os.path.expanduser("~"), "ai-memories-and-functionality", "06_math_research",
                       "probability_open_problem_campaign_2026_08_09", "eval", "bank10k")
sys.path.insert(0, BANK10K)
import run_bank10k as rb  # noqa: E402

RUN_PLIT = os.path.join(HERE, os.environ.get("MDLIT_RUN_DIR") or "run_md")
os.makedirs(RUN_PLIT, exist_ok=True)
rb.RUN = RUN_PLIT
rb.ITEMS = os.path.join(HERE, "items", "mdlit.jsonl")
rb.KEYS = r"<HOME>/bank_multidomain_keys_quarantine\mdlit_keys.jsonl"
rb.SEED = 20260916

# no tools for the solver (PROTOCOL_MDLIT.md): sterile settings AND an empty tool list
_orig_sterile = rb._sterile_args


# 2026-09-06 17:0x: NO MCP SERVERS - the same fix run_plit_wrapper.py got at 11:1x. Under
# load the CLI spends its whole probe budget starting the claude.ai connector servers unless the MCP config is
# strict and empty (memory claude_p_hangs_on_mcp_connector_startup_under_load_strict_mcp_config_2026_09_06). The
# solver never had tools (--tools ""), so this only removes the startup hang. Effort from BANK_EFFORT (default high).
EMPTY_MCP = os.path.join(HERE, "empty_mcp.json")
EFFORT = os.environ.get("BANK_EFFORT", "high")


def _sterile_no_tools():
    return list(_orig_sterile()) + ["--tools", "", "--effort", EFFORT,
                                    "--strict-mcp-config", "--mcp-config", EMPTY_MCP]


rb._sterile_args = _sterile_no_tools

# keep every grade artifact under run_md/ (the inherited cmd_grade writes to bank10k/results/)
_dump_atomic_orig = rb.dump_atomic
_shared_results = os.path.join(BANK10K, "results")


def _dump_atomic_redirected(path, obj):
    if os.path.abspath(os.path.dirname(path)) == os.path.abspath(_shared_results):
        os.makedirs(os.path.join(RUN_PLIT, "results"), exist_ok=True)
        path = os.path.join(RUN_PLIT, "results", os.path.basename(path))
    return _dump_atomic_orig(path, obj)


rb.dump_atomic = _dump_atomic_redirected

REVIEW = os.path.join(HERE, "VALIDITY_REVIEW.json")
_load_sample_orig = rb.load_sample
_grade_orig = rb.cmd_grade


def _load_sample_validated():
    try:
        with open(os.path.join(rb.RUN, "SAMPLE.json"), encoding="utf-8") as handle:
            sample = json.load(handle)
        items, _ = rb.load_bank()
        validate_sample(sample, REVIEW, items)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit("MDLIT VALIDITY GATE: " + str(exc)) from exc
    return _load_sample_orig()


def _grade_validated(args):
    _load_sample_validated()
    return _grade_orig(args)


rb.load_sample = _load_sample_validated
rb.cmd_grade = _grade_validated


def served_anywhere():
    ids = set()
    for f in glob.glob(os.path.join(HERE, "run_md*", "verdicts", "*", "*.json")):
        ids.add(os.path.basename(f)[:-5])
    return ids


def cmd_sample_plit(args):
    """PROTOCOL_MDLIT.md sampler: flawed items stratified over operators (floor per operator, then proportional),
    clean items at the requested share, never-served items only, seeded by stage."""
    if os.path.exists(os.path.join(rb.RUN, "SAMPLE.json")):
        raise SystemExit("preserve the frozen sample; choose a fresh MDLIT_RUN_DIR")
    if args.n < 1 or not 0 <= args.clean_share <= 1 or args.floor < 0:
        raise SystemExit("invalid sample size, clean share, or operator floor")
    try:
        invalid, receipt = read_review(REVIEW)
    except ValidityError as exc:
        raise SystemExit("MDLIT VALIDITY GATE: " + str(exc)) from exc
    items, keys = rb.load_bank()
    exclude = served_anywhere()
    elig = [i for i in items if i not in exclude and i not in invalid]
    flawed = sorted(i for i in elig if keys[i].get("truth") == "flawed")
    clean = sorted(i for i in elig if keys[i].get("truth") == "clean")
    n_clean = round(args.n * args.clean_share)
    n_flawed = args.n - n_clean
    if len(flawed) < n_flawed or len(clean) < n_clean:
        raise SystemExit("not enough eligible items for the requested sample and clean share")
    rng = random.Random(rb.SEED + int(args.stage or 0))
    by_op = collections.defaultdict(list)
    for i in flawed:
        by_op[keys[i]["family_id"]].append(i)
    total = sum(len(v) for v in by_op.values())
    picked = []
    for o in sorted(by_op):
        pool = sorted(by_op[o])
        picked += rng.sample(pool, min(args.floor, len(pool)))
    quota = {o: max(0, round((n_flawed - len(picked)) * len(by_op[o]) / total)) for o in by_op} if total else {}
    for o in sorted(by_op):
        rest = sorted(set(by_op[o]) - set(picked))
        picked += rng.sample(rest, min(quota[o], len(rest)))
    rest = sorted(set(flawed) - set(picked))
    if len(picked) < n_flawed and rest:
        picked += rng.sample(rest, min(n_flawed - len(picked), len(rest)))
    picked = picked[:n_flawed]
    picked_clean = rng.sample(clean, min(n_clean, len(clean)))
    sample = {
        "seed": rb.SEED + int(args.stage or 0), "stage": int(args.stage or 0),
        "protocol": "PROTOCOL_MDLIT.md",
        "protocol_amendment": "VALIDITY_GATE_AMENDMENT.md",
        "validity_gate": receipt,
        "excluded_served_ids": len(exclude),
        "bank_fingerprint": rb.bank_fingerprint(items),
        "sampled_text_hash": rb.sampled_text_hash(items, sorted(picked) + sorted(picked_clean)),
        "requested": args.n, "n_faulted": len(picked), "n_clean": len(picked_clean),
        "n_faulted_by_operator": dict(collections.Counter(keys[i]["family_id"] for i in picked)),
        "n_faulted_by_tier": dict(collections.Counter(keys[i]["tier"] for i in picked)),
        "n_faulted_by_ext_refs": dict(collections.Counter(keys[i]["external_refs"] for i in picked)),
        "n_primary_metric_items": len(picked),
        "cost_note": "three arms x %d items; %s sterile serves, no tools" % (len(picked) + len(picked_clean), os.environ.get("BANK_MODEL", rb.MODEL)),
        "item_ids": sorted(picked) + sorted(picked_clean),
    }
    validate_sample(sample, REVIEW, items)
    rb.dump_atomic(os.path.join(rb.RUN, "SAMPLE.json"), sample)
    print(json.dumps({k: v for k, v in sample.items() if k != "item_ids"}, indent=1))
    print("frozen to", os.path.join(rb.RUN, "SAMPLE.json"))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument("sample")
        ap.add_argument("--n", type=int, default=80)
        ap.add_argument("--stage", type=int, default=0)
        ap.add_argument("--clean-share", type=float, default=0.25)
        ap.add_argument("--floor", type=int, default=3)
        cmd_sample_plit(ap.parse_args())
    else:
        rb.main()
