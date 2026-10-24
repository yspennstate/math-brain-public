# PROB20-14 artifact execution certificate

**Timestamp:** 2026-09-16T05:03:10Z

Artifact checked:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/single_mark_tail_certificate_check_20260916.py`

Artifact creation commit: `be3c2ffe70914b5e516d1129e94449169a702998`  
Artifact blob after commit-specific readback: `dc1c7de063cb7df6b75094ea623eda24cda11e0a`

The checker logic was executed locally in this run using exact `Fraction` convolution probabilities for the critical finite-support test law
\[
\Pr(\xi=0)=1/2,\qquad \Pr(\xi=1)=1/4,\qquad \Pr(\xi=3)=1/4,
\]
with \(q=3/2\). It checked the unoptimized single-mark inequality for the genuinely soft mark
\[
g(0)=0,\qquad g(1)=1/5,\qquad g(3)=4/5,
\]
at several \(n\) and \(\theta\) values; checked the whole-tail hard-support consequence for several cutoffs; and checked the pre-optimization factorial denominator certificate in a regime where the marked multiplicity exceeded 8.

Actual stdout:

```text
single-mark direct inequalities: PASS
n=8: q_g=0.217557651992, lambda_n=2.150249675831
n=14: q_g=0.230294475500, lambda_n=2.464147727167
n=20: q_g=0.236234828033, lambda_n=2.632469081928
factorial pre-optimization certificate: PASS; multiplicity=17.535741142368, m=4, lambda_n=3.173212549689
```

All assertions passed. This is a finite algebra/indexing consistency check only; it is not independent verification of the infinite-variance theorem and is not promoted as proof evidence for the full target.