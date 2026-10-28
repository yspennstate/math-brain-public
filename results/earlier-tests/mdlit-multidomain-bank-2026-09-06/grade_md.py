# -*- coding: utf-8 -*-
# Copied from the probability campaign's grade_plit.py (2026-09-06) and re-pointed at the multi-domain bank; that lane's file is never edited from here.

"""grade_md.py - the pre-registered grade for the probability-literature bank (PROTOCOL_MDLIT.md), paired by item.

The B12/B13 rule, unchanged: a flawed item is correct when the verdict is "flawed" AND the reported fault_step equals
the key's fault step; a clean item is correct when the verdict reads valid/clean/correct/sound and feeds only the
false-positive guard. Contrasts: brain vs none (primary), brain vs placebo (content), any extra arm (brain_v2, ...)
vs none and vs brain. Descriptive slices: by operator, by tier, by external-reference count, by proof length; the
detection-only rate (verdict flawed, any step) beside full credit; the notes-coverage receipt when the notes file
carries scores. The pilot rule: the none arm above CEILING_NONE_RATE on flawed items means the bank is a ceiling for
this solver and no powered stage runs; otherwise n = ceil(784 * d) clamped to [120, 400] flawed pairs plus clean.

    python grade_md.py [--run run_md] [--label PILOT] [--arms none,brain,placebo]
Read-only over <run>/verdicts; writes <run>/results/<LABEL>.json and .md.
"""
import argparse
import collections
import glob
import io
import json
import math
import os
import time
from validity_gate import validate_run

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = r"<HOME>/bank_multidomain_keys_quarantine\mdlit_keys.jsonl"
FP_GUARD_PP = 10.0
CEILING_NONE_RATE = 0.85


