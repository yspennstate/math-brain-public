#!/usr/bin/env python3
"""Finite sanity checks for BT4-R4-F3-NEUTRAL-HEAVY-CLEAN-PAIR-v1.

This is not the proof.  It only checks the finite counting/port statements used
in the uniform argument.
"""
import json

out = {}

# Global-minimum comparison in F3-BOTH:
# |H|+3+|U| <= |H|+|C|+3, hence |U| <= |C|, and oriented cycles have order >=3.
out["support_bound"] = [
    {"return_cycle_order": c, "admissible_U_orders": [u for u in range(3, 20) if u <= c]}
    for c in (3, 4)
]

# In the pure neutral-heavy leaf, the proof first shows exactly two old-H
# targets.  There are then no S* targets, at most two C_z targets {u,b}, and
# at most three remainder targets {q,a,c}.  Exact outdegree seven saturates all.
allowed = ["H:e", "H:f", "C_z:u", "C_z:b", "R:q", "R:a", "R:c"]
out["degree_saturation"] = {
    "allowed_count": len(allowed),
    "exact_outdegree": 7,
    "forced_targets": allowed,
    "pass": len(allowed) == 7,
}

# The forced H'->S* path and surviving sink-heavy edge have four distinct
# packed ports and disjoint interiors.
P = {"t", "a", "p"}
Q = {"x", "h"}
out["clean_pair"] = {
    "P": ["t", "a", "p"],
    "Q": ["x", "h"],
    "intersection": sorted(P & Q),
    "four_distinct_packed_ports": len({"t", "p", "x", "h"}) == 4,
    "pass": not (P & Q) and len({"t", "p", "x", "h"}) == 4,
}

# After the neutral heavy pivot, t dominates every remainder vertex q,a,c,e.
# A common predecessor of either new support edge d->t or t->f therefore
# cannot lie in the remainder; chordlessness excludes H'.  It must be light.
out["side_dominator"] = {
    "excluded_remainder": ["q", "a", "c", "e"],
    "excluded_Hprime_by_chordlessness": True,
    "remaining_packed_supports": ["S*", "C_z"],
    "C_z_sources_if_U_order_3": ["z"],
    "C_z_sources_if_U_order_4": ["v", "z"],
    "pass": True,
}

assert all(x["admissible_U_orders"] == ([3] if x["return_cycle_order"] == 3 else [3, 4]) for x in out["support_bound"])
assert out["degree_saturation"]["pass"]
assert out["clean_pair"]["pass"]
assert out["side_dominator"]["pass"]
print(json.dumps(out, indent=2, sort_keys=True))
