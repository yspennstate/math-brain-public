#!/usr/bin/env python3
"""Finite index sanity check for the BT4 U1 external-dominator escape lemma.

This checks only the bounded index descent m<=7 forced by exact outdegree seven.
The graph-theoretic proof (arc domination, chordlessness, path-fan exclusion,
and single-port exclusion) is in report.md.
"""

def chains(m, i):
    # Start with the dominated arc p_{m-1}->b_i.
    # If its dominator remains on the tight path, it must be p_h with
    # i-1 <= h < j for the currently dominated arc p_j->b_i.
    # "E" means the next dominator is forced outside C union P.
    out = []
    def rec(j, seq):
        out.append(tuple(seq) + ("E",))
        for h in range(i - 1, j):
            rec(h, seq + [h])
    rec(m - 1, [])
    return out

rows = []
for m in range(3, 8):
    for i in range(2, m):
        cs = chains(m, i)
        max_internal = max(len(c) - 1 for c in cs)
        expected = m - i
        assert max_internal == expected
        assert all(c[-1] == "E" for c in cs)
        # Any fully internal descent bottoms at p_{i-1}; one more
        # domination step cannot stay on the path.
        rows.append((m, i, len(cs), max_internal))

for m, i, n, depth in rows:
    print(f"m={m} i={i} chains={n} max_internal_path_dominators={depth}")
print(f"PASS cases={len(rows)} m_range=3..7 forced_external=true")
