# PROB20-14 — conditioned-forest transition checker execution

**Status:** consistency check only; not proof evidence for the universal infinite-variance theorem.

Artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/forest_transition_factorization_check_20260916.py`

Artifact creation commit: `5ecd4a66407dddafb92bec57da20ae042c70ffd4`  
Artifact exact-commit blob: `fcc61c8a5d63dec63545e6382f86a097840b1562`

The checker was executed after the substantive Markdown report had been delivered. Test law:
\[
\Pr(\xi=0)=1/2,\qquad \Pr(\xi=1)=1/4,\qquad \Pr(\xi=3)=1/4,
\]
which is critical and finite-support. This law is used only for exact algebra/indexing consistency and does not model the target infinite-variance quantifiers.

Execution output:

```text
ALL_ASSERTIONS_PASSED
transition_cases= [(8, 1), (8, 2), (10, 2), (12, 3), (15, 4), (20, 5)]
product_cases= 117
kappa_spine_b=1..6 passed
tail_checks= [(1, 1.0, 0.0, 2.299038105676658), (1, 2.0, 0.0, 0.5), (1, 4.0, 0.0, 0.25), (2, 1.0, 0.0, 2.299038105676658), (2, 2.0, 0.0, 0.5), (2, 4.0, 0.0, 0.25), (3, 1.0, 0.0, 2.299038105676658), (3, 2.0, 0.0, 0.5), (3, 4.0, 0.0, 0.25), (5, 1.0, 0.0, 2.299038105676658), (5, 2.0, 0.0, 0.5), (5, 4.0, 0.0, 0.25), (10, 1.0, 0.0, 2.299038105676658), (10, 2.0, 0.0, 0.5), (10, 4.0, 0.0, 0.25)]
```

Checks performed:

- exact forest Dwass normalization for several \((m,b)\);
- exact equality \(\eta_{m,b}(c)=\kappa_b(c)L_{m,b}(c)\);
- exact normalization \(\mathbb E_{\kappa_b}L_{m,b}=1\) on interior states;
- exact Kesten transition identity \(\kappa_b=\mathcal L(\widehat\xi+\xi_1+\cdots+\xi_{b-1})\) for \(b=1,\dots,6\);
- 117 nonzero level-1-to-level-2 cases of the product identity \(R_{n,2}=R_{n,1}L_{n-1,B_1}(B_2)\);
- numerical consistency of the normalized fractional-tail inequality from Lemma 5.1 for selected \(b,M\).

The tail check is deliberately only a consistency check; for this bounded test law its left side is zero at the tested thresholds.