def mcnemar_exact_two_sided(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    return min(1.0, 2.0 * sum(math.comb(n, i) for i in range(0, k + 1)) / 2.0 ** n)


def paired_diff_ci(b, c, n):
    if n == 0:
        return None, None, None
    d = (b - c) / n
    se = math.sqrt(max(0.0, (b + c) - (b - c) ** 2 / n)) / n
    return d, d - 1.96 * se, d + 1.96 * se


def norm(v):
    v = str(v or "").strip().lower()
    if v.startswith("flaw") or v in ("invalid", "incorrect", "false"):
        return "flawed"
    if v.startswith("valid") or v in ("clean", "correct", "sound", "true"):
        return "clean"
    return v


def load_keys():
    keys = {}
    for ln in io.open(KEYS, encoding="utf-8"):
        if ln.strip():
            k = json.loads(ln)
            keys[k["item_id"]] = k
    return keys


def load_arm(run, arm, sample):
    rows = {}
    for p in glob.glob(os.path.join(run, "verdicts", arm, "*.json")):
        try:
            r = json.load(io.open(p, encoding="utf-8"))
        except Exception:
            continue
        if r.get("item_id") in sample and r.get("answer"):
            rows[r["item_id"]] = r
    return rows


def _squash(s):
    return "".join(ch for ch in str(s or "").lower() if ch.isalnum())


def reason_hit(answer, key):
    """Descriptive only: does the solver's 'why' name the changed text (the inserted or the removed token, or the
    operator's mechanism words)? A right step with a wrong reason is still full credit under the B12 rule; this
    receipt says how often the reason also matched."""
    why = _squash(answer.get("why"))
    if not why:
        return False
    for t in (key.get("inserted"), key.get("removed")):
        t2 = _squash(t)
        if len(t2) >= 3 and t2 in why:
            return True
    words = {"ineq_flip": ("inequal", "direction", "revers", "shouldbe", "sign"),
             "limop_swap": ("sup", "inf", "max", "min", "limsup", "liminf"),
             "setop_swap": ("union", "intersect", "subset", "superset", "cup", "cap", "contain"),
             "quantifier_swap": ("forall", "exist", "quantif", "every", "some"),
             "limit_target": ("limit", "tendsto", "goesto", "infinity", "zero"),
             "index_shift": ("index", "offbyone", "shift", "plus1", "minus1", "n1", "k1"),
             "word_flip": ("increas", "decreas", "atmost", "atleast", "positive", "negative", "upper", "lower", "finite",
                           "convex", "concave", "larger", "smaller", "sub", "super"),
             "hypothesis_swap": ("uncorrelat", "independ", "probabil", "almostsure", "pointwise", "uniform", "measurab",
                                 "continu", "l1", "l2", "compact", "closed", "martingale"),
             "hypothesis_drop": ("independ", "bounded", "uniform", "integrab", "finite", "continu", "nonneg", "increas",
                                 "measurab", "compact", "positive", "hypothes", "assum", "missing", "requir"),
             "theorem_swap": ("theorem", "lemma", "inequality", "formula", "cite", "misapp", "doesnotapply", "applies"),
             "const_change": ("constant", "exponent", "factor", "power", "coefficient", "square", "cube"),
             "sign_flip": ("sign", "plus", "minus", "negat"),
             "ineq_to_eq": ("equal", "inequal", "strict")}
    return any(w in why for w in words.get(key.get("family_id"), ()))


def score(rows, keys):
    """ok[iid] full credit on flawed items; det[iid] detection only; clean guard counts; rh[iid] reason receipt."""
    ok, det, rh = {}, {}, {}
    c_n = c_fp = 0
    for iid, r in rows.items():
        k = keys[iid]
        a = r["answer"]
        v = norm(a.get("verdict"))
        if k["truth"] == "clean":
            c_n += 1
            c_fp += int(v == "flawed")
            continue
        det[iid] = (v == "flawed")
        good = False
        if v == "flawed":
            try:
                good = int(a.get("fault_step")) == int(k["fault_step"])
            except (TypeError, ValueError):
                good = False
        ok[iid] = good
        rh[iid] = bool(good and reason_hit(a, k))
    score.last_reason = rh
    return ok, det, c_n, c_fp


def contrast(name, a_ok, b_ok):
    paired = sorted(set(a_ok) & set(b_ok))
    b = sum(1 for i in paired if a_ok[i] and not b_ok[i])
    c = sum(1 for i in paired if b_ok[i] and not a_ok[i])
    d, lo, hi = paired_diff_ci(b, c, len(paired))
    return {
        "contrast": name, "n_paired": len(paired),
        "a_correct": sum(a_ok[i] for i in paired), "b_correct": sum(b_ok[i] for i in paired),
        "diff_pp": None if d is None else 100 * d, "ci95_pp": None if d is None else [100 * lo, 100 * hi],
        "discordant_a_only": b, "discordant_b_only": c,
        "mcnemar_exact_two_sided_p": mcnemar_exact_two_sided(b, c),
        "room_to_fail_pp": None if not paired else 100 * (1 - sum(b_ok[i] for i in paired) / len(paired)),
        "a_only_ids": [i for i in paired if a_ok[i] and not b_ok[i]][:60],
        "b_only_ids": [i for i in paired if b_ok[i] and not a_ok[i]][:60],
    }


def slice_table(ok_by_arm, keys, field, arms):
    out = {}
    ids = set()
    for a in arms:
        ids |= set(ok_by_arm.get(a, {}))
    groups = collections.defaultdict(list)
    for i in ids:
        groups[str(keys[i].get(field))].append(i)
    for g, members in sorted(groups.items()):
        row = {}
        for a in arms:
            m = [i for i in members if i in ok_by_arm.get(a, {})]
            row[a] = "%d/%d" % (sum(ok_by_arm[a][i] for i in m), len(m))
        out[g] = row
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="run_md")
    ap.add_argument("--label", default="PILOT")
    ap.add_argument("--arms", default="none,brain,placebo")
    ap.add_argument("--extra-arm", action="append", default=[],
                    help="NAME=RUNDIR[:ARM] - an arm served in another run directory (the sterile runner only knows "
                         "none/brain/placebo, so brain_v2 is served as 'brain' inside its own run view that holds the "
                         "same SAMPLE.json and the v2 notes as brain_notes.json)")
    a = ap.parse_args()
    run = a.run if os.path.isabs(a.run) else os.path.join(HERE, a.run)
    validate_run(run, HERE)
    arms = [x.strip() for x in a.arms.split(",") if x.strip()]
    keys = load_keys()
    sample = json.load(io.open(os.path.join(run, "SAMPLE.json"), encoding="utf-8"))
    sids = set(sample["item_ids"])
    rows = {arm: load_arm(run, arm, sids) for arm in arms}
    extra_dirs = {}
    for spec in a.extra_arm:
        name, rest = spec.split("=", 1)
        rd, _, served_as = rest.partition(":")
        served_as = served_as or "brain"
        rd = rd if os.path.isabs(rd) else os.path.join(HERE, rd)
        validate_run(rd, HERE)
        s2 = json.load(io.open(os.path.join(rd, "SAMPLE.json"), encoding="utf-8"))
        if set(s2["item_ids"]) != sids:
            raise SystemExit("extra arm %s: its SAMPLE.json is not the same item set as %s" % (name, run))
        rows[name] = load_arm(rd, served_as, sids)
        extra_dirs[name] = (rd, served_as)
        arms.append(name)
    ok, det, guard = {}, {}, {}
    per_arm = {}
    for arm in arms:
        o, d, c_n, c_fp = score(rows[arm], keys)
        rh = getattr(score, "last_reason", {})
        ok[arm], det[arm] = o, d
        guard[arm] = {"clean_n": c_n, "false_positives": c_fp, "fp_rate": (c_fp / c_n) if c_n else None}
        per_arm[arm] = {
            "served": len(rows[arm]), "flawed_n": len(o), "full_credit": sum(o.values()),
            "full_credit_rate": (sum(o.values()) / len(o)) if o else None,
            "detected_any_step": sum(d.values()), "detected_rate": (sum(d.values()) / len(d)) if d else None,
            "full_credit_with_reason_receipt": sum(rh.values()),
            "clean_guard": guard[arm],
        }
    contrasts = []
    if "brain" in arms and "none" in arms:
        contrasts.append(contrast("brain vs none (PRIMARY, full credit)", ok["brain"], ok["none"]))
        contrasts.append(contrast("brain vs none (detection only)", det["brain"], det["none"]))
    if "brain" in arms and "placebo" in arms:
        contrasts.append(contrast("brain vs placebo (CONTENT, full credit)", ok["brain"], ok["placebo"]))
    if "placebo" in arms and "none" in arms:
        contrasts.append(contrast("placebo vs none (descriptive)", ok["placebo"], ok["none"]))
    for extra in arms:
        if extra in ("none", "brain", "placebo"):
            continue
        if "none" in arms:
            contrasts.append(contrast("%s vs none (full credit)" % extra, ok[extra], ok["none"]))
        if "brain" in arms:
            contrasts.append(contrast("%s vs brain (full credit)" % extra, ok[extra], ok["brain"]))
    guard_flags = {}
    if "none" in arms:
        for arm in arms:
            if arm != "none" and guard[arm]["fp_rate"] is not None and guard["none"]["fp_rate"] is not None:
                diff = 100 * (guard[arm]["fp_rate"] - guard["none"]["fp_rate"])
                guard_flags[arm] = {"fp_diff_pp_vs_none": diff, "flag": diff > FP_GUARD_PP}
    # pilot rule
    pilot = {}
    if "none" in arms and ok["none"]:
        none_rate = sum(ok["none"].values()) / len(ok["none"])
        pilot["none_full_credit_rate"] = none_rate
        pilot["ceiling"] = none_rate > CEILING_NONE_RATE
        if "brain" in arms:
            pr = contrasts[0]
            n = pr["n_paired"]
            dsc = (pr["discordant_a_only"] + pr["discordant_b_only"]) / n if n else None
            pilot["discordance_rate"] = dsc
            pilot["powered_n_flawed"] = None if dsc is None else max(120, min(400, math.ceil(784 * dsc)))
    # notes coverage receipt: how often a served note's title shares a rare token with the claim
    coverage = {}
    for arm in ("brain", "placebo") + tuple(x for x in arms if x not in ("none", "brain", "placebo")):
        if arm in extra_dirs:
            p = os.path.join(extra_dirs[arm][0], extra_dirs[arm][1] + "_notes.json")
        else:
            p = os.path.join(run, arm + "_notes.json")
        if not os.path.exists(p):
            continue
        blob = json.load(io.open(p, encoding="utf-8"))
        notes = blob.get("notes", {})
        n_items = len([i for i in notes if i in sids])
        empty = sum(1 for i in notes if i in sids and not notes[i])
        coverage[arm] = {"items": n_items, "empty": empty, "store": blob.get("store"), "n_nodes": blob.get("n_nodes"),
                         "label": blob.get("label")}
        # literature notes: how many served sets contain a statement from the item's OWN paper (a memory of the
        # paper's other results) and how many items got at least one literature node at all
        lit_ids = {nid for i in notes if i in sids for nid in (n.get("node_id") for n in notes[i]) if str(nid).startswith("lit_")}
        if lit_ids and blob.get("store") and os.path.exists(blob["store"]):
            import sqlite3
            con = sqlite3.connect("file:" + blob["store"].replace("\\", "/") + "?mode=ro", uri=True)
            paper_of = {}
            for nid, meta in con.execute("select id, metadata_json from nodes where id like 'lit_%'"):
                try:
                    paper_of[nid] = json.loads(meta or "{}").get("paper")
                except Exception:
                    pass
            con.close()
            same = with_lit = 0
            same_ids = []
            for i in notes:
                if i not in sids:
                    continue
                nids = [n.get("node_id") for n in notes[i]]
                if any(str(x).startswith("lit_") for x in nids):
                    with_lit += 1
                if any(paper_of.get(x) == keys[i].get("paper") for x in nids):
                    same += 1
                    same_ids.append(i)
            coverage[arm]["items_with_literature_note"] = with_lit
            coverage[arm]["items_with_same_paper_note"] = same
            if arm in ok and same_ids:
                m = [i for i in same_ids if i in ok[arm]]
                o = [i for i in ok[arm] if i not in same_ids]
                coverage[arm]["full_credit_same_paper"] = "%d/%d" % (sum(ok[arm][i] for i in m), len(m))
                coverage[arm]["full_credit_other"] = "%d/%d" % (sum(ok[arm][i] for i in o), len(o))
                if "none" in ok:
                    mn = [i for i in m if i in ok["none"]]
                    on = [i for i in o if i in ok["none"]]
                    coverage[arm]["none_full_credit_same_paper_items"] = "%d/%d" % (sum(ok["none"][i] for i in mn), len(mn))
                    coverage[arm]["none_full_credit_other_items"] = "%d/%d" % (sum(ok["none"][i] for i in on), len(on))
    out = {
        "label": a.label, "run": run, "graded_at": time.strftime("%Y-%m-%d %H:%M:%S"), "protocol": "PROTOCOL_MDLIT.md",
        "keys_file": KEYS, "sample": {k: v for k, v in sample.items() if k != "item_ids"},
        "extra_arms": {k: {"run": v[0], "served_as": v[1]} for k, v in extra_dirs.items()},
        "per_arm": per_arm, "contrasts": contrasts, "guard_flags": guard_flags, "pilot_rule": pilot,
        "by_operator": slice_table(ok, keys, "family_id", arms),
        "by_tier": slice_table(ok, keys, "tier", arms),
        "by_external_refs": slice_table(ok, keys, "external_refs", arms),
        "by_kind": slice_table(ok, keys, "kind", arms),
        "by_year": slice_table(ok, {i: dict(k, year=str(k.get("published", ""))[:4]) for i, k in keys.items()}, "year", arms),
        "notes_coverage": coverage,
    }
    os.makedirs(os.path.join(run, "results"), exist_ok=True)
    with io.open(os.path.join(run, "results", a.label + ".json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    lines = ["# %s grade (%s)" % (a.label, os.path.basename(run)), ""]
    for arm in arms:
        pa = per_arm[arm]
        g = pa["clean_guard"]
        lines.append("%-9s served %3d | flawed full credit %s/%s (%s) | detected %s/%s | clean FP %s/%s" % (
            arm, pa["served"], pa["full_credit"], pa["flawed_n"],
            "-" if pa["full_credit_rate"] is None else "%.1f%%" % (100 * pa["full_credit_rate"]),
            pa["detected_any_step"], pa["flawed_n"], g["false_positives"], g["clean_n"]))
    lines.append("")
    for c in contrasts:
        lines.append("%s: n=%d a=%d b=%d diff=%s pp CI=%s discordants %d/%d p=%.4f room=%s" % (
            c["contrast"], c["n_paired"], c["a_correct"], c["b_correct"],
            "-" if c["diff_pp"] is None else "%+.1f" % c["diff_pp"],
            "-" if c["ci95_pp"] is None else "[%.1f, %.1f]" % tuple(c["ci95_pp"]),
            c["discordant_a_only"], c["discordant_b_only"], c["mcnemar_exact_two_sided_p"],
            "-" if c["room_to_fail_pp"] is None else "%.1f pp" % c["room_to_fail_pp"]))
    lines.append("")
    lines.append("pilot rule: " + json.dumps(pilot))
    lines.append("guard flags: " + json.dumps(guard_flags))
    lines.append("by operator: " + json.dumps(out["by_operator"]))
    lines.append("by tier: " + json.dumps(out["by_tier"]))
    lines.append("by external refs: " + json.dumps(out["by_external_refs"]))
    lines.append("notes coverage: " + json.dumps(coverage))
    with io.open(os.path.join(run, "results", a.label + ".md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
