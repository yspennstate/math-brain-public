# PROB20-14 artifact execution certificate

Artifact:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/forest_block_sizebias_check_20260916.py`

Purpose: finite-support algebra/indexing consistency check for the new exact block-size-bias representation and the relative-jump forest-to-coordinate tail inequality. This is **not** proof evidence for the universal infinite-variance theorem.

Test law:
\[
\Pr(\xi=0)=1/2,\qquad \Pr(\xi=1)=1/4,\qquad \Pr(\xi=3)=1/4,
\]
which is critical. Checker exponent: \(r=1/2\), \(q=3/2\).

The checker enumerated admissible pairs \(2\le m\le25\), \(1\le b<m\), verified exactly with rational arithmetic that
\[
\eta_{m,b}(c)=\frac{mc}{b(m-b)}Q_{m,b}(X_b=c),
\]
verified the normalization consequence
\[
\mathbb E_{Q_{m,b}}X_b=b(m-b)/m,
\]
checked the report's relative-jump inequality for \(M\in\{1,4,9,16\}\) whenever \(b\le m/2\), and checked deterministic emptiness of the relative-jump region when \(b>m/2\).

Actual execution output:

```text
IDENTITY_CHECKS=1986
TAIL_CHECKS=624
MAX_LHS_RHS_RATIO=0.0178159046426117
ALL_ASSERTIONS_PASSED
```

Status: **EXECUTED / ALL ASSERTIONS PASSED**.
