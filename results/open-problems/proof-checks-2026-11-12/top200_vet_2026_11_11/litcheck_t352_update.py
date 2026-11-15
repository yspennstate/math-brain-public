"""T352 row of LITCHECK.tsv after reading Theorem 3.3 of arXiv 2401.10371v7 and two follow-up abstracts (T352_READ.md)."""
NEW = ("CONFIRMED_WITH_BETTER_CITATION: Theorem 3.3 of 2401.10371v7 (read in the paper) gives a T-independent Renyi DP bound "
       "without convexity for FULL-BATCH projected noisy GD on a ball, constant exponential in R^2/(eta sigma^2); minibatches "
       "are only remarked on. Hidden-state Noisy-SGD on a bounded domain for nonconvex nonsmooth losses is Chien-Li 2410.01068v2, "
       "projected DP-SGD is Asoodeh-Diaz 2305.09903v1 (abstracts read). Removal stands; cite those. Not covered: unbounded "
       "domain without projection or clipping, non-exponential constants (paper and abstracts read 2026-11-11, an agent; "
       "see T352_READ.md)")
with open("LITCHECK.tsv", encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
n = 0
for i, l in enumerate(lines):
    p = l.split("\t")
    if p[0] == "T352" and len(p) >= 5:
        p[4] = NEW
        lines[i] = "\t".join(p); n += 1
assert n == 1, n
with open("LITCHECK.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
print("rows updated:", n)
