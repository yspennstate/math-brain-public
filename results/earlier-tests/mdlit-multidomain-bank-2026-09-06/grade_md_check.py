# -*- coding: utf-8 -*-
# Copied from the probability campaign's grade_plit_check.py (2026-09-06) and re-pointed at the multi-domain bank; that lane's file is never edited from here.

"""grade_md_check.py - the independent re-derivation of grade_md.py's numbers, by a different data path.

Reads every verdict file's RAW json text (not through the grader's loader), parses the verdict and the step with its
own regexes, reads the keys file line by line, recomputes each arm's rates, the paired discordant counts and the
exact McNemar p-value with its own binomial code, and prints every disagreement with <run>/results/<LABEL>.json.
An empty disagreement list is the receipt; a non-empty one blocks the report.

    python grade_md_check.py [--run run_md] [--label PILOT] [--arms none,brain,placebo]
"""
import argparse
import io
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = "<HOME>/bank_multidomain_keys_quarantine/mdlit_keys.jsonl"


def binom_two_sided(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = 0.0
    for i in range(k + 1):
        tail += math.comb(n, i)
    p = 2.0 * tail / (2.0 ** n)
    return 1.0 if p > 1.0 else p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="run_md")
    ap.add_argument("--label", default="PILOT")
    ap.add_argument("--arms", default="none,brain,placebo")
    ap.add_argument("--extra-arm", action="append", default=[], help="NAME=RUNDIR[:ARM], as for grade_md.py")
    a = ap.parse_args()
    run = a.run if os.path.isabs(a.run) else os.path.join(HERE, a.run)
    arms = [x.strip() for x in a.arms.split(",") if x.strip()]
    arm_dir = {arm: (run, arm) for arm in arms}
    for spec in a.extra_arm:
        name, rest = spec.split("=", 1)
        rd, _, served_as = rest.partition(":")
        rd = rd if os.path.isabs(rd) else os.path.join(HERE, rd)
        arm_dir[name] = (rd, served_as or "brain")
        arms.append(name)
    keys = {}
    with io.open(KEYS, encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            k = json.loads(ln)
            keys[k["item_id"]] = (k["truth"], k.get("fault_step"))
    sample = set(json.load(io.open(os.path.join(run, "SAMPLE.json"), encoding="utf-8"))["item_ids"])
    per = {}
    for arm in arms:
        d = os.path.join(arm_dir[arm][0], "verdicts", arm_dir[arm][1])
        rows = {}
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if not fn.endswith(".json"):
                    continue
                iid = fn[:-5]
                if iid not in sample:
                    continue
                raw = io.open(os.path.join(d, fn), encoding="utf-8").read()
                mv = re.search(r'"verdict"\s*:\s*"([^"]*)"', raw)
                ms = re.search(r'"fault_step"\s*:\s*(null|-?\d+|"[^"]*")', raw)
                if not mv or '"answer"' not in raw:
                    continue
                v = mv.group(1).strip().lower()
                v = "flawed" if (v.startswith("flaw") or v in ("invalid", "incorrect", "false")) else (
                    "clean" if (v.startswith("valid") or v in ("clean", "correct", "sound", "true")) else v)
                st = None
                if ms and ms.group(1) != "null":
                    try:
                        st = int(ms.group(1).strip('"'))
                    except ValueError:
                        st = None
                rows[iid] = (v, st)
        ok, fp, cn = {}, 0, 0
        for iid, (v, st) in rows.items():
            truth, fstep = keys[iid]
            if truth == "clean":
                cn += 1
                fp += int(v == "flawed")
            else:
                ok[iid] = (v == "flawed" and st == fstep)
        per[arm] = {"served": len(rows), "flawed_n": len(ok), "full_credit": sum(ok.values()), "clean_n": cn, "fp": fp, "ok": ok}
    ref = json.load(io.open(os.path.join(run, "results", a.label + ".json"), encoding="utf-8"))
    dis = []
    for arm in arms:
        r = ref["per_arm"][arm]
        mine = per[arm]
        for k1, k2 in (("served", "served"), ("flawed_n", "flawed_n"), ("full_credit", "full_credit")):
            if r[k1] != mine[k2]:
                dis.append("%s.%s: grader %s vs check %s" % (arm, k1, r[k1], mine[k2]))
        if r["clean_guard"]["false_positives"] != mine["fp"] or r["clean_guard"]["clean_n"] != mine["clean_n"]:
            dis.append("%s.clean_guard: grader %s vs check %s/%s" % (arm, r["clean_guard"], mine["fp"], mine["clean_n"]))

    def pair(a1, a2):
        ids = sorted(set(per[a1]["ok"]) & set(per[a2]["ok"]))
        b = sum(1 for i in ids if per[a1]["ok"][i] and not per[a2]["ok"][i])
        c = sum(1 for i in ids if per[a2]["ok"][i] and not per[a1]["ok"][i])
        return len(ids), b, c, binom_two_sided(b, c)
    for con in ref["contrasts"]:
        name = con["contrast"]
        if "detection only" in name:
            continue
        m = re.match(r"(\w+) vs (\w+)", name)
        if not m or m.group(1) not in per or m.group(2) not in per:
            continue
        n, b, c, p = pair(m.group(1), m.group(2))
        if (n, b, c) != (con["n_paired"], con["discordant_a_only"], con["discordant_b_only"]) or abs(p - con["mcnemar_exact_two_sided_p"]) > 1e-9:
            dis.append("%s: grader n=%s b=%s c=%s p=%s vs check n=%s b=%s c=%s p=%s" % (
                name, con["n_paired"], con["discordant_a_only"], con["discordant_b_only"], con["mcnemar_exact_two_sided_p"], n, b, c, p))
    out = {"label": a.label, "run": run, "per_arm": {k: {x: v[x] for x in ("served", "flawed_n", "full_credit", "clean_n", "fp")} for k, v in per.items()},
           "disagreements": dis}
    with io.open(os.path.join(run, "results", a.label + "_CHECK.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))
    return 1 if dis else 0


if __name__ == "__main__":
    sys.exit(main())
